---
title: Running Your Projects
date: 2022-10-08T05:17:17-08:00
draft: false
images: [{ alt: "Incident Review", src: "/img/cool-plan-person.jpg" }]
tags: ["Engineering Management", "Management", "Project", "Planning"]
categories: ["management", "learning", "development", "Project", "Planning", "Performance"]
---

Note: This is a series of project planning talks I gave my team.

<h3>Running your project</h3>


<h4>Writing A Technical Design Document</h4>


At this point, you’re ready to start designing your system.

A good technical design document should contain:



* An overview of the problem
* A breakdown of the individual milestones and how they’re related
* High-level process / workflow diagrams / designs / etc
* Any other notes that might be relevant to folks who will be working on the project

You should also consider if certain steps can be done in parallel, and what steps block other aspects of the work. Make sure to prioritize blocking steps, and possibly assign parallel work out simultaneously (if staffing permits).

Attempting to breakdown work or introduce parallelism for projects that were not initially designed that way can cause problems later on. So it’s best to figure out in the design phase what work that can be done in parallel (planning for multiple developers).

Once your technical design is complete, you should review it with the engineering team before starting on your milestones.

<h4>Setting up goals / milestones / tickets</h4>


The planning phase is key to successful projects and focuses on developing a roadmap for the team to follow. During the planning phase, you should plan to organize your team, set up resources, and set goals.

After your design doc is complete and vetted, you should deconstruct each milestone into smaller chunks (tickets) so one person can be assigned responsibility for each facet.

In breaking down the work, consider many factors such as the strengths and weaknesses of project team members, the interdependencies among tasks, available resources, and the overall project deadline.

<h5>How do you know your milestones were successful? </h5>




* Should be clear what you’re delivering
    * What is the smallest thing we can deliver to our customers/partners so they can validate our approach?
        * Example: If you’re building a complex webpage, could you ship a read-only, not interactive version of the page, to test that the data displayed is what they want?
    * How can you split up the work into the smallest pieces possible that can be shown to your stakeholders?
* After you ship a milestone, you should get sign-off from your stakeholders
    * This can be as small as a demo at the sprint meeting
    * Stakeholders should sign off on what you did
        * If something is wrong, better to find out earlier than later
* You need time for fast-follow work after each milestone
    * If the customer requests changes based of the sign-off session, you want to have time in your schedule for that
    * If you find small pieces of tech debt/bugs while working on the milestone, fix it directly afterwards while it’s fresh in your mind.
* Does your milestone fit your overall timeline?
    * If the project has a two month deadline, but the work you’ve laid out for the 1st milestone will take three months, you need to figure out how to get on track fast
        * Can you cut scope?
        * Can you increase velocity by adding more developers?
        * Can you deliver a proof of concept by the deadline and follow up with the rest of the work?

<h5>What work should you include in your milestones? </h5>




* You need time devoted to design, review, write tech specs
    * Each milestone should include a tech design doc and a review session
    * This can be a paragraph or a multi-page document
    * You should get a review and a sanity check for each tech design doc you create.
* You need time devoted to metrics / data / monitoring what you built
* Implement monitoring and error visibility to make it easier to debug problems down the road.
* Ideally you have a way to record usage whenever we can to illustrate impact.
* implement monitoring & debugging for every milestone, every deliverable
* You need time devoted to testing
* Unit tests for new work is a minimum
* Implement automated testing early in the process
* Write a Test Plan/Test Matrix up-front if you’re building a complex system with many interactions
* You need time devoted to tech debt
    * Fix broken windows along the way
* Broker time for tech debt
* Broker time for related bugs in the backlog
* Build quality into every phase of the project
* **How would you build this if you had to maintain it forever?**

<h4>Communicating Updates</h4>


There should be constant, detailed, concise status updates in your project channel. This is particularly helpful when rolling new people on because you can say "please go back and read the content of the channel for the past week".

Relevant documents (such as your kickoff slidedeck and your technical roadmap) should be included in your project channel.

You should invite your stakeholders to your project channel to have a central place to vet ideas and invite feedback.

When setbacks occur, you should highlight the risks early and often in the channel. Surprises are worse than setbacks.

<h4>Involve the whole team along the way</h4>




* Include more people in code reviews even if they're not actively picking up development tasks
    * this shares out knowledge of the changes and gets another set of eyes that can ask good questions
* Break team silos where possible and share knowledge
* Do Team PR's for big PR's
    * Ideally break work into small pieces though
* Demo your work early and often
* Try to avoid having single developers on projects
