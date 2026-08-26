# Beginner's Guide modernization recommendations

Offline analysis only. Do **not** paste Atlantis wiki prose into the Hugo guide without permission; prefer paraphrase + link-outs with attribution.

| Corpus | Location |
|--------|----------|
| Current guide | `content/beginners-guide/` |
| Atlantis wiki mirror | `scripts/uwh-guide-migration/atlantis-wiki/` ([INDEX.md](atlantis-wiki/INDEX.md)) |
| Local Sea Lions extras | `/Users/matt/Projects/uwh-beginners-guide` → extracts in [local-docs-extract/CATALOG.md](local-docs-extract/CATALOG.md) |

Wiki scrape: **255** published pages via GraphQL list + HTML fetch (`scrape_atlantis_wiki.py`). Text lives under `atlantis-wiki/text/`.

Priorities: **P0** correctness/safety/rules · **P1** structural gaps beginners hit · **P2** nice-to-have / coach track.

---

## Crosswalk (guide ↔ wiki ↔ local)

| Guide chapter | Strongest wiki hubs | Local extras |
|---------------|---------------------|--------------|
| 00 What is it | `/getting-started/new-player`, `/home`, `/Safety` | — |
| 01 Rules | `/game`, `/game/fouls/*`, `/game/protocols/*` | `UWH Foul 1.docx`, `UWH Foul 2.docx` |
| 02 Equipment | `/game/gear-setup/*` (sticks, gloves, caps, mouth-guards, pucks, goals, courts) | — |
| 03 Skills | `/players/individual_fundamentals/*`, `/players/evasive_maneuvers/*`, `/players/tackling_maneuvers/*`, `/players/individual_drills/*`, `/getting-started/new-player/first-hockey-skills` | Tourist skills HTML; `Drill File 2017v3.pptx` |
| 04 Positions | `/teams/formations/3-3`, role pages under 2-2-2/MuffinTop; teamwork | `Position Complete 2016-07-29*.docx`, `Pivot.docx`, `Swing.docx` |
| 05 Formations | `/teams/formations` + `1-3-2`, `2-2-2`, `2-3-1`, `2-1-2-1`, `3-2-1`, `3-3` | `Style of Play version 01.pdf`, Playbook drafts |
| 06 Zones | (partial: formation/teamwork pages; no dedicated “zones” hub) | Style of Play / playbook spacing language |
| 07–08 Positioning (3-3) | `/teams/formations/3-3`, `/teams/teamwork/*`, `/game/protocols/advantage_puck`, `/game/protocols/penalty_shot` | Playbook, Advantage pucks pptx, Position Complete |
| 09 Scoring | `/teams/teamwork/attacking_the_goal`, `/game/fouls/no-goal-calls` | — |
| 10 Subbing | `/game/protocols/substitutions`, `/game/fouls/illegal_sub` | — |
| 11 Cycling / breakaways | `/teams/teamwork/swings`, `/players/tackling_maneuvers/chasing_breakaways` | Playbook “Flow” slides |
| 12–13 2-on-1 / 2-on-2 | `/teams/teamwork/pinches`, coordinating tackles | `Drill File 2017v3.pptx` |
| 14 Set play | `/game/protocols/*` (equal/advantage/disadvantage) | Advantage pucks pptx |
| 15 Tournament checklist | `/club-organization/hosting-tournaments/*` (partial overlap) | — |
| *(gap)* | `/Coaching` Levels 1–4 + Badges; `/fitness-and-training/*`; `/pool-managers`; `/getting-started/starting-a-team/*`; `/Referees/*` | Workout plans, children’s syllabus, annual plan |

---

## Additions

### P0 — New “Fouls” chapter (or major Rules expansion)

- **Why:** Guide rules are a short informal list. Wiki has a full foul taxonomy with when/how to call and examples (illegal advancement, illegal stopping, stick infringement, free-arm, obstruction barging/blocking/screening, false start, illegal sub, barrier, out of bounds, delay of game, unsportsmanlike, no-goal, advantage rule).
- **Sources:** wiki `/game/fouls` + children; local `UWH Foul 1.docx` / `UWH Foul 2.docx` (older illustrations).
- **Action:** Add beginner-facing foul primers (what it looks like in the water + what happens next). Link CMAS Vol 2 for official wording. Do not copy wiki text verbatim.

### P0 — New “Protocols / Restarts” section

- **Why:** Advantage puck, equal puck, disadvantage, penalty shot, timeouts, warnings, time penalties are barely explained as *rules of restart*; scenario chapter assumes them.
- **Sources:** wiki `/game/protocols/*` (esp. `advantage_puck`, `equal_puck`, `disadvantage_puck`, `penalty_shot`, `substitutions`); local `Advantage pucks 2017.pptx` for *set-play ideas* (club/advanced—see demotions).
- **Action:** Short chapter or Rules subsection: what the ref signals, where teams set up, 5-second touch rule, 3 m exclusion on advantage.

### P0 — Safety / equalisation blurb

- **Why:** Guide never covers ear equalisation or “don’t force it.”
- **Sources:** wiki `/Safety`; getting-started beginner mistakes.
- **Action:** Half-page under What is it / Getting started—or a tiny Safety page linked from the index.

### P1 — Getting-started on-ramp

- **Why:** `00-what-is-it.md` is ~60 words. Wiki has first session, water skills, movement fundamentals, first hockey skills, beginner mistakes.
- **Sources:** `/getting-started/new-player/*`.
- **Action:** Expand chapter 00 (or add “Your first practice”) with: what to bring, comfort prerequisites, beginner mistakes list, “control first / speed later.”

### P1 — Multi-formation overview (beyond “we only teach 3-3”)

- **Why:** Formations chapter correctly focuses beginners on 3-3 but only names 2-3-1 in passing. Wiki documents 1-3-2, 2-2-2, 2-3-1, 2-1-2-1, 3-2-1, 3-3 with play-style summaries.
- **Sources:** `/teams/formations` + per-formation pages; local Style of Play / Playbook (3-3 centric but mentions morphs).
- **Action:** Keep deep dive on 3-3; add a comparison table (shape, strengths, who it suits). Optional later chapters for 2-3-1 / 2-2-2 as “next after beginner.”

### P1 — Evasive + tackling skill taxonomies

- **Why:** Skills chapter has curling / shooting / body position but not a structured catalog. Wiki splits **evasive** (standard/reverse/inverted curl, deep-V, figure-6, deke, fade, around-the-world, upper-cut) vs **tackling** (tackles both sides, back-picks, wall wedge, chasing breakaways, redirects).
- **Sources:** `/players/evasive_maneuvers/*`, `/players/tackling_maneuvers/*`.
- **Action:** Add sections or subpages: name + when to use + link to existing curling prose. Align naming (“figure-6” / deep-V vs guide’s “6” / Ethiopian / halfmoon).

### P1 — Caps, mouth-guards, court/puck/goal basics

- **Why:** Equipment covers mask/snorkel/glove/fins/sticks; wiki also treats caps, ear-guards, mouth-guards, pucks, goals, walls, courts as first-class.
- **Sources:** `/game/gear-setup/*`.
- **Action:** Add short subsections (esp. caps + mouth-guards for tournament readiness; puck weight/colour; goal trough).

### P1 — Teamwork primitives: pinches, swings, goal attack/defense

- **Why:** 2-on-1/2-on-2 chapters exist; wiki’s “pinch” / “swing” language matches playbook “flow” and fills gaps between individual skills and 3-3 scenarios.
- **Sources:** `/teams/teamwork/pinches`, `swings`, `attacking_the_goal`, `defending_the_goal`, `coordinating_tackles`; local Playbook Flow slides; Pivot/Swing role docs.
- **Action:** Either new “Teamwork basics” chapter or fold pinch/swing definitions into 11–13.

### P2 — Drill appendix / link-outs

- **Sources:** wiki `/players/individual_drills/*`, `/teams/teamwork_drills/*`; local `Drill File 2017v3.pptx`.
- **Action:** Optional “Practice drills” page with 5–10 beginner drills; point coaches to Atlantis drill libraries + local drill file.

### P2 — Explicit CMAS links

- **Sources:** wiki `/game` already links CMAS Vol 1 (playing area) and Vol 2 (rules of play).
- **Action:** Put those links on Rules and Equipment (court) pages.

---

## Updates

| Priority | Chapter | Update | Cite |
|----------|---------|--------|------|
| P0 | 01 Rules | Reconcile “non-contact” summary with modern foul names (obstruction types, free-arm, illegal advancement/stopping). Keep beginner voice; add “see Fouls chapter.” | `/game/fouls/*`, local foul docs |
| P0 | 08 Advantage / penalty scenarios | Tie diagrams to protocol definitions (3 m, 5 s touch, who may set where). | `/game/protocols/advantage_puck`, `penalty_shot` |
| P1 | 02 Equipment | Refresh stick/glove/fin guidance against wiki gear pages; add caps/mouth-guard; note dual-lens / divider / monolithic mask language. | `/game/gear-setup/masks`, `fins`, `sticks`, `gloves`, `caps` |
| P1 | 03 Skills | Map “three levels of puck handling” to wiki grips + rolls + passes (tic-tac, front-to-back roll, flicks/sliders/rollers). Add moving-in-water / cobra / strike sequence pointers. | `/players/individual_fundamentals/**` |
| P1 | 03 Skills (curling / feints) | Align maneuver names with wiki evasive set; keep unique Sea Lions nicknames as aliases. | `/players/evasive_maneuvers/**` |
| P1 | 04 Positions | Cross-link Pivot/Swing naming (Canada) already mentioned in formations; enrich Center/Swing Back duties from Position Complete + wiki 3-3. | Position Complete, Pivot/Swing docs, `/teams/formations/3-3` |
| P1 | 05 Formations | Fix/clarify naming: guide’s X-Y-Z (F-M-B) vs wiki’s “offensive then defensive” convention—state both so readers aren’t confused. Expand beyond one paragraph on 2-3-1. | `/teams/formations` |
| P1 | 07–08 3-3 positioning | Refresh with wiki 3-3 overview (wall pressure, cycling, side switch). Replace `[MISSING DIAGRAM: GOOD POSITIONING]` (likely `GoodPassing2.gif` already in static—verify). | `/teams/formations/3-3`, GoodPassing2.gif |
| P1 | 09 Scoring | Expand thin page using attacking_the_goal + no-goal-calls; keep existing scoring diagrams. | `/teams/teamwork/attacking_the_goal`, `/game/fouls/no-goal-calls` |
| P1 | 10 Subbing | Align with `/game/protocols/substitutions` and illegal_sub foul. | wiki protocols/fouls |
| P1 | 11 Cycling | Connect “cycling” language to wiki **swings** + playbook **flow**. | `/teams/teamwork/swings`, Playbook v4 |
| P2 | 12–13 | Add “pinch” terminology alongside DSZ language; cite drill file for practice progressions. | pinches, Drill File |
| P2 | 15 Checklist | Optional: link hosting-tournaments wiki for organizers (not player packing list). | `/club-organization/hosting-tournaments` |
| P2 | `_index.md` | Add “Further reading” to Atlantis wiki + CMAS; note guide origin (mid-2000s Sea Lions) vs modern wiki. | `/home` |

---

## Deletions / demotions

| Item | Action | Why |
|------|--------|-----|
| USA Men’s set-play sequences in `Advantage pucks 2017.pptx` / Playbook Flow as *beginner required reading* | **Demote** to “Advanced / club playbook” (future section or external) | Too system-specific; beginners need protocol rules first, not national-team scripts |
| Full Playbook / Style of Play / Position Complete as drop-in chapters | **Do not** merge wholesale into beginner guide | Coach/advanced; overlaps 3-3 chapters; different audience |
| Duplicate `*-comments.html` exports | **Ignore / delete from consideration** | Editor debris |
| Children’s syllabus, annual plan, training pyramid, beep test, swim workout library | **Out of beginner guide** (fitness/coach tracks) | See below |
| Guide claim that document “focuses solely on 3-3” without naming other formations | **Soften** (update, not delete chapter) | Still true as focus; wiki shows beginners benefit from knowing other shapes exist |
| Broken fake images still referenced (`backpick*.png`, `uwh-1-1-*.PNG`) | **Not a content deletion**—restore via Wayback process in [README.md](README.md) | Asset pipeline, not prose |

---

## Out of scope for the beginner guide

Recommend **link out** or a later site section—not chapters inside `beginners-guide/`:

| Topic | Where it lives | Suggestion |
|-------|----------------|------------|
| Coaching Levels 1–4, lesson plans, drill libraries, badges | wiki `/Coaching/**`, `/Coaching/Badges/**` | “For coaches” link on index |
| Fitness / water workouts / cross-training | wiki `/fitness-and-training/**`; local swim plans, beep test, workouts xls | Separate “Training” section later |
| Pool managers / facility FAQ | wiki `/pool-managers` | Link from What is it / club pages |
| Starting a team, recruitment, funding | wiki `/getting-started/starting-a-team/**`, `/club-organization/recruitment/**` | Club-ops section |
| Hosting tournaments | wiki `/club-organization/hosting-tournaments/**` | Organizer docs |
| Referee positioning / special rules | wiki `/Referees/**` | Ref track |
| National playbook systems (Flow, MuffinTop 2-2-2 deep dive) | local Playbook/Style; wiki `2-2-2/MuffinTop/**` | Advanced tactics |

---

## Suggested implementation order

1. **P0:** Safety blurb · Protocols/restarts · Fouls chapter · Rules refresh  
2. **P1:** Expand Getting started · Equipment gaps · Skills taxonomy alignment · Formations comparison table · 3-3/scoring/subbing touch-ups  
3. **P2:** Teamwork pinch/swing chapter · Drills appendix · Index further-reading · Coach/fitness link-outs  
4. Parallel: finish Wayback image restores (backpick, 2-1, 2-2) per migration README—not blocked by this doc  

---

## Attribution reminder

- Atlantis Sports wiki: https://wiki.atlantissports.org/ (mirror for analysis; contentLicense empty in siteConfig—treat as third-party; ask before republishing).
- Sea Lions / USA Men’s local docs: club-internal; use for ideas and historical continuity, not as public verbatim playbooks unless you own distribution rights.
- Official rules: CMAS Vol 1 / Vol 2 (linked from wiki `/game`).
