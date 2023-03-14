---
title: Improving Code Quality on your team
date: 2023-03-14T10:54:47-08:00
draft: true
tags: ["Engineering Management", "Management", "Code Quality", "Quality", "Tech Debt"]
categories: ["management", "learning", "development", "Code Quality", "Quality"]
---



I'm looking at improving the quality within the team I manage. We have a large number of bugs coming out from our (external) QA team and I'm looking at getting the team to take more ownership of their quality. I'm looking at what to measure for to show this is improving.
One idea was measuring the number of bugs created (both from support and by QA) but this is a lagging metric. I was wondering if there was any leading metrics peoples use to measure quality?

Leading metrics could be code quality and test coverage (e.g with a tool like Codeclimate).

Was just going to say this. A simple starting point is adding code coverage, then adding a code coverage floor that your team can't go under. e.g. If your current code coverage is 20%, set that as your "floor" you can't go under. As folks add new code without tests, that will naturally decrease the code coverage. Break the build if this happens, so folks have to add tests. As the code coverage increases, increase the floor/ I've put this strategy into effect in a couple of different places, and rapidly got code coverage into the 90s. With a corresponding decrease in bugs.


Secondly, every bug fix that is put into place should have a corresponding test that would have caught the regression. Ideally written in a TDD style, where you write the test that would catch the issue, it fails as the code is currently written, then you fix the code to make the test pass. That will prevent the same bugs from happening in the future.


Finally, I've sometimes found a "to Verify" state for work can be useful for teams that have bad habits. So for every ticket that is completed, another developer on the team has to verify that it works as expected. Which means the person who wrote the code has to figure out how to test the change, document that, and then explain that to someone else, who then tests it. If you don't have good automated tests then can catch a lot of small issues before they're merged.

Oh, as for measurements outside of something mechanical, you could think about your end-to-end test coverage per page/endpoint/etc. e,g. If you app has 5 distinct UI flows, how many headless, automated browser tests do you have for each of those flows? If you have 10 API endpoints you support, how many automated integration tests have you written for each of those endpoints?
