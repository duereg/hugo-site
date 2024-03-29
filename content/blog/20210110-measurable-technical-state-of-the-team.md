---
title: "Measure the Technical State of your Team"
date: 2021-01-10T21:40:42-08:00
draft: false
images: [{ alt: "Technical Evaluation", src: "/img/evaluation.jpg" }]
tags: ["Project Management", "Management"]
categories: ["management", "teaching", "learning", "growth", "development", "classes", "evaluation"]
---

Some thoughts on how you could evaluate the state of the systems your team owns.

One way to use this:
* Put some of these criteria on the Y axis
* Put the name of the components you own on the X.
* Give everything a score from 1 to 0.
* Either average the scores or sum them to figure out which components need the most love.

If all of these are the same for everything you own, it might make sense to skip that section. For example, if you own 10 services, but they all use a common build pipeline that you don't maintain, it might make sense to skip that criteria.

## Builds:

Consistent Build from Dev -> Prod
* The same image/code used in each step, not built at each step

Blocking tests at each phase
* Unit is a good start, acceptance is better

Canary and/or staged releases to production
* Having an "alpha" or "canary" production environment can save you a good deal of heartache

Easy, well understood deployment process
* Can you deploy and roll back in 1 step?
* Is it fast? Both the overall process and each individual step?

## Code Ownership & Quality

What is the level of comfort your team has with the code?
* Has your team built the codebase?
* Have they maintained it in any meaningful way?
* Do they own it without knowing it?

Well Factored Code
* If an ax weilding maniac who knew where you lived was the next person to maintain the code you're working on, would you be worried?

Health Quality Score
* Does your company have a way to measure code health?
* If not, could you use something off the shelf?
* How many bugs per component exist? Is that number increasing or decreasing?

Fully Owned Code
* Are you in a codebase where you share dependencies or entire sections of your code?

Well Documented Code
* Not commenting per se, but diagrams/drawings/something to help folks understand and dive in

Degrading Gracefully
* Circuit Breakers
* Rate Limiting
* `Retry-After` on 429/503's
* Can the services you rely on fail and would still return a useful response?

## On-Call / Triage

Everyone on the team is on-call

Do you have a process for handling bugs / requests / questions?
* Is there someone who reliably triages questions and concerns?
* Is it one person, or a rotation of people?

"Good" Runbooks
* Can you actually fix problems from them?
* Do they cover most of the common errors your systems experience?

"Good" Alerting
* Do the alerts identity the issue and point towards resolution, or the tools to resolve?
* When your alerts fire, does that cause an action, or do they frequently get ignored/silenced?

Non-Noisy Alerts
* Are your on-calls dreading their shifts because of pages day & night?

Do you have a formal incident policy?
* When do you work into the night vs work 9-5 until its over?
* Do you have a formal incident review process once the incident is over?
* Do you have a process to make sure incident remediation gets completed?

Low Incident Rate

Service License Agreement (SLO) for Services
* What is the expected response time? What's your TP50? TP95? TP99?
* 200 rate? is 4 nines enough?
* Do you alert when you service doesn't perform as expected?

Code is easy to debug
* Easy to plug in debugger?
* Error messages that make sense?
* Can you trace calls from start to finish through your systems?
* Can you time calls from start to finish through your system?

## Testing / Tooling

Load Testing Tooling in Place
* Can you determine the maximum # of callers while maintaining your SLO's?

Acceptance Tests
* Can you test end to end your services?

Integration Tests
* Do you have tests that bridge layers of your codebase?

High Test Coverage
* What percentage of your code has unit tests?

Non-Noisy Tests
* Do you have tests that inconsistently fail? You should fix or delete them

## Metrics/Monitoring

Non-Noisy Logging

Useful Metrics
* Do you track the big metrics?
  * Response/Run time
  * 200's or successful operations
  * 500's or failed operations

"Good" Dashboards
* Can you not only track performance, but the rate at which events happen/don't happen that are relevant?

Useful Logging
* Do you use all the information you're logging?

## Roadmaps

Is there a technical roadmap for each component?

Is there a product roadmap for each component?
