# Stakeholder Analysis & Engagement Plan

As the agency's BA I sit between two groups:
- the **club**, which owns the problem and makes the decisions about its own needs
- **my own company**, which designs, builds and tests the solution, and wants what we build to work for other clubs too

A big part of the job is translating between them. Volunteers describe problems in football terms, developers need testable requirements, and the agency's Product Manager needs to know which requests are specific to this club and which are needs every club will have.

## 1. Stakeholder register
### Club (client)
| Stakeholder | Role | Interest | Influence | What they care about | Engagement |
|-------------|------|:-:|:-:|----------------------|------------|
| Karen | President (Sponsor) | High | High | Volunteer burnout, keeping families happy | Manage closely: steering meeting, short written updates |
| Raj | Treasurer (club Product Owner) | High | High | Getting fees in without chasing friends | Manage closely: weekly catch-up, backlog decisions |
| Linda | Secretary & Registrar | High | Medium | ~40 hours of registration admin every summer | Co-design: workshops, lead UAT tester |
| Priya | Child Safety Officer | High | High (veto on child-safety matters) | WWCC compliance, safe communication with children | Keep satisfied: signs off child-safety requirements |
| Marco | Coach Coordinator | High | Medium | Late registrations break team allocation | Co-design: team allocation workshop |
| Coaches & team managers (12) | Volunteers, mostly parents | High | Medium | Less time chasing availability | Consult: focus group, app pilot |
| Parents & guardians (51 families) | Register children, pay fees | High | Low individually | One place for everything, fewer messages | Consult: survey (n = 38), 5 interviews |
| Players (65, aged 4–13) | Members | Medium | Low | Knowing when and where they play | Consult: short session with 6 older players, with parents present |

### Agency (my company)
| Stakeholder | Role | Interest | Influence | What they need from me |
|-------------|------|:-:|:-:|------------------------|
| Elena | Platform Product Manager | High | High | To know which needs are common to all clubs and which are specific to this one; a configurable product, not a one-off |
| Head of Delivery | Agency sponsor | Medium | High | A pilot that runs to time and budget |
| Sam | Delivery Manager | High | High | A ready backlog, a clear MVP, impact analysis for every change |
| Arjun | Solution Architect | High | High | Integration and data requirements, NFRs, constraints raised early |
| Chloe | UX/UI Designer | High | Medium | Personas, journeys, access to real parents and coaches |
| Nina / Tom | Web / mobile leads | High | Medium | Stories with clear acceptance criteria, quick answers on edge cases |
| Ben | QA Lead | High | Medium | Testable criteria, traceability, UAT test data |

### External
| Stakeholder | Relevance |
|-------------|-----------|
| State federation | Players must be registered through its portal. We depend on its daily data export |
| Local Council | Grants the club funding and allocates grounds |
| Payment provider | Card and wallet payments, payout reports |

## 2. Power / interest grid
```
                Lower interest                     Higher interest
           ┌───────────────────────────────┬──────────────────────────────────┐
 Higher    │ KEEP SATISFIED                │ MANAGE CLOSELY                   │
 influence │ Agency Head of Delivery       │ President · Treasurer (PO)       │
           │ Federation · Council          │ Child Safety Officer             │
           │                               │ Platform PM · Delivery · Architect│
           ├───────────────────────────────┼──────────────────────────────────┤
 Lower     │ MONITOR                       │ KEEP INFORMED / CO-DESIGN        │
 influence │ Sponsors                      │ Registrar · Coach Coordinator    │
           │                               │ Coaches · Parents · Players      │
           │                               │ UX · Dev leads · QA              │
           └───────────────────────────────┴──────────────────────────────────┘
```

## 3. RACI
| Activity | Club President | Treasurer (club PO) | Child Safety Officer | BA | Platform PM | Delivery Mgr | Architect | UX | Dev | QA |
|----------|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Approve pilot agreement and scope | **A** | C | C | R | C | R | I | I | I | I |
| Elicit and document requirements | I | C | C | **A/R** | C | I | C | C | C | C |
| Prioritise club backlog | C | **A** | C | R | C | C | C | I | I | I |
| Decide club-specific vs platform feature | I | C | I | R | **A** | C | C | C | I | I |
| Child-safety requirements sign-off | I | C | **A** | R | C | I | C | C | I | I |
| Solution and integration design | I | I | I | C | C | I | **A/R** | C | C | I |
| UX design and prototype testing | I | C | C | C | C | I | I | **A/R** | I | I |
| Build | I | I | I | C | I | A | C | C | **R** | I |
| System test | I | I | I | C | I | A | I | I | C | **R** |
| UAT planning and coordination | I | A | C | **R** | I | C | I | I | I | C |
| Change requests: impact analysis | I | A | I | **R** | C | R | C | C | C | I |
| Go / no-go | **A** | R | C | C | C | R | C | I | I | C |

## 4. Communication plan
| Audience | What | Channel | When | Owner |
|----------|------|---------|------|-------|
| Steering group | Progress, risks, decisions needed | 30-minute call + one-page update | Fortnightly | Delivery Manager + BA |
| Club PO | Backlog questions, acceptance | Call + shared backlog | Weekly, Thu 7pm | BA |
| Platform PM | Club-specific vs common features, roadmap | 1:1 | Weekly | BA |
| Committee and coaches | Sprint demo, feedback | In person at the clubroom | End of each sprint | BA + UX |
| Dev team | Refinement, story walkthroughs | Office / video | Weekly + daily stand-up | BA |
| Parents | What's changing and when | Email, coach briefings, flyer at training | Launch −4 weeks, −1 week, go-live | Club secretary (BA drafts) |

## 5. Elicitation activities
| Technique | Who | Output |
|-----------|-----|--------|
| Kick-off and goal-setting workshop | Committee (5) | Objectives O1–O6 |
| Interviews (8) | President, treasurer, registrar, child safety officer, coach coordinator, 3 coaches | Pain points, rules, exceptions |
| Time diary (3 weeks) | Registrar, treasurer, 4 coaches | Volunteer-hours baseline |
| Parent survey (n = 38 of 51 families) | All families, by email | Channel preferences, pain ranking |
| Document analysis | Fee schedule, child-safe policy, 2024–26 registration and payment records | Business rules, data analysis |
| Observation | Registration day at the clubroom; a Saturday match morning | As-is process maps |
| Communication-rules workshop | Child safety officer, coaches, two parents | Messaging rules BRL-05 to BRL-08 |
| Prototype testing (2 rounds) | 5 parents, 3 coaches, registrar | Validated journeys before build |

## 6. Conflicts I managed
**1. Coaches wanted group chat with the kids; the child safety officer said no.**
Some coaches wanted older players (U12–U14) in a team chat. The child safety officer pointed out that the club's child-safe policy does not allow adults to message children directly. I ran a joint session and we agreed:
- All team messages go to parents and guardians only.
- Players get a view-only profile, controlled by a parent, showing fixtures, their team and training times, with no messaging.
- No player's contact details are visible to anyone except the committee.

These rules became BRL-05 to BRL-08. Dropping chat also removed the developers' biggest technical risk.

**2. Club-specific vs platform features.**
The club wanted a sibling discount rule of "10% off the second child, 15% off the third". Elena (Platform PM) didn't want rules for one club hard-coded into the product. I turned the request into a configurable discount rule that any club can set up (FR-05). The club got exactly what it asked for, and the product got a feature it can sell to other clubs. I used the same approach for fee categories, age groups and volunteer duty types.

**3. The federation sync was slower than expected.**
In sprint 1 the architect found the federation offers only a nightly data export, not a live connection. I analysed the impact, which was that a child's federation status could lag by up to 24 hours. I rewrote FR-03 to accept the overnight sync, with a "federation check pending" label for parents. The club PO accepted this without a change request.
