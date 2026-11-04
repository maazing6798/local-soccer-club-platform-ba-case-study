-- =============================================================
-- Local Junior Soccer Club: Registration & Fee Collection Analysis (SQLite)
-- Run:  sqlite3 ../data/club.db < registration_analysis.sql
-- =============================================================

-- Q1. Fee collection by season: paid by round 1, unpaid at season end
SELECT season,
       COUNT(*)                                                     AS players,
       SUM(fee_due_aud)                                             AS fees_due_aud,
       ROUND(100.0 * SUM(CASE WHEN paid_by_round1 = 1 THEN fee_due_aud ELSE 0 END) / SUM(fee_due_aud), 1) AS pct_fees_paid_by_round1,
       SUM(CASE WHEN unpaid_at_season_end = 1 THEN fee_due_aud ELSE 0 END) AS unpaid_at_season_end_aud,
       ROUND(100.0 * AVG(unpaid_at_season_end), 1)                  AS pct_players_never_paid
FROM registrations
GROUP BY season
ORDER BY season;

-- Q2. Registration timing: how many players registered after the grading deadline?
SELECT season,
       COUNT(*) AS players,
       ROUND(100.0 * AVG(before_grading_deadline), 1) AS pct_before_grading,
       ROUND(100.0 * AVG(early_bird), 1)              AS pct_early_bird
FROM registrations
GROUP BY season
ORDER BY season;

-- Q3. Payment method mix and bank transfers needing manual matching (2026)
SELECT payment_method,
       COUNT(*) AS players,
       ROUND(100.0 * COUNT(*) / SUM(COUNT(*)) OVER (), 1) AS pct_players,
       SUM(missing_bank_reference)                        AS missing_reference,
       ROUND(AVG(days_to_pay), 1)                         AS avg_days_to_pay
FROM registrations
WHERE season = 2026
GROUP BY payment_method
ORDER BY players DESC;

-- Q4. Families with more than one child pay later (manual sibling discount), 2026
SELECT CASE WHEN siblings_registered >= 2 THEN '2+ children' ELSE '1 child' END AS family,
       COUNT(*)                                  AS players,
       ROUND(AVG(days_to_pay), 1)                AS avg_days_to_pay,
       ROUND(100.0 * AVG(paid_by_round1), 1)     AS pct_paid_by_round1,
       ROUND(100.0 * AVG(unpaid_at_season_end), 1) AS pct_never_paid
FROM registrations
WHERE season = 2026
GROUP BY family;

-- Q5. Do players with unpaid fees come back? (2024 and 2025, excluding U14s, who age out)
SELECT CASE unpaid_at_season_end WHEN 1 THEN 'fees unpaid' ELSE 'fees paid' END AS fee_status,
       COUNT(*) AS players,
       ROUND(100.0 * AVG(returned_next_season), 1) AS pct_returned_next_season
FROM registrations
WHERE season IN (2024, 2025) AND age_group <> 'U14'
GROUP BY unpaid_at_season_end;

-- Q6. Players and families per season
SELECT season,
       COUNT(*)                  AS players,
       COUNT(DISTINCT family_id) AS families,
       SUM(CASE WHEN siblings_registered >= 2 THEN 1 ELSE 0 END) AS players_with_siblings
FROM registrations
GROUP BY season
ORDER BY season;

-- Q7. Outstanding fees at round 1, 2026: what the treasurer has to chase
SELECT COUNT(*)                     AS players_unpaid_at_round1,
       COUNT(DISTINCT family_id)    AS families_to_chase,
       SUM(fee_due_aud)             AS outstanding_at_round1_aud
FROM registrations
WHERE season = 2026 AND paid_by_round1 = 0;
