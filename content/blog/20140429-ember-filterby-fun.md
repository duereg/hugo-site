+++
title = "Ember FilterBy Fun"
description = "Ember FilterBy Fun"
date = 2014-04-29
post_name = "ember-filterby-fun"
status = "publish"
tags = ["development","software","coding","web","html","JavaScript","CoffeeScript","EMCAScript","Ember","Ember.js","Ember.data"]
categories = ["engineering", "technical", "javascript"]
layout = "post"
+++

If you happen to be writing filterBy statements in Ember against an object, you will want to use this syntax:

```javascript
  skusForStyle: function(style) {
    return this.get('mergedSkus').filterBy('style.id', style.get('id'));
  }
```

Instead of this similar looking but exceptionally evil and non-functioning cousin:

```javascript
  skusForStyle: function(style) {
    return this.get('mergedSkus').filterBy('style', style);
  }
```
