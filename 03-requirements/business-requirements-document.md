# Business Requirements Document (BRD)
**Project:** Club platform for a local junior soccer club | **Version:** 1.3 | **Status:** Baselined 12 Sep 2026

## 1. Business requirements
| ID | Business requirement | Objective | Priority |
|----|----------------------|-----------|----------|
| BR-01 | Families must be able to register and pay club fees in one step, online | O1, O3 | Must |
| BR-02 | The committee must be able to see which players are paid and registered with the federation, without manual cross-checking | O1, O3 | Must |
| BR-03 | Teams must be allocated from complete registration data by the grading deadline | O2 | Must |
| BR-04 | No adult may be assigned to a team without a verified, current WWCC | O4 | Must |
| BR-05 | Coaches must be able to communicate with families and confirm availability safely and quickly | O3, O5 | Must |
| BR-06 | Families must be able to sign up for and swap volunteer duties | O3 | Should |
| BR-07 | The club must have a public website the committee can keep up to date | O5, O6 | Must |

## 2. Functional requirements
### Registration & payments (Release 1)
| ID | Requirement | BR | MoSCoW |
|----|-------------|----|--------|
| FR-01 | A parent shall be able to create a family account and add one or more children | BR-01 | Must |
| FR-02 | Returning families shall see last season's details pre-filled for confirmation | BR-01 | Must |
| FR-03 | The system shall import the federation registration export nightly and show each player's federation status (registered / pending) | BR-02 | Must |
| FR-04 | The system shall calculate the fee per child from configurable fee categories (by age group) | BR-01 | Must |
| FR-05 | The system shall apply configurable discount rules (early-bird by date; sibling discount by child count) and show the breakdown before payment | BR-01 | Must |
| FR-06 | Parents shall be able to pay by card, Apple Pay or Google Pay | BR-01 | Must |
| FR-07 | Parents shall be able to choose 2 instalments; the second is charged automatically on a set date | BR-01 | Should |
| FR-08 | Parents shall be able to submit a confidential hardship request instead of paying; only the treasurer can see it | BR-01 | Must |
| FR-09 | Registration shall close at the grading deadline; after it, families join a waitlist that the coach coordinator approves | BR-03 | Must |
| FR-10 | The coach coordinator shall be able to allocate players to teams by dragging and dropping, with team size limits per age group | BR-03 | Must |

### Compliance (Release 1)
| ID | Requirement | BR | MoSCoW |
|----|-------------|----|--------|
| FR-11 | Coaches and team managers shall enter their WWCC number and expiry date in their profile | BR-04 | Must |
| FR-12 | The child safety officer shall mark each WWCC as verified after checking it with the issuing authority | BR-04 | Must |
| FR-13 | The system shall block assigning an adult to a team if their WWCC is missing, unverified or expired, and shall alert the child safety officer 30 days before expiry | BR-04 | Must |

### Communication & availability (Release 2)
| ID | Requirement | BR | MoSCoW |
|----|-------------|----|--------|
| FR-14 | Coaches, team managers and the committee shall be able to send team announcements to parents and guardians | BR-05 | Must |
| FR-15 | The system shall not allow any direct or group message to be sent to a player profile | BR-05 | Must |
| FR-16 | The system shall send game reminders by push notification at 6pm the day before and 7am on game day | BR-05 | Must |
| FR-17 | The committee shall be able to send club-wide announcements to all families | BR-05 | Must |
| FR-18 | Each Monday the system shall ask parents for each child's availability for the next game | BR-05 | Must |
| FR-19 | Coaches shall see a live availability count and be able to remind parents who haven't replied in one tap | BR-05 | Must |
| FR-25 | Coaches shall be able to mark training attendance from the team list | BR-05 | Should |
| FR-26 | A parent shall be able to create a view-only player profile for their child and switch it off at any time | BR-05 | Should |

### Volunteer roster (Release 2)
| ID | Requirement | BR | MoSCoW |
|----|-------------|----|--------|
| FR-20 | The volunteer coordinator shall be able to create duty slots for each game day | BR-06 | Should |
| FR-21 | Parents shall be able to claim a slot, swap with another parent and get a reminder the day before | BR-06 | Should |

### Website & admin (Release 1)
| ID | Requirement | BR | MoSCoW |
|----|-------------|----|--------|
| FR-22 | Committee members shall be able to edit website pages and post news without technical skills | BR-07 | Must |
| FR-23 | The website shall show upcoming fixtures and results from the platform automatically | BR-07 | Must |
| FR-24 | The website shall have a "Join the club" page linking to registration | BR-07 | Must |
| FR-27 | The treasurer shall be able to export payments and payouts as CSV for the accounts | BR-02 | Must |
| FR-28 | The admin dashboard shall show registrations, fees paid and outstanding, federation status and compliance at a glance | BR-02 | Must |

## 3. Non-functional requirements
| ID | Category | Requirement | MoSCoW |
|----|----------|-------------|--------|
| NFR-01 | Child safety | The platform shall enforce the club's child-safe policy: no messaging to children, no child contact details visible outside the committee, no player photos in Release 1–2 | Must |
| NFR-02 | Privacy | Personal information shall be collected and handled in line with the Australian Privacy Principles; a collection notice shall appear at registration | Must |
| NFR-03 | Security | Card data shall be handled by the payment provider only (PCI-DSS SAQ-A). The platform stores tokens, not card numbers | Must |
| NFR-04 | Security | Committee accounts shall use two-factor authentication | Must |
| NFR-05 | Accessibility | Website and app shall meet WCAG 2.2 AA | Must |
| NFR-06 | Usability | A returning parent shall be able to register and pay for two children in under 5 minutes (tested with 5 parents) | Must |
| NFR-07 | Availability | 99.5% monthly; ≥ 99.9% during 1–14 Dec registration peak | Must |
| NFR-08 | Configurability | Fee categories, discount rules, age groups and duty types shall be configurable per club without code changes | Must |
| NFR-09 | Devices | iOS 16+, Android 11+, last 2 versions of major browsers | Must |

## 4. Business rules
| ID | Rule |
|----|------|
| BRL-01 | Fees: U5–U8 A$160; U9–U14 A$220 (2026 schedule; increases by A$15 in 2027) |
| BRL-02 | Early-bird discount: A$30 off per child if paid by 31 January |
| BRL-03 | Sibling discount: 10% off the second child and 15% off the third and later children, applied to the cheaper fees first and **before** the early-bird discount |
| BRL-04 | A player is "ready for team allocation" only when paid (or hardship approved) **and** registered with the federation |
| BRL-05 | No adult may send a message to a player profile, individually or in a group |
| BRL-06 | Team announcements go only to the parents and guardians of players in that team |
| BRL-07 | Team lists visible to parents and players show first names only |
| BRL-08 | Only the committee and the team's coach and team manager can see guardian contact details |
| BRL-09 | Hardship requests are visible to the treasurer only; the registrar sees "approved" or "pending" without details |

## 5. Assumptions, constraints, dependencies, risks
| Type | Description | Owner / mitigation |
|------|-------------|--------------------|
| Constraint | Registrations open 1 Dec 2026; Release 1 must be live by 24 Nov | Delivery Manager: fixed scope for R1 |
| Constraint | Volunteers can only meet on weeknights and weekends | BA: Thursday evening sessions, recorded demos |
| Dependency | Federation provides a nightly CSV export | Architect: confirmed in sprint 1; FR-03 adjusted |
| Dependency | Apple and Google app store approval (up to 2 weeks) | Mobile lead: submit by 2 Mar 2027 |
| Assumption | 90% of families have a smartphone | Survey: 37 of 38 do; the website covers the rest |
| Risk | Parents keep using WhatsApp alongside the app | Change plan: coaches close old groups at launch, with the club's backing |
| Risk | Club-specific requests bloat the platform | Platform PM decides; BA turns requests into configurable features |

## 6. Release plan
| Release | Scope | Date |
|---------|-------|------|
| R1 "Registration" | Website, registration & payments, federation sync, team allocation, WWCC compliance, admin dashboard (FR-01–FR-13, FR-22–FR-24, FR-27–FR-28) | 24 Nov 2026 |
| R2 "Match day" | Member app: announcements, reminders, availability, attendance, player view, volunteer roster (FR-14–FR-21, FR-25–FR-26) | 23 Mar 2027 |
| R3 backlog | Canteen pre-orders, merchandise, photos (after a child-safety review), player stats | Costed, not committed |

## 7. Sign-off
| Name | Role | Decision | Date |
|------|------|----------|------|
| Karen | Club President | Approved | 12 Sep 2026 |
| Raj | Treasurer, club PO | Approved | 12 Sep 2026 |
| Priya | Child Safety Officer | Approved BRL-05 to BRL-08 and NFR-01 | 12 Sep 2026 |
| Elena | Platform Product Manager (agency) | Approved, with NFR-08 as a condition | 11 Sep 2026 |
