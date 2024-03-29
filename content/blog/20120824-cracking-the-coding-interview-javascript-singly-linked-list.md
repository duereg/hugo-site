+++
title = "Cracking the Coding Interview - JavaScript Singly Linked List"
link = "http://codetype.wordpress.com/2012/08/24/cracking-the-coding-interview-javascript-singly-linked-list/"
categories = ["engineering", "technical", "javascript"]
description = ""
post_id = "228"
date = 2012-08-24
created_gmt = "2012/08/24 03:50:08"
comment_status = "open"
post_name = "cracking-the-coding-interview-javascript-singly-linked-list"
status = "publish"
tags = ["development","software","coding","web","html","JavaScript","CoffeeScript","EMCAScript","C#",".NET","algorithms","cracking the coding interview","interviewing","linked list"]
layout = "post"
+++

I finished my first algorithm from [Cracking the Coding Interview](http://www.amazon.com/gp/product/098478280X/ref=as_li_qf_sp_asin_il_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=098478280X&linkCode=as2&tag=aplfopoex-20) - the almighty [Singly Linked List](http://en.wikipedia.org/wiki/Linked_list#Singly.2C_doubly.2C_and_multiply_linked_lists).

This is the low-hanging fruit of the data structures I mean to tackle. Even implementing this simple structure, I managed to somehow squeeze in a bug that luckily I caught in my testing. An unfortunate case of premature optimization.

The code doesn't look as cool as it did, but at least it does the job. One thing I found in reading a bit about Linked Lists on wikipedia, which I had never heard of before; Hash Linking.

> The link fields need not be physically part of the nodes. If the data records are stored in an array and referenced by their indices, the link field may be stored in a separate array with the same indices as the data records.

At first I thought it was a silly way to implement a linked list; if you have an array storing your values, what value are you getting from the list?

Once I thought a little more, I realized the value of the link field being stored in a separate array. You can easily re-order your list by changing the values in the array, without traversing and without touching your data.

This might be a valuable solution if the relationship between items constantly changes but the size of the data remains somewhat static. In the notes of various implementations of this pattern I've seen, people have commented on how they expand the array when more spots are needed.

I have yet to see any information about if you shrink the array once the "list" contracts to a certain point. The source code for the project and the tests is [here](https://github.com/duereg/js-algorithms).
