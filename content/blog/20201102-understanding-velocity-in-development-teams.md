---
title: Understanding Velocity in Development Teams
description: Best Practices and Cautionary Tales
date: 2020-11-02T17:31:07-08:00
draft: false
tags: ["Engineering Management", "Management", "Sprint", "Planning", "Velocity", "Agile", "Points", "Pointing"]
categories: ["management", "learning", "development", "Planning", "Agile"]
---

Velocity is a commonly used metric in development teams to measure how much work they can fit into a sprint. However, using velocity for any other purpose can be problematic as it might not reflect the real progress of the project and can be a flawed planning mechanism.

It's crucial to understand that each team defines what a point means for them, making velocity not useful for comparing teams with each other. Each team can track their own velocity to have a better gauge of their progress and how much they can fit into a sprint. Teams should be self-organizing, and how they want to track velocity is up to them.

One use case where velocity can be used as a proxy metric is for cross-cutting concerns, such as investing time in infrastructure to reduce future costs in a certain area. A flat velocity line over a few sprints can indicate that the team is investing time in non-feature work, such as refactoring or technical debt reduction. This can signal that the team is taking a long-term view of the project and focusing on improving the codebase, even if it means that they're not delivering new features at the same rate.

However, it's important to note that using velocity as a proxy metric for cross-cutting concerns should be resolved within the team rather than the organization. This means that the team should decide when to invest in non-feature work and how much time to allocate to it. As a manager, it's your responsibility to ensure that the team has the necessary resources and support to make these decisions.

Cycle time can be a better metric for measuring progress towards cross-cutting concerns. Cycle time is the time it takes for a ticket to move from the "in progress" stage to "done." This metric can be used to measure the time it takes to complete non-feature work, such as refactoring or technical debt reduction. Normalizing the data for days worked, tracking moving averages over 1, 3, and 5 sprints, and using deeper retrospectives to understand trends in the data can help teams make more informed decisions.

In conclusion, velocity is a helpful tool for development teams to plan their work, but it should be used cautiously and only for its intended purpose. A flat velocity line can be used as a proxy metric for cross-cutting concerns, but it should be resolved within the team rather than the organization. Cycle time can be a better metric for measuring progress towards non-feature work, and each team should define their own points to avoid comparing teams with each other. As a manager, your role is to support the team in making informed decisions and provide them with the necessary resources to succeed.
