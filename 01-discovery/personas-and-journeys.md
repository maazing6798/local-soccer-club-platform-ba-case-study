# Personas & Journeys
These personas are based on 8 interviews, a survey of 38 families and a 3-week time diary. The UX designer and I used them to decide what each view of the app does first.

---

## Mei: parent of two
**Kids:** U8 and U12 · **Device:** iPhone · **With the club:** 3 seasons
> "Two kids, two coaches, two WhatsApp groups and a Facebook page. I missed a time change because it was buried under messages about a lost drink bottle."

- **Needs:** both children's games in one place, one payment with the sibling discount already applied, reminders she can't miss
- **Pain today:** waits for the treasurer to email the sibling discount before she can pay; families with 2+ children took **39 days** on average to pay, compared with 26 days for one-child families
- **App view:** a family home screen with each child's next game, an availability toggle for each child and her volunteer duties

## Dave: volunteer U10 coach
**Day job:** electrician · **Device:** Android · **Coaching:** 2 seasons
> "Every Thursday night I'm counting thumbs-up emojis to work out if I've got seven kids for Saturday."

- **Needs:** availability at a glance, one message to all parents, attendance marked in seconds
- **App view:** a team screen with availability counts (✅ 8 · ❌ 1 · ❔ 2), a "Remind parents who haven't replied" button and one-tap attendance

## Linda: secretary and registrar
**Age:** 58 · **Device:** laptop · **Role:** 6 years
> "December basically disappears. I download the federation list and tick names against the bank statement."

- **Needs:** registrations and payments in one list, with only the exceptions to deal with
- **Pain today:** about 40 hours each registration season; 13 of 49 bank transfers in 2026 had no usable reference
- **Admin view:** a registration list with filters for "Registered, not paid", "Paid, federation check pending" and "Needs a decision" (hardship requests)

## Raj: treasurer and club Product Owner
> "Twelve families still owed money at round 1. I know them all from the sideline. Chasing them is the worst part of the job."

- **Needs:** fees paid at the time of registration, automatic polite reminders so he doesn't have to chase people himself, a payout report for the accounts
- **Admin view:** a fees dashboard, an outstanding-fees list and a reconciliation export

## Priya: child safety officer
> "If a coach's Working With Children Check expires mid-season, I need to know before they turn up to training."

- **Needs:** a WWCC register with expiry alerts, no unverified adult attached to a team, messaging rules enforced by the system rather than by goodwill
- **Admin view:** a compliance view of every coach and team manager, each marked verified, expiring within 30 days, expired or missing

## Leo: player, 12 (U13)
**Device:** his mum's old iPad
> "I just want to know what time the game is and what number I am."

- **Needs:** his team, next game, training times, and the "player of the week" medal he got
- **Rules:** a parent creates and controls his profile; no messaging; he sees no other player's contact details (BRL-05 to BRL-08)
- **App view:** a simple "My team" screen with the next game, the team list (first names only) and his medals

---

## Journey map: Mei registers two children (as-is → to-be)
| Stage | As-is | Feeling | To-be |
|-------|-------|:-:|-------|
| Hears registration is open | Facebook post, word of mouth | 😐 | Email and push notification to last season's families on 1 Dec |
| Registers | Federation portal, once per child, re-entering family details | 😣 | Club app: last season's details pre-filled; pick both children; federation sync runs overnight |
| Works out the cost | Emails the treasurer and waits for the sibling discount | 😠 | Total shown straight away with the early-bird and sibling discounts applied |
| Pays | Bank transfer, often forgetting the reference | 😐 | Card or Apple/Google Pay, in full or in 2 instalments |
| Finds out the team | Coach adds her to a WhatsApp group in March | 😕 | App shows the team, coach and first training once teams are published |
| Game day | Scrolls the group chat for the time | 😣 | Saturday 7am push notification: "U8 Blue vs Eastfield, 9:30, Pitch 2" |

## Journey map: Dave's week (to-be)
```mermaid
journey
    title Dave, U10 coach: a week in the season (to-be)
    section Monday
      Availability request goes to parents automatically: 5: Dave
    section Wednesday
      Sees 8 in, 1 out, 2 not replied: 4: Dave
      Taps "Remind parents": 5: Dave
    section Thursday training
      Marks attendance in 20 seconds: 5: Dave
    section Saturday
      Team sheet ready; canteen duty filled: 5: Dave
```
