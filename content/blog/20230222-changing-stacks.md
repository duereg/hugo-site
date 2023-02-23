---
title: Which stacks are the easiest to switch between?
date: 2023-02-22T17:31:07-08:00
draft: false
tags: ["Engineering Management", "Management", "Project", "Planning", "Tech Debt", "Technical Excellence"]
categories: ["management", "learning", "development", "Project", "Planning", "Performance"]
---

Another question posed by a friend of mine:

> Which stacks do you think are easiest to move between and which ones are the hardest?

Experience in the tech stack you're going to be working in is valuable — though not specifically required in most Software Engineering roles. A good engineer can ramp up. Someone experienced in the tech stack can contribute quickly to key development initiatives, while also bringing outside experience using the stack.

In my experience, when I’ve transitioned from one stack to another it took a little while to get my footing.
But if you already have experience, you can share that experience to up-level the team.

IMO, you can typically group the stacks around concepts. So a Java stack and a .NET stack, the language and OOP concepts are so similar, the typical migration is pretty easy.

However, if you're a shop where you roll all your software, and only use native libraries, vs. a shop that uses a lot of 3rd party libraries and OSS, moving from a closed-source shop using .NET to a OOS shop using Java (think Java Spring Boot) might actually be really difficult if you've never seen that paradigm.

This goes similarly with Python/Ruby/JS. Languages that are by default weakly typed, the concepts are the same. Should be easy to port over. But if the developers on that stack have only used it in one way (Ruby on Rails, Python/Django, Node/Express), it might be difficult to master the concepts of what the other stack is doing. Especially in the case of something like Ruby where tons of the extensions are "baked" into the language and the order you import the packages actually is important as it changes how the language behaves. Or the use of middleware as a concept in your stack vs a stack that doesn't use middleware. Or a JS stack that heavily uses promises vs something that uses async/await (or a stack that doesn't use these concepts at all).

Add in type hints in Python, or TypeScript in JS, and you have another ball of wax.

Getting back to your original question,  I like to think that the more OSS friendly weakly-typed languages are easier to move between, because if you get any good at one of these stacks, you typically have to learn a bunch of other concepts (how OSS works, SemVar, modules, duck-typing, etc etc).

I think it's also worth mentioning that the ramp-up time for engineers changing stacks is mitigated a bit by the stack they're coming from.

Someone moving from Java to .NET is going to have a shorter ramp up.
Someone moving from Java to Python (Strongly typed OOP to weakly typed scripting language) or vice verse will have a longer ramp up.
Someone moving from JavaScript (weakly typed scripting) to Haskell (Strongly typed functional) or vice versa would take even longer IMO.

It really depends on your company's mentorship abilities and your ability to be patient as their manager.

I think it's hardest to make the migration from a closed source shop that uses a strongly-typed language to almost anything else. Think about working at a bank or for the government on a .NET platform where you're only allowed to use the baked in MS libraries. Then moving to a startup using Python and Django and 100+ other OSS modules. There is almost no overlap between what the developer was doing before hand and what they're doing now. OOP vs scripting, strong vs weak, OOS vs closed source, etc etc.

What they're doing in the stack might impact how quickly they ramp up as well. A person coming from a web dev background in Ruby might find moving to web dev in Python/JS pretty easy. A data engineer moving from Python to Python web dev might really struggle outside of the language due to the complete difference in tools, concepts, etc.

A final caveat - stacks that are outside of the typical scripting/OOP style development. Think of Elm, Haskell, etc etc. Functional programming languages, for folks who have never used them, can be like learning to code from scratch. Even the functional concepts in other languages can't compare to only creating functional concepts.
