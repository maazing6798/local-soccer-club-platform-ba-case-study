# Epics & User Stories
Stories follow INVEST and have acceptance criteria written in Gherkin. The QA lead turns the criteria into test cases, which is how the [traceability matrix](requirements-traceability-matrix.csv) links each requirement to a test.

**Definition of Ready (agreed with the dev team):** the story has a persona and value statement, acceptance criteria cover the happy path, at least one edge case and an error case, any designs are linked, dependencies are noted, and the story is estimated.

---

## Epic E1: Register & pay (Release 1)

### US-101 Register my children with last season's details · 5 pts · Must
**As a** returning parent
**I want** my family's details from last season filled in already
**so that** I can register both kids in a few minutes.

```gherkin
Scenario: Returning family
  Given I registered Mia (U8) and Sam (U12) last season
  When I start 2027 registration
  Then I see both children with last season's details pre-filled
  And their age groups are updated for 2027 (U9 and U13)
  And I only need to confirm or edit the details before paying
```
Traces to: FR-01, FR-02, NFR-06

### US-102 See the right price before I pay · 5 pts · Must
**As a** parent of two
**I want** the sibling and early-bird discounts worked out for me
**so that** I can pay straight away without emailing the treasurer.

```gherkin
Scenario Outline: Discounts applied
  Given today is <date>
  And I am registering a U9 child (A$235) and a U13 child (A$235)
  Then the total shown is <total>
  Examples:
    | date        | total    |
    | 20 Jan 2027 | A$386.50 |
    | 05 Feb 2027 | A$446.50 |
```
*Worked example: the 2027 fee for U9–U14 is A$235 (BRL-01). The sibling discount is applied first: the second child pays A$235 × 0.9 = A$211.50. The early bird then takes A$30 off each child. Before 31 Jan: A$205 + A$181.50 = **A$386.50**. After: A$235 + A$211.50 = **A$446.50**.*

*BA note: when I worked through this example in refinement, the developers and the treasurer each assumed a different order for the two discounts. The treasurer confirmed that the sibling discount comes first, and BRL-03 now says so explicitly.*

Traces to: FR-04, FR-05, BRL-02, BRL-03

### US-103 Pay by card, wallet or instalments · 5 pts · Must
```gherkin
Scenario: Apple Pay
  Given my total is A$386.50
  When I choose Apple Pay and confirm with Face ID
  Then both children show as "Paid"
  And I receive an email receipt

Scenario: Instalments
  When I choose "2 instalments"
  Then A$193.25 is charged today
  And A$193.25 is scheduled for 1 March 2027
  And I can see the scheduled payment in my payment history

Scenario: Card declined
  When my card is declined
  Then I see "Your card was declined. Try another card or payment method."
  And my registration details are kept
```
Traces to: FR-06, FR-07, NFR-03

### US-104 Ask for help with fees, privately · 3 pts · Must
**As a** parent who is struggling financially
**I want** to ask for fee support without anyone except the treasurer knowing
**so that** my child can still play.

```gherkin
Scenario: Hardship request
  When I choose "I need help with fees" and submit a short note
  Then my children's registration shows "Pending" without the word "hardship"
  And only the treasurer can see my note
  And the registrar sees only "Fee status: pending"
```
Traces to: FR-08, BRL-09

### US-105 Federation status without the cross-checking · 3 pts · Must
**As the** registrar
**I want** each child's federation status updated automatically every night
**so that** I only deal with the families who haven't finished.

```gherkin
Scenario: Pending federation registration
  Given a child is paid but not found in last night's federation export
  Then the parent sees "Federation check pending" and a link to finish registering
  And the child appears in my "Paid, federation check pending" list
```
Traces to: FR-03, BRL-04

---

## Epic E2: Teams & compliance (Release 1)

### US-201 Allocate teams by drag and drop · 5 pts · Must
```gherkin
Scenario: Team size limit
  Given the U9 team size limit is 10
  And U9 Blue already has 10 players
  When I drag another player onto U9 Blue
  Then I see "U9 Blue is full (10 of 10)"
  And the player stays unallocated
```
Traces to: FR-10, BRL-04

### US-202 Late registrations go to a waitlist · 2 pts · Must
```gherkin
Scenario: After the grading deadline
  Given today is after the 14 Feb grading deadline
  When a new family tries to register
  Then they can join the waitlist for their child's age group
  And the coach coordinator is notified to approve or decline
```
Traces to: FR-09

### US-203 Block coaches without a verified WWCC · 5 pts · Must
**As the** child safety officer
**I want** the system to stop anyone without a verified, current WWCC being assigned to a team
**so that** compliance doesn't depend on someone remembering to check.

```gherkin
Scenario: Unverified WWCC
  Given Dave's WWCC status is "Entered, not verified"
  When the coach coordinator tries to assign Dave to U10 Red
  Then the assignment is blocked
  And the message reads "Dave can't be assigned until their WWCC is verified by the child safety officer"

Scenario: Expiry warning
  Given Dave's verified WWCC expires in 30 days
  Then the child safety officer and Dave both receive an expiry alert
```
Traces to: FR-11, FR-12, FR-13, NFR-01

---

## Epic E3: Match day (Release 2)

### US-301 Tell the coach if my child can play · 3 pts · Must
```gherkin
Scenario: Availability for two children
  Given Mia and Sam both have games on Saturday
  When I open Monday's availability request
  Then I can mark each child ✅ or ❌ separately
  And their coaches see the counts update straight away
```
Traces to: FR-18, FR-19

### US-302 See who's in at a glance · 3 pts · Must
```gherkin
Scenario: Remind parents who haven't replied
  Given 8 players are in, 1 is out and 2 haven't replied
  When I tap "Remind parents"
  Then only the parents of the 2 players without a reply get a push notification
```
Traces to: FR-19

### US-303 Team announcements go to parents only · 3 pts · Must
**As a** coach
**I want** to send one announcement to my team's parents
**so that** everyone gets the change without a chat thread.

```gherkin
Scenario: Announcement recipients
  When I send "Game moved to Pitch 3" to U10 Red
  Then every parent and guardian of a U10 Red player receives it
  And no player profile receives it

Scenario: No messaging to players
  Given I am viewing Leo's player card
  Then there is no option to message Leo
```
Traces to: FR-14, FR-15, BRL-05, BRL-06

### US-304 Game reminders · 2 pts · Must
```gherkin
Scenario: Reminders
  Given Mia has a game at 9:30 on Saturday at Pitch 2
  Then I receive a push notification at 6pm Friday and 7am Saturday with the time and pitch
```
Traces to: FR-16

### US-305 My child's own view · 3 pts · Should
```gherkin
Scenario: Parent creates a player view
  Given I am Leo's parent
  When I turn on "Player view" for Leo
  Then Leo can sign in on our iPad and see his team, next game, training times and medals
  And Leo sees teammates' first names only
  And Leo cannot send or receive messages
```
Traces to: FR-26, BRL-05, BRL-07

### US-306 Pick and swap volunteer duties · 3 pts · Should
```gherkin
Scenario: Swap a duty
  Given I am down for canteen at 9am Saturday
  When I offer the slot for a swap and another parent accepts
  Then the roster updates
  And the volunteer coordinator sees the change
```
Traces to: FR-20, FR-21

---

## Backlog summary
| Epic | Stories | Points | Release |
|------|:-:|:-:|:-:|
| E1 Register & pay | 5 | 21 | R1 |
| E2 Teams & compliance | 3 | 12 | R1 |
| E3 Match day (incl. US-307 in the backlog) | 7 | 19 | R2 |
| Website & admin (see [backlog](product-backlog.csv)) | 4 | 13 | R1 |
| **Total** | **19** | **65** | |
