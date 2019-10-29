---
layout: post
title: "What is a PLC and how do I talk Python to it?"
tags:
 - factorytech
 - plc
published: true
date: October 27, 2019
---

If you've found your way to this blog, chances are that you already know that I've given a few conference talks about Python and factory automation.
**Why am I doing this?**

Back at the turn of the century, when I was going to high school[^1], I managed to finagle my way into an internship at the nearby semiconductor factory.
The clean room was the coolest thing I had ever seen!
Given my, uh, limited qualifications I was a pretty useless intern, but the three weeks I spent at the factory had an outsized impact on my life and set the direction of my career.

Since this internship, I have been fascinated by the role that software plays in building the amazingly complex machines which we call "factories".
But I also sometimes feel like I've stumbled upon some very weird niche:
**Most software developers never even encounter factory automation as a place where they can apply their skills.**
At software conferences the topic has a very low profile, and the same is true for podcasts and blogs and all the other places where software engineers exchange knowledge.

I figured I could help change this just a little bit.
**The goal I set for myself is to prepare a conference presentation about an automation topic for a software engineering audience every calendar year.**
So far, it worked and the conference presentations streak has been going for three years!

In 2017 I [brought a conveyor belt on stage at Pycon](https://jonasneubert.com/talks/pycon2017.html) and in 2018 I did a [deep dive into barcodes](https://jonasneubert.com/talks/pybay2018.html).
For 2019 I decided to put together a presentation on Programmable Logic Controls (PLCs).

Head over to my [talks page](https://jonasneubert.com/talks/) for links to video recordings of me talking about PLCs at Python conferences.
This blog post is the first in a series that puts the contents of these talks in writing, including all the content I had to cut out due to time limits on conference talks.

* Part 1: Introduction (you are reading it right now)
* Part 2: What is a Programmable Logic Controller?
* Part 3: [Ladder Logic‽]({{ site.url }}/2019/10/29/ladder-logic)
* Part 4: Using pymodbus to communicate with a PLC
* Part 5: Other protocols and libraries for communicating with PLCs
* Part 6: PLC vs Raspberry Pi
* Part 7: How to get started with Python and PLCs?

I will add links to the table of contents as I publish each part.

---

###### Footnotes

[^1]: Technically, I didn't go to high school because that concept doesn't really exist in Germany. I was in the final two years of the kind of schooling that qualifies you for going to university, which, for a majority American audience, is easiest translated with "high school".

