---
title: Moving Between Tech Stacks
description: How difficult is it?
date: 2023-03-02T17:31:07-08:00
draft: false
tags: ["Engineering Management", "Management", "Project", "Planning", "Tech Debt", "Technical Excellence"]
categories: ["management", "learning", "development", "Project", "Planning", "Performance"]
---

When it comes to software engineering roles, experience in the tech stack you're going to be working in is valuable but not specifically required. A good engineer can ramp up and learn new stacks. However, someone experienced in the tech stack can contribute quickly to key development initiatives, while also bringing outside experience using the stack.

But which tech stacks are easier to move between, and which ones are the hardest? In my experience, when I’ve transitioned from one stack to another, it took a little while to get my footing. But if you already have experience, you can share that experience to up-level the team.

Stacks can be grouped around concepts. For example, a Java stack and a .NET stack have similar OOP concepts, so the typical migration is pretty easy. Similarly, languages like Python, Ruby, and JavaScript are by default weakly typed, so the concepts are the same and it should be easy to port over. However, if the developers on that stack have only used it in one way (e.g., Ruby on Rails, Python/Django, Node/Express), it might be difficult to master the concepts of what the other stack is doing.

Additionally, some shops roll their own software and only use native libraries, while others use a lot of third-party libraries and open-source software (OSS). Moving from a closed-source shop using .NET to an OOS shop using Java (think Java Spring Boot) might actually be really difficult if you've never seen that paradigm.

There are also other factors to consider. For example, in Ruby, extensions are "baked" into the language, and the order you import the packages actually changes how the language behaves. The use of middleware as a concept in your stack vs. a stack that doesn't use middleware can also be a challenge. And a JavaScript stack that heavily uses promises vs. something that uses async/await (or a stack that doesn't use these concepts at all) can require a different mindset.

Add in type hints in Python, or TypeScript in JS, and you have another ball of wax.

So, which tech stacks are easiest to move between? I like to think that the more OSS-friendly, weakly-typed languages are easier to move between. If you get any good at one of these stacks, you typically have to learn a bunch of other concepts (how OSS works, SemVer, modules, duck-typing, etc.).

The ramp-up time for engineers changing stacks is also mitigated a bit by the stack they're coming from. Someone moving from Java to .NET is going to have a shorter ramp up than someone moving from Java to Python (strongly-typed OOP to weakly-typed scripting language) or vice versa. Someone moving from JavaScript (weakly-typed scripting) to Haskell (strongly-typed functional) or vice versa would take even longer.

However, it really depends on your company's mentorship abilities and your ability to be patient as their manager. I think it's hardest to make the migration from a closed-source shop that uses a strongly-typed language to almost anything else. For example, if you're used to working at a bank or for the government on a .NET platform where you're only allowed to use the baked-in MS libraries, then moving to a startup using Python and Django and 100+ other OSS modules might be very challenging.

What they're doing in the stack might impact how quickly they ramp up as well. For example, a person coming from a web dev background in Ruby might find moving to web dev in Python/JS pretty easy. A data engineer moving from Python to Python web dev might really struggle outside of the language
