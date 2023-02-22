---
title: Promoting Technical Excellence in your Organization
date: 2023-02-21T17:31:07-08:00
draft: false
tags: ["Engineering Management", "Management", "Project", "Planning", "Tech Debt", "Technical Excellence"]
categories: ["management", "learning", "development", "Project", "Planning", "Performance"]
---

I was speaking to a friend who works at a startup with a team of around 14 engineers. 80% of them are mid level engineers with 3-4 years of experience. They all work in product squads covering specific areas.

These have lost momentum in the development and they are seeing 2 key problems:

1) The teams lacks direction on where to focus their energy and prefer tackling small issues as they don't have a vision as to what impactful engineering initiatives to do.
2) They are struggling to find time to work on technical debt. There is a perception that they should be working on Product work all the time.

She had originally proposed two solutions, but wanted to hear my thoughts:

1) Allocating a percentage of time per week to work on tech debt.
2) Getting the Tech Lead and EMs to set the technical direction of what to work on.

In our view solution 1 sounds like it might help relieve some of problem 2 but not really address problem 1.

Solution 2 would solve the issues, but she was worried that would take the autonomy/empowerment from engineers to really own those initiatives.

I've seen both of these approaches tried in other organizations. We ended up steering the conversation towards engineering planning on product initiatives.

Engineering planning on product initiatives is not exactly her 2nd solution - where tech leads pick the tech debt to work on. It's more a strategy along the lines of establishing a technical culture for your org.

An example: Product wants to add a button a screen. You could leave it at that and an engineer could code up a solution. In high-functioning engineering organizations, the leadership has set up a set of principles that allow you to bake in engineering excellence work along the way. So for this example, a couple principles that might apply:
* The page has to load in under 1 second
* All new code has to have corresponding unit tests
* All new UI features have to corresponding headless browser tests
* The APIs that support the page have to respond in under 200ms.
* etc etc etc

So as the developer is doing the work, they're baking in engineering excellence. If adding the button slows down the page dramatically, they have to figure out a way to get the page load time down.

The person reviewing their code has to check for the presence of the right kind of tests.
Someone has to verify the new data being used by the button doesn't slow down the system.

All of these are cultural things that slow down development slightly, but they leave with a durable foundation that really accelerates your development later on.

This allows developers to drive the technical excellence of their products, by baking in their principals into their projects and their everyday practices.

It removes the idea of needing 20% time to pay down technical debt. You pay down your debt on every project. If you're touching code that needs improvement, it's part of the project itself. The larger the project, the larger the amount of debt you can pay down
