---
title: Technical State of the Team - Expanded
date: 2022-12-12T12:12:12-08:00
draft: false
images: [{ alt: "Technical Evaluation", src: "/img/evaluation.jpg" }]
tags: ["Engineering Management", "Management", "Project", "Planning"]
categories: ["management", "learning", "development", "Project", "Planning", "Performance"]
---

Note: This is a compliment to the previous article I wrote about the [Technical state of a Team](http://blog.mattblair.co/blog/20210110-measurable-technical-state-of-the-team/), and explains the concepts in depth.

# Technical State of the Team

There’s a saying that people don’t leave companies, they leave managers. Management is a key part of any organization, yet the discipline is often self-taught and unstructured. Getting to the good solutions for complex management challenges can make the difference between fulfillment and frustration for teams, and, ultimately, between the success and failure of companies.

In Will Larson’s excellent book [An Elegant Puzzle](https://amzn.to/3yJshmx) focuses on the particular challenges of engineering management—from sizing teams to handling technical debt to performing succession planning—and provides a path to the good solutions.

One of the early concepts in An Elegant Puzzle centers around the [Four States of a Team](https://lethain.com/durably-excellent-teams/):

The framework starts with vocabulary for describing teams, their performance within their surrounding context. Teams are slotted into a continuum of four states:

* A team is **falling behind** if each week their backlog is longer than the week before. Typically folks are working extremely hard but not making much progress, morale is low, and your users are vocally dissatisfied.
* A team is **treading water** if they’re able to get their critical work done, but are not able to start paying down technical debt or start major new projects. Morale is a bit higher, but folks are still working hard and your users may seem happier because they’ve learned that asking for help won’t go anywhere.
* A team is **repaying debt** when they’re able to start paying down technical debt, and are beginning to benefit from the debt repayment snowball: each piece of debt you repay leads to more time to repay more debt.
* A team is **innovating** when their technical debt is sustainably low, morale is high, and the majority of work is satisfying new user needs.

Teams want to climb from falling behind to innovation, while entropy drags you backwards. Each state transition requires a different tact.

Larson speaks in his blog and his book on strategies for teams transitioning between each state. However, some managers might have problems identifying which state their team is in. Other managers might believe it is better to hide the facts of their team’s failures or shortcomings from their peers or leadership. Other teams might hide the nature of their team’s failures by the excellent always-on work of some key engineers.

## So what is the best way to audit the technical state of an engineering team?

When I worked at Slack, I worked with a talented engineer, and together we came up with a set of questions we thought could help evaluate the technical state of a team.

The way this works; you record a row in a spreadsheet for every API/Site/System that you own. Get as granular as you would like. Then go through the [list of questions](https://blog.mattblair.co/blog/20210110-measurable-technical-state-of-the-team/) for each owned system.

Not all questions apply to all architectures or all system types. Remove the questions that do not apply to the systems that you own.

Once you’re pruned the list of questions, go through and evaluate each system for each question. Each question is evaluated on a binary basis; a question is given a value of 1 if you have the most positive outcome of the questions, and a 0 if you’re unsure or can’t answer the question positivity.

Once you’ve calculated your scores, do some simple math to figure out where your team should be focusing and how it compares to other teams in your organization. Ideally the scores you generate roughly align to the four stages of team progress, so you use some of the guidance there to figure out how to fix the problems your org is facing.

**0%-25%: falling behind**

**25%-50%: treading water**

**50%-75%: repaying debt**

**75%+: innovating**

Once you gathered your data, there are a couple ways to process it:



1. Sum across everything

Add up all your yes answers. Divide by the total number of questions asked. This should give you a percent score of your organization’s technical health.

Example: Say you have 50 total questions and 10 services you’re evaluating. That means you have a possible score of 50*10 = 500 questions for your organization to answer.

Let’s say you add up all of your positive answers, and you get a score of 240. (240 / 500) * 100 = 48%.

Your team is **treading water.**



2. Sum across subject areas

Add up the possible questions and scores for each section you’re focusing on.

Example: Let’s say you have 10 questions around **Metrics** and 10 questions around **Build & Deploy** for your 10 services. You scored a 20 on Metrics and a 60 on Build and Deploy.

For **Metrics**, you scored (20 / 100) * 100 = 20%. Your services are **failing behind** in regard to Metrics

For **Build & Deploy**, you scored (60 / 100) * 100 = 60%. Your services are **repaying debt** in regards to Build & Deploy.



3. Sum across services

Add up the possible questions and scores for each API/Site/System you’re focusing on.

Let’s say you have 50 total questions, and you’ve scored a 40 for your “Alpha Service”.

For the Alpha Service, you scored (40 / 50) * 100 = 80%. Your Alpha Service is **innovating.**
