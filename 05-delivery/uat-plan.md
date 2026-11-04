# UAT Plan: Release 1 (Registration)

## 1. Objective
Confirm that Release 1 meets the baselined requirements and that the committee can run 2027 registrations on it from 1 December 2026.

## 2. Testers and setup
| Item | Detail |
|------|--------|
| Testers | Treasurer, registrar, child safety officer, coach coordinator, 4 parents (including one with 3 children and one using a screen reader) |
| Sessions | 3 evening sessions at the clubroom + 1 week of testing at home |
| Environment | UAT site and TestFlight / Play test build; payment provider in sandbox mode |
| Test data | 2026 families migrated and anonymised; test cards (valid, declined, expired); a fake federation export with 5 deliberate mismatches |
| Defects | Logged by the BA in the agency's tracker; testers report by voice note or screenshot if they prefer |

## 3. Entry criteria
- All R1 stories passed system test
- No open Severity 1 or 2 defects from system test
- Testers have accounts and a 1-page test guide

## 4. Exit criteria
- 100% of Must test cases run; ≥ 95% pass
- No open Severity 1 defects; any Severity 2 has a fix date before go-live
- Sign-off from the treasurer (club PO) and the child safety officer (compliance cases)

## 5. Severity
| Severity | Definition | Example |
|----------|------------|---------|
| 1 | Stops registration or payment, or breaks a child-safety rule | Unverified coach can be assigned to a team |
| 2 | Wrong amount or wrong status; no workaround | Discount calculated incorrectly |
| 3 | Works, but awkward or confusing | Unclear error message |
| 4 | Cosmetic | Misaligned button |

## 6. Progress (as at 4 Nov 2026)
| Measure | Result |
|---------|--------|
| Test cases | 19 in R1: 17 run (14 passed, 2 failed, 1 blocked), 2 not yet run |
| Average time for a returning parent to register 2 children | 3 min 40 s (target < 5 min) ✅ |
| Open defects | 1 × Sev 2, 2 × Sev 3 (1 awaiting retest) |

## 7. Open defects
| ID | Test | Sev | Description | Owner | Status |
|----|------|:-:|-------------|-------|--------|
| DEF-012 | TC-05 | 2 | For a family of 3, the 15% sibling discount is applied to the most expensive fee instead of the cheapest (BRL-03) | Web lead | Fix in sprint 3 hotfix, retest 8 Nov |
| DEF-014 | TC-14 | 3 | WWCC expiry alert email goes to the coach but not the child safety officer | Web lead | Fix agreed |
| DEF-015 | TC-09 | 3 | Hardship confirmation screen uses the word "hardship"; the club prefers "fee support" | BA (copy change) | Done, awaiting retest |

Test cases: [`uat-test-cases.csv`](uat-test-cases.csv)
