# Project Charter
**Project:** Club platform for a local junior soccer club: public website, committee admin portal and member app
**Client:** a local community soccer club for children under 14, with about 65 players, 6 teams and a committee made up entirely of volunteers
**Delivery partner:** the digital agency I work for, which is building a reusable platform for community sports clubs. This club is its first pilot client.
**Prepared by:** Business Analyst (agency side) | **Version:** 1.4 | **Status:** Signed by club and agency

> The club, the people and all data in this repository are fictional and were made up for a portfolio case study.

---

## 1. Background
The club runs on goodwill, a spreadsheet and a handful of WhatsApp groups. Every December families register their children through the state federation's portal. Club fees are collected separately by bank transfer or cash, and the treasurer matches payments by hand. Each coach chases Saturday availability in a group chat. Parents with two or three children juggle several chats and invoices. The club's website is an old free page that nobody on the committee knows how to update.

The agency is building a platform for community clubs and offered this club a place as its pilot client, at a subsidised price. I led discovery with the club. I also work with the agency's own product, design and engineering teams to turn what the club needs into something that works for many clubs, not just this one.

## 2. Problem statement
> The club is small, but its volunteers carry the same admin load as a big club. In 2026:
> - **A$2.3K of fees (20%) was still unpaid at round 1**, spread across 12 families the treasurer had to chase personally.
> - **15% of players registered after the team grading deadline.**
> - **27% of bank transfers arrived without a usable reference.**
> - Volunteers spent an estimated **220 hours a season** on admin.
> - The child safety officer could not show at a glance that every coach and team manager held a current Working With Children Check (WWCC).

## 3. Objectives
| # | Objective | Baseline (2026) | Target (2027 season) |
|---|-----------|----------------:|---------------------:|
| O1 | Fees paid by round 1 | 79.7% | **≥ 95%** |
| O2 | Players registered before the grading deadline | 84.6% | **≥ 95%** |
| O3 | Volunteer admin hours per season | ~220 | **≤ 80** |
| O4 | Coaches and team managers with a verified WWCC before their first session | Spreadsheet, not checked | **100%, enforced by the system** |
| O5 | Families using the app by round 3 | 0 | **≥ 90%** (about 46 of 51 families) |
| O6 | Players returning next season (excluding U14s, who age out) | ~78% | **≥ 85%** |

## 4. Scope
### Products
| Product | Users | Core purpose |
|---------|-------|--------------|
| **Public website** | Prospective families, sponsors, local community | Club info, news, fixtures and results, "Join the club", sponsor logos |
| **Committee admin portal** (web) | President, secretary/registrar, treasurer, child safety officer, coach coordinator | Registrations, fees, teams, WWCC compliance, volunteer roster, announcements, website content |
| **Member app** (iOS and Android, one app with role-based views) | **Parents & guardians**, **coaches & team managers**, **players** (a view-only profile that a parent controls) | Register and pay, fixtures, availability, team announcements, attendance, volunteer duties |

### In scope
- Online registration and payment for club fees, with the sibling discount, early-bird pricing and a confidential hardship option
- Daily sync with the state federation's registration portal (players must still be registered with the federation)
- Team allocation for the coach coordinator
- WWCC capture, expiry alerts and a hard block on assigning unverified adults to a team
- Match availability, training attendance, team announcements and push notifications
- Volunteer roster for duties such as canteen, setting up goals and ground marshal, with swaps
- Website pages the committee can edit without technical skills

### Out of scope (Release 3 backlog)
- Canteen pre-ordering and merchandise shop
- Player stats, photos and video (child-safety review needed first)
- Ground bookings (the Council allocates grounds through its own system)

## 5. Options analysis
| Option | Description | Club cost (yr 1) | Fit | Verdict |
|--------|-------------|-----------------:|-----|---------|
| A | Keep the spreadsheet, chats and bank transfers | A$0 | Low: no online payment, compliance or availability | ✗ Volunteer burnout continues |
| B | Off-the-shelf generic team app + separate website builder | ~A$700 | Medium: covers team chat and fixtures, but not the club's fee rules, the federation sync or the WWCC block; it also allows direct messaging with children | Considered |
| C | **Pilot client on the agency's club platform** | **A$12K + A$900/yr** | **High: meets all 32 Must requirements** | **✓ Recommended** |
| D | Bespoke build just for this club | ~A$85K | High | ✗ Not affordable for a 65-member club |

**Why C over B:** I scored both options against the 32 Must requirements (functional and non-functional). Option B met 18 of them. Its gaps were the things that matter most to this committee: online fee collection with sibling discounts (O1), WWCC enforcement (O4), and messaging that stays within the club's child-safe policy.

**Honest caveat:** for a club this size, B is a reasonable choice. C only makes sense because the agency is paying for most of the build as an investment in its product. I recorded this in the decision log so the committee chose with full information.

## 6. Funding
### Club
| Item | A$ |
|------|---:|
| Pilot fee (setup, configuration, data migration, training) | 12,000 |
| Funded by | Council community grant A$10,000 + club funds A$2,000 |
| Running cost (licence, SMS, app store) | 900 / yr, paid from a A$15 rise in fees per player (≈ A$975) |

### Agency (internal business case, owned by the agency's Product Manager)
| Item | A$ |
|------|---:|
| Platform build (Release 1 + 2) | 95,000 |
| Recovered through pilot fee | 12,000 |
| Target: 60 clubs on A$900–1,800/yr licences within 2 years | ~A$80K/yr recurring |

## 7. Timeline
| Phase | Dates | Milestone |
|-------|-------|-----------|
| Discovery | 4 Aug – 12 Sep 2026 | Requirements baselined, pilot agreement signed |
| Release 1 build | 15 Sep – 24 Oct 2026 | 3 two-week sprints |
| Release 1 UAT | 27 Oct – 14 Nov 2026 | Committee volunteers test |
| **Release 1 go-live** | **24 Nov 2026** | Ready before 2027 registrations open on **1 Dec** |
| Release 2 build | 30 Nov 2026 – 12 Feb 2027 | 5 sprints (2-week Christmas break) |
| Release 2 UAT + app store review | 15 Feb – 12 Mar 2027 | Pilot with 2 teams |
| **Release 2 go-live** | **23 Mar 2027** | Ready before round 1 (10 Apr 2027) |

## 8. Governance
| Role | Club | Agency |
|------|------|--------|
| Sponsor | Karen, President | Head of Delivery |
| Product Owner | Raj, Treasurer (for club needs) | Elena, Platform Product Manager (for the product roadmap) |
| Delivery | — | Sam, Delivery Manager |
| Requirements | — | **You, Business Analyst** |
| Architecture | — | Arjun, Solution Architect |
| Design | — | Chloe, UX/UI Designer |
| Build | — | Nina (web lead), Tom (mobile lead), 2 developers |
| Quality | — | Ben, QA Lead |

**Cadence:** a fortnightly steering meeting, a sprint demo at the clubroom every two weeks, and a weekly BA/PO catch-up on Thursday evenings because the volunteers have day jobs.
