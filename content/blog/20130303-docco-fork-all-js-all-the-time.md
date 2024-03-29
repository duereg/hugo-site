+++
title = "Docco Fork - All JS, all the time"
date = 2013-03-03
created_gmt = "2013/03/02 18:54:47"
comment_status = "open"
post_name = "docco-fork-all-js-all-the-time"
status = "publish"
tags = ["development","software","coding","web","html","JavaScript","CoffeeScript","EMCAScript","C#",".NET"]
categories = ["engineering", "technical", "javascript"]
layout = "post"
+++

> EDIT: My fork is no longer needed. The folks at docco saw the same thing and recently ported over the library to use [highlight.js](http://highlightjs.org/).

I love documentation generators for code. You know what I've talking about to - something which gives you a split screen of the code and the comments, side by side, for easy reading and scrolling. Like [jasmine](http://pivotal.github.io/jasmine/) uses for their documentation:

![docco](/images/posts/docco.jpg)

Since I've mostly been working in JavaScript lately I've been looking for something to help document the packages I create easily. In comes [docco](http://jashkenas.github.io/docco/).

A CoffeeScript + Python library to help generate good-looking documentation from comments in your code. One thing bothered me about this project - the python part. Docco uses a python library to highlight the syntax. There are plenty of decent syntax highlighters out there - why not use one written in a JavaScript flavor? So I forked docco and plugged in a JS highlighter. Pretty happy with the results.

You can check out the fork [here](https://github.com/duereg/docco).
