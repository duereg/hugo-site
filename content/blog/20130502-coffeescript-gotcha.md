+++
title = "My ongoing relation with CoffeeScript - and a gotcha"
description = ""
date = 2013-05-02
comment_status = "open"
post_name = "coffeescript-gotcha"
status = "publish"
tags = ["development","software","coding","web","html","JavaScript","CoffeeScript","EMCAScript","C#",".NET"]
categories = ["engineering", "technical", "javascript"]
layout = "post"
+++

[CoffeeScript](http://coffeescript.org/), what can I tell ya - I didn't want to love it.

I have an unreasonable grudge against significant whitespace.

I couldn't figure out the value of a language that compiles to another reasonable language.

And don't even get me started on the for of/in thing. I still don't understand that.

But the more I use CoffeeScript, the more I love it.

The lambdas are probably my biggest love - how can you not love them, in comparison to what JavaScript makes you do?

However, I found something out the other day that seems slightly counter-intuitive to me.

``` coffeescript
supposedToBeArray = null
if foo in supposedToBeArray
  # You will never reach this code, because the line above throws an exception.
```

I guess my thought would be `if foo in supposedToBeArray` would return false. But nope, throws when the object is not an array (or is not array-like).
