"""
Generate synthetic registration and payment data for a small, fictional local junior soccer club
(under 14s, about 65 members). Seasons 2024-2026.

The generator follows the as-is process uncovered in discovery:
  * club fees are paid by bank transfer, cash or card at the clubroom, outside
    the federation's online registration portal
  * families with 2+ children wait for the registrar to work out the sibling
    discount by hand, so they pay later
  * bank transfers often arrive without a usable reference, so they need
    manual matching
  * many players register after the team grading deadline
  * players with unpaid fees are less likely to come back the next season
  * players who age out of U14 leave the club (it has no older teams)

Usage:  python generate_data.py   (writes ../data/*.csv and ../data/club.db)
"""
import random
import sqlite3
from datetime import date, timedelta
from pathlib import Path

import pandas as pd
import os
SEED = int(os.environ.get("SEED", 3))

random.seed(SEED)
OUT = Path(__file__).resolve().parent.parent / "data"
OUT.mkdir(exist_ok=True)

SEASONS = [2024, 2025, 2026]


def age_group(age):
    return f"U{age + 1}"


def fee(age):
    return 160 if age <= 7 else 220


def key_dates(season):
    return dict(
        opens=date(season - 1, 12, 1),
        early_bird=date(season, 1, 31),
        grading=date(season, 2, 14),
        round1=date(season, 4, 11),
        season_end=date(season, 8, 31),
    )


# ---------- build the player pool ----------
next_pid, next_fid = 1, 1
players = {}  # pid -> dict(age, family_id, gender)


def new_family(ages):
    global next_pid, next_fid
    fid = f"F{next_fid:04d}"
    next_fid += 1
    pids = []
    for a in ages:
        pid = f"P{next_pid:05d}"
        next_pid += 1
        players[pid] = dict(age=a, family_id=fid,
                            gender="F" if random.random() < 0.31 else "M")
        pids.append(pid)
    return pids


def random_family_ages():
    n = random.choices([1, 2, 3], weights=[0.62, 0.30, 0.08])[0]
    first = random.randint(4, 13)
    return [max(4, min(13, first + random.randint(-3, 3))) for _ in range(n)]


active = []
while len(active) < 60:
    active += new_family(random_family_ages())

rows = []
prev_unpaid = set()
for season in SEASONS:
    d = key_dates(season)
    fam_counts = {}
    for pid in active:
        fam_counts[players[pid]["family_id"]] = fam_counts.get(players[pid]["family_id"], 0) + 1

    fam_rank = {}
    for pid in active:
        p = players[pid]
        fid = p["family_id"]
        fam_rank[fid] = fam_rank.get(fid, 0) + 1
        siblings = fam_counts[fid]
        returning = p.get("seasons", 0) > 0

        # registration date: returning players a little earlier
        mean_days = 62 if returning else 80
        offset = int(random.expovariate(1 / mean_days))
        while offset > 140:  # registrations close mid-April
            offset = int(random.expovariate(1 / mean_days))
        reg = d["opens"] + timedelta(days=offset)
        base = fee(p["age"])
        early = reg <= d["early_bird"]
        discount = 30 if early else 0
        sibling_disc = round(base * 0.10) if fam_rank[fid] >= 2 else 0
        due = base - discount - sibling_disc

        method = random.choices(["bank_transfer", "cash", "card_clubroom"],
                                weights=[0.72, 0.18, 0.10])[0]
        hardship = random.random() < 0.04

        mean_pay = 24 + (22 if siblings >= 2 else 0) + (15 if hardship else 0)
        days_to_pay = int(random.expovariate(1 / mean_pay))
        never_pays = random.random() < (0.055 + (0.03 if siblings >= 2 else 0))
        if never_pays:
            paid_date = None
        else:
            paid_date = reg + timedelta(days=days_to_pay)
            if paid_date > d["season_end"]:
                paid_date = None

        missing_ref = method == "bank_transfer" and paid_date is not None and random.random() < 0.18
        paid = due if paid_date else 0
        rows.append(dict(
            season=season, player_id=pid, family_id=fid, gender=p["gender"],
            age=p["age"], age_group=age_group(p["age"]),
            player_type="returning" if returning else "new",
            siblings_registered=siblings,
            registration_date=reg.isoformat(),
            before_grading_deadline=int(reg <= d["grading"]),
            early_bird=int(early), fee_due_aud=due,
            payment_method=method, hardship_request=int(hardship),
            paid_date=paid_date.isoformat() if paid_date else None,
            days_to_pay=(paid_date - reg).days if paid_date else None,
            paid_by_round1=int(paid_date is not None and paid_date <= d["round1"]),
            unpaid_at_season_end=int(paid_date is None),
            amount_paid_aud=paid,
            missing_bank_reference=int(missing_ref),
        ))

    # ---------- who comes back next season ----------
    unpaid_now = {r["player_id"] for r in rows if r["season"] == season and r["unpaid_at_season_end"]}
    nxt = []
    for pid in active:
        p = players[pid]
        p["seasons"] = p.get("seasons", 0) + 1
        p_return = 0.82
        if p["age"] >= 13:      # aged out of U14: the club has no older teams
            p_return = 0.0
        if pid in unpaid_now:
            p_return -= 0.35
        if random.random() < p_return:
            p["age"] += 1
            nxt.append(pid)
    # mark retention on this season's rows
    nxt_set = set(nxt)
    for r in rows:
        if r["season"] == season:
            r["returned_next_season"] = int(r["player_id"] in nxt_set) if season < SEASONS[-1] else None
    # recruit new players, slight growth
    target = int(len(active) * 1.03) if season < 2026 else 0
    while len(nxt) < target:
        nxt += new_family(random_family_ages())
    active = nxt

df = pd.DataFrame(rows)
df.to_csv(OUT / "registrations.csv", index=False)

db = OUT / "club.db"
db.unlink(missing_ok=True)
with sqlite3.connect(db) as con:
    df.to_sql("registrations", con, index=False)

print(df.groupby("season").size().to_string())
print(f"{len(df):,} rows -> {OUT}")
