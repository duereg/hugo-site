---
title: Improving Software Quality
description: Leading Metrics to Measure and Strategies to Implement
date: 2023-03-27T10:54:47-08:00
draft: false
tags: ["Engineering Management", "Management", "Code Quality", "Quality", "Tech Debt"]
categories: ["management", "learning", "development", "Code Quality", "Quality"]
---

As a manager, you're responsible for ensuring that the software your team creates is of the highest quality possible. This means reducing the number of bugs and improving code quality. But how do you measure these improvements? And what strategies can you implement to achieve them?

## Measuring Quality
One traditional way of measuring quality is by the number of bugs that are found and fixed. However, this is a lagging metric, meaning that you can only measure it after the damage has been done. Instead, leading metrics can be used to predict the quality of the software before any bugs are found. Two examples of leading metrics are code quality and test coverage.

### Code Quality
Code quality can be measured by using tools such as Codeclimate. These tools analyze your codebase and provide a report on the quality of your code. This includes metrics such as code complexity, duplication, and style consistency. By continuously monitoring and improving code quality, you can prevent bugs from occurring in the first place.

### Test Coverage
Test coverage is another leading metric that measures the amount of code that is covered by automated tests. By implementing a code coverage floor, you can ensure that your team cannot release code that falls below a certain level of test coverage. As new code is added, the code coverage will naturally decrease, but by breaking the build when this happens, you can ensure that your team adds tests to maintain the required level of coverage. This strategy has been proven to rapidly increase code coverage and decrease the number of bugs.

## Strategies to Implement
In addition to measuring quality, there are several strategies that you can implement to improve it.

### Test-Driven Development
One effective strategy is to implement Test-Driven Development (TDD). With TDD, you write tests before you write code. This ensures that your code meets the requirements and prevents regression bugs from occurring. Every bug fix that is put into place should have a corresponding test that would have caught the regression. This approach can be especially effective when working on legacy code, as it provides a safety net when making changes.

### Peer Verification
Another strategy is to implement peer verification. For every completed ticket, another developer on the team has to verify that it works as expected. This means that the person who wrote the code has to figure out how to test the change, document that, and then explain it to someone else, who then tests it. This strategy can be useful for teams that have bad habits, and if you don't have good automated tests, it can catch a lot of small issues before they're merged.

### End-to-End Test Coverage
Finally, you can think about your end-to-end test coverage per page, endpoint, or flow. For example, if your app has 5 distinct UI flows, you should have a corresponding number of headless, automated browser tests for each of those flows. Similarly, if you have 10 API endpoints you support, you should have a corresponding number of automated integration tests for each of those endpoints. By measuring end-to-end test coverage, you can ensure that all critical paths are covered and prevent bugs from occurring.

## Conclusion
Improving software quality requires a combination of measuring and implementing strategies. By using leading metrics such as code quality and test coverage, you can predict and prevent bugs from occurring. Strategies such as TDD, peer verification, and end-to-end test coverage can be implemented to improve code quality and reduce the number of bugs. By continuously monitoring and improving software quality, you can ensure that your team delivers high-quality software that meets the needs of your customers.
