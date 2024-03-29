+++
title = "Ember - The content property of DS.PromiseArray should be set before modifying it"
description = "Ember - The content property of DS.PromiseArray should be set before modifying it"
date = 2014-04-08
post_name = "ember-the-content-property-of-ds-promise-array"
status = "publish"
tags = ["development","software","coding","web","html","JavaScript","CoffeeScript","EMCAScript","Ember","Ember.js","Ember.data"]
categories = ["engineering", "technical", "javascript"]
layout = "post"
+++

## The content property of DS.PromiseArray should be set before modifying it

If you see the following error in Ember.Data 1.0.0-beta.7:

**The content property of DS.PromiseArray should be set before modifying it**

The issue is with changing the contents of an async field.

```javascript
//program.js
Program = DS.Model.extend({
  styles: DS.hasMany('style', {async: true}),
});

Style = DS.Model.extend({});
```

and then used like so:

```javascript
program.get('styles').pushObject(style);
```

That code will throw the exception listed above. To work around this behavior, do the following:

```javascript
program.get('styles').then(function(styles){
  styles.pushObject(style);
});
```

A gist talking about the issue is [here](https://gist.github.com/Microfed/6573839).
