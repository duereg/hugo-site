---
title: "Breakdown; post-mortem of a process failure"
date: 2021-02-17T18:49:50-08:00
draft: false
images: [{ alt: "Incident Review", src: "/img/incident-response.jpg" }]
tags: ["Project Management", "Management", "Incident Response"]
categories: ["management", "learning", "development", "incident"]
---

I was reviewing an old incident review doc where I wrote up some of the high level learnings from the incident. Thought it was worth sharing, with the details omitted to protect the innocent.

Some backstory; we were trying to load test a component and ended up getting the load testing done at the last minute right before customer launch. The team had to work into the weekend to meet the customer deadline.

So while this wasn't an "incident" as most people would define it, the fact that our process failed us in a way that we missed several deliverables led me to run a review of our process, much like in a typical post-mortem. Here were the team's findings.

## When lacking knowledge, use historical data.
We got stuck early in the process trying to get the customer's release plan, where we could have looked at what we had done other customers had done for their release plans. Using that data, we could have suggested a plan, and moved forward under those assumptions. The fact that we didn’t have comprehensive data until almost a week into the project shouldn’t have slowed us down as much as it did.

## When looking for direction, write up a plan and look for feedback
Our original plan for this project consisted of an Epic and a write up of tickets. For these type of projects, it is expected that a load test plan would be written up and vetted with folks outside of the team. This was a known requirement of the project that wasn’t completed until very late in the process, and we didn’t have sign-off until the day of our load testing. Had we done this early in the process, we would have gotten valuable feedback about our approach early, and most likely met our deadline.

## Make “unreasonable” asks
Early in the process, we booked a late load testing time (the day of the deadline at 1pm). The reason we did this wasn’t that we wanted to test this late, but that by the time we signed up, this was the only timeslot left available. This would have been a good time to make an “unreasonable” ask of the loadtest team, and see if they could accommodate us at another time, either before or after their normal slots.

The worst thing that could happen is they say no, and at least then it’s known that you’d like to test earlier, in case someone else cancelled or can’t make their slot.

## Ask for help early and often
We hit some snags with our load testing, but the request for help didn’t come up until late in the process, and the biggest push for assistance came days before our load testing deadline. Had we front-loaded some of these questions, we probably wouldn’t have missed our deadline.

Additionally, some of the updates from the team indicated we were on track when we were not. Had those updates been more transparent, we would have had the right folks working on the right set of problems.

One of the problems we hit was testing multiple users vs a single user. This was never highlighted in channel until it was uncovered during load testing on the day of the deadline. Had this been highlighted earlier, we might have swarmed on the problem then.

## Swarm on problems early
Going into the deadline, we did not have a working load test script that met our requirements. By early Saturday morning (after our deadline) we did. The key here was that 4 people jumped on a call and walked through the problems, live debugged, and kept folks focused on the problem. After a few hours we had a working proof of concept.

While we needed much of the early context and research to allow for this to happen, if we had swarmed earlier in the week we might have come up with a solution at our deadline.
