---
title: Establishing 1-1s that work
date: 2024-03-05T11:52:59-08:00
description: My lessons learned
draft: true
tags: ["Engineering Management", "Management", "Direct Reports", "1-1", "1:1", "one on one"]
categories: ["management", "direct reports"]
---

## Background

In my current role, I inherited an older codebase where best practices were often overlooked. As I reviewed the code and the surrounding processes, I found numerous areas for improvement in both code quality and operational practices.

## Where to Start?

When tackling a project like this, I find it best to break down the necessary changes into four categories:

1. Immediate Changes
2. Short-Term Changes
3. Medium-Term Changes
4. Long-Term Changes

## Immediate Changes

Stack Overflow used to offer a list of concrete practices that engineering companies should follow. These include specific technical and operational practices, such as:

1. **Repeatable Builds:** Ensuring that builds can be reliably reproduced in any environment.
2. **Source Control:** Using version control systems like Git for all code.
3. **One-Step Build:** Implementing a one-step build process for simplicity and efficiency.
4. **Daily Deployments:** Enabling and encouraging frequent code deployments to catch issues early.
5. **Bug Tracker:** Utilizing a bug tracking system to manage and prioritize issues.
6. **Testing:** Incorporating automated tests within the code to ensure reliability and quality.
7. **Monitoring:** Setting up monitoring tools to track the performance and health of applications.
8. **Staging Environment:** Maintaining a staging environment that mirrors production for testing changes.
9. **Code Reviews:** Conducting code reviews to maintain quality and share knowledge.
10. **Documentation:** Providing comprehensive documentation for code, processes, and systems.

Some of these practices are more critical than others. For me, the following are deal breakers if they don't exist:

- Source Control
- Repeatable Builds
- Code Reviews
- Monitoring
- Automated Tests

When I started my current job, we lacked repeatable builds and automated tests. These became my top priorities, and I implemented them first.

## Short-Term Changes

Once immediate priorities are addressed, focus on team-wide changes to improve code quality.

### Identifying Problems

Look at what your code reviews are highlighting. Are there issues with the current production code, such as slowness or memory leaks?

In my role, we had a long-standing memory leak due to a lack of development guidance and best practices. This required a detailed code review to identify problematic areas and practices, which we then addressed systematically in each pull request.

### Two-Pronged Approach

**Systemic Changes:** Implement automated systems to facilitate good practices. For example, use code linters and enforce code coverage standards for PRs. This allows code reviews to focus on holistic issues rather than basic formatting or style.

**Process Changes:** Establish and document the rules you want your code to follow. Create a Contributing guide and ensure code reviewers adhere to these practices.

Examples from our Contributing guide include:
- Use Functional Components over Class Components
- Use `invoke` for events rather than `send/receive` where possible
- Use Named Functions over Anonymous functions when possible
- Use Custom Hooks for Repetitive UI Logic

## Medium-Term Changes

These changes are straightforward but not easy. They often require dedicated project bandwidth to complete.

For us, medium-term changes included:
- Moving to shared components between systems (Internal Open Source)
- Transitioning to a different logging stack
- Creating a One-Step Build process
- Switching to a different compiler
- Developing a comprehensive integration test suite

## Long-Term Changes

These changes are neither straightforward nor easy. They often involve structural modifications and should be approached with caution.

In our case, this meant restructuring a significant portion of our codebase. However, it's crucial not to rush into these changes. Take the time to fully understand the issues at hand to avoid suboptimal solutions. The best time to make these decisions is at the last possible moment, when you have the most information.

---

By following this approach, you can systematically improve your codebase and development processes, ensuring a more robust and maintainable system for the future.
