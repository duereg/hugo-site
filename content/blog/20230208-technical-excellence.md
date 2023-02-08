---
title: Promoting Technical Excellence in your Organization
date: 2023-02-08T13:36:37-08:00
draft: true
images: [{ alt: "Technical Evaluation", src: "/img/evaluation.jpg" }]
tags: ["Engineering Management", "Management", "Project", "Planning", "Tech Debt", "Technical Excellence"]
categories: ["management", "learning", "development", "Project", "Planning", "Performance"]
---

I've seen the approaches you suggested tried in other organizations. I think the thing that it sounds like you're missing is the engineering planning on product initiatives. It's not exactly solution 2 - your tech leads and EM's should be providing guidance here - but more along the lines of establishing a technical culture for your org.

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
