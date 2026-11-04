"""
Run the registration SQL against club.db, print results and save charts.

Usage:  python analyse.py
"""
import sqlite3
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
DB = ROOT / "data" / "club.db"
SQL = (ROOT / "sql" / "registration_analysis.sql").read_text()
CHARTS = ROOT / "charts"
CHARTS.mkdir(exist_ok=True)

INK, MUTED, ACCENT, ALERT = "#14213D", "#9AA5B1", "#1D5FA8", "#C2410C"
plt.rcParams.update({"font.size": 10, "axes.spines.top": False,
                     "axes.spines.right": False, "axes.edgecolor": MUTED})

queries = [q.strip() for q in SQL.split(";") if "SELECT" in q.upper()]
with sqlite3.connect(DB) as con:
    for i, q in enumerate(queries, 1):
        print(f"\n--- Q{i} ---\n{pd.read_sql_query(q, con).to_string(index=False)}")
    df = pd.read_sql_query("SELECT * FROM registrations", con,
                           parse_dates=["registration_date", "paid_date"])

s26 = df[df.season == 2026]

# Chart 1: cumulative fees collected, 2026 season
paid = s26.dropna(subset=["paid_date"]).sort_values("paid_date")
cum = paid.groupby("paid_date")["amount_paid_aud"].sum().cumsum() / s26.fee_due_aud.sum() * 100
fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(cum.index, cum.values, color=INK, lw=2)
for label, dt in [("Grading deadline", "2026-02-14"), ("Round 1", "2026-04-11")]:
    ax.axvline(pd.Timestamp(dt), color=ALERT, ls="--", lw=1)
    ax.text(pd.Timestamp(dt), 4, f" {label}", color=ALERT)
r1 = cum[cum.index <= "2026-04-11"].iloc[-1]
ax.annotate(f"{r1:.0f}% collected by round 1", xy=(pd.Timestamp("2026-04-11"), r1),
            xytext=(pd.Timestamp("2026-05-10"), r1 - 22), arrowprops=dict(arrowstyle="->", color=INK))
ax.axhline(cum.iloc[-1], color=MUTED, lw=1, ls=":")
ax.text(pd.Timestamp("2026-06-10"), cum.iloc[-1] + 1.5, f"{cum.iloc[-1]:.0f}% by season end", color=INK)
ax.set_ylim(0, 100)
ax.set_ylabel("% of 2026 fees collected")
ax.xaxis.set_major_formatter(mdates.DateFormatter("%b"))
ax.set_title("2026 club fees collected over the season", loc="left")
fig.tight_layout(); fig.savefig(CHARTS / "01_fee_collection_2026.png", dpi=150); plt.close(fig)

# Chart 2: weekly registrations vs grading deadline, 2026
wk = s26.set_index("registration_date").resample("2W")["player_id"].count()
fig, ax = plt.subplots(figsize=(8, 3.8))
colors = [INK if d <= pd.Timestamp("2026-02-14") else ALERT for d in wk.index]
ax.bar(wk.index, wk.values, width=10, color=colors)
ax.axvline(pd.Timestamp("2026-02-14"), color=ALERT, ls="--", lw=1)
late = 100 - s26.before_grading_deadline.mean() * 100
ax.text(pd.Timestamp("2026-02-17"), wk.max() * 0.9, f"{late:.0f}% registered after\nthe grading deadline", color=ALERT)
ax.set_title("2026 registrations per fortnight", loc="left")
ax.set_ylabel("Players")
ax.xaxis.set_major_formatter(mdates.DateFormatter("%b"))
fig.tight_layout(); fig.savefig(CHARTS / "02_registration_timing_2026.png", dpi=150); plt.close(fig)

# Chart 3: retention by fee status
ret = df[df.season.isin([2024, 2025]) & (df.age_group != "U14")].groupby("unpaid_at_season_end")["returned_next_season"].mean() * 100
fig, ax = plt.subplots(figsize=(6, 3.4))
labels = ["Paid their fees", "Fees still unpaid\nat season end"]
ax.barh(labels[::-1], [ret[1], ret[0]], color=[ALERT, INK])
for y, v in enumerate([ret[1], ret[0]]):
    ax.text(v + 1, y, f"{v:.0f}%", va="center", color=INK)
ax.set_xlim(0, 100)
ax.set_title("Players who came back the next season\n(2024–25, excluding U14s who age out)", loc="left")
fig.tight_layout(); fig.savefig(CHARTS / "03_retention_by_fee_status.png", dpi=150); plt.close(fig)

print(f"\nCharts saved to {CHARTS}")
