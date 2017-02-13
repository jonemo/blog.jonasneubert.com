---
layout: post
title: "Fluidinfo API Contest: Fluidinfo API Contest: Design Decisions"
tags:
 - fluidinfo
published: true
date: Apr 18th, 2011 3:09pm
---

I announced yesterday that I am currently working on a submission to the O'Reilly/Fluidinfo API contest. You should check out the other submissions so far:

* [BookChirpa](http://www.bookchirpa.com/) by Mark McSpadden is a data mashup project showing recent tweets about O'Reilly books enriched with information about these books which is pulled from Fluidinfo. There is an [About page with a whole bunch of technical info](http://www.bookchirpa.com/about). Ironically, the top entry on the [Bookchirpa library page](http://www.bookchirpa.com/books) is "21 Recipes for Mining Twitter".
* David Karapetyan opts for a submission which only adds data to the Fluidinfo data store but doesn't have a frontend. That's legit by the contest rules. [Here's a blog post about how he added Amazon Suggestions to each book](http://articulationstudy.posterous.com/oreilly-writable-api-competition). 90% of his post are crossed out indicating that the story behind his submission isn't exactly linear.
* Eric Seidel's submission is really similar to Skillshelv.es. Shockingly similar. [Read about it in his blog](http://eseidel.org/blog/2011/04/fluidinfo-oreilly-competition/). By the looks of it he's been a Fluidinfo aficionado before because his prior project FluidCV is based on it. His submission to the contest is to let people add O'Reilly books to their FluidCV to - hold your breath - show their skills based on the books they own. Disclaimer: I hadn't seen his project when I started working on [Skillshelv.es](http://www.skillshelv.es/).
* Michael Hawes noticed that the books which Fluidinfo imported into their database are only those English language ones sold in the USA. But O'Reilly also publishes books in other languages in the small part of the earth known as ROTW to Americans (the acronym stands for both Rest of the World and Rim of the World). He embarked on the mission to add links to the foreign language equivalents to all existing Fluidinfo book objects. Like David K.'s entry, Michael's has no front page, [but extensive documentation on his blog](http://www.gottahavacuppamocha.com/about/oreilly-fluidinfo-api-competition/).
* Rachel Willmer [wrote an extension](http://luzme.com/blog/2011/04/luzme-enters-fluidinfos-writable-api-competition/) to her eBook price aggregator [Luzme.com](http://www.luzme.com/) to send up to date eBook pricing details into the Fluidinfo data store. She writes that she will only sync this data for the duration of the competition but I sure hope she continues to do so after the deadline on Sunday night.
It strikes me how open everyone is about what their entry is and how they went about creating it. So I won't hold back either and write up the details on my submission, predominantly in this blog and maybe later on as part of the Skillshelv.es site. Today, let's talk about the design decision that had to be made before I started touching my keyboard.

## Quick Recap

Here's the quick technical summary of what my submission will do: Each book will be tagged with one or more skills representing the expertise conveyed in the book. Each book will also be tagged with usernames to represent ownership. Based on this info, users' skill levels and some other derivative data will be computed.

## Platform & Language

Based on my skill set (which you will soon be able to see on Skillshelv.es) and my resources the options are: PHP on my shared webspace, Python on Google App Engine (GAE), or mostly browser based JavaScript. Doing things purely in Javascript would be appealing because it would allow for a very snappy interface and server load would virtually never become a concern. But at least for the write operations to Fluidinfo we need to authenticate and obviously sending my Fluidinfo password to the client as Javascript isn't cool. So the Javascript only option won't fly. That leaves us with GAE or shared hosting. Thankfully, there are Fluidinfo libraries available for many languages including [Python](https://github.com/paparent/phpFluidDB) and [PHP](https://github.com/paparent/phpFluidDB) so this wasn't a concern. I decided to go with GAE because I wanted to get a little more experienced in working with it. After all, what's the point of doing anything if you don't learn from doing it?

## User Authentication

Any service that requires user accounts presents the headache of authentication. Sure, there is fancy PECL packages and libraries and whatnot, but in the end you'll still be storing usernames and passwords and sending password reset emails and all that. I decided to give OpenID a shot. I know that OpenID [is](http://productblog.37signals.com/products/2011/01/well-be-retiring-our-support-of-openid-on-may-1.html) [a](http://blog.wekeroad.com/thoughts/open-id-is-a-party-that-happened) [failure](http://www.quora.com/OpenID/What-s-wrong-with-OpenID). I don't care. I want to fail in the first person. The good part is that [Google App Engine makes using OpenID ~really~ easy](http://code.google.com/appengine/articles/openid.html).

## Data Source

To determine what skills someone has based on the books they read, each book needs to be associated with skills. That data is not available (neither in Fluidinfo nor on the O'Reilly website) so I need to make it. At first, I thought about using Amazon Mechanical Turk to gather this data. That might work if the books had to be sorted into a known set of tags. But since I am not intimately familiar with O'Reilly's book inventory, I didn't even have the list of skills to start with. In the end I figured, that to get consistency I should first tag all >2000 books myself. Maybe I can recruit specialists in fields that I am not familiar with later on to check and refine my work. Let me know if you are interested. At this point it looks like I might need help sorting the Java and Microsoft Server Products groups of books.

## Namespace or Tag?

So the plan is to tag books with skills. Fluidinfo allows [pretty much any content as a tag's value](http://doc.fluidinfo.com/fluidDB/api/tag-values.html) and tag names are alphanumeric. That opens two sensible options:

1. Use one tag `/skillshelves/skills` to hold a list of all tags associated with the book.
2. Make each skill a tag inside a `/skillshelves/skills/` namespace.

Let's think about the types of queries Skillshelv.es will run: We'll need to know which books are owned by a user, and which books belong to a certain skill, and maybe which books belong to a certain skill and to a certain user. [Fluidinfo's query language](http://doc.fluidinfo.com/fluidDB/queries.html) would enable both data models:

1. Use the `contains` operator for the single `skills` tag containing a list of skills.
2. Use the `matches` operator for the namespace of individual `skills` tags.

But what if I want to store some additional meta info for each skill? I am currently toying with the idea of categorizing each book as *Beginner*, *Intermediate*, or *Expert*. This could still be stored either way (instead of a list, use a JSON object), but I don't think the `contains` operator can look inside opaque tag values and even if it can it would probably be way slower.

## Where is the data?

This question is about where data should be stored. There is the data store local to GAE and there is the Fluidinfo data store. The former is fast and hidden to the public, the latter is slow and everything in there is public. The idea behind Fluidinfo is to make data publicly accessible and writable so my goal is to store as much data as possible in Fluidinfo. That means, both the skill tags and the ownership information will be stored in Fluidinfo. Due to the data model described in the section above, the tags in the skills namespace are a full list of skill categories and the tags in the user namespace are a complete list of Skillshelv.es users. Therefore, basically all data is stored in Fluidinfo's data store and nothing locally in GAE's data store. I'll make three exceptions to that rule:

1. User data: To make authentication and authorization on the page easier, all usernames are stored locally, too. Theoretically, even the info needed for authentication could be held in Fluidinfo but seriously, why should it?
2. List of display names of skills: Because each skill is a tag in Fluidinfo and tags may not contain spaces and some other symbols (e.g. the + in C++), a list of skills is held locally where the display name of each skill and the corresponding Fluidinfo tag are stored. This also allows me to change the display of a skill wihout the hassle of having to change the tags on all affected objects.
3. Full list of books: Retrieving the full list of books from Fluidinfo takes lots of time and data volume. To make matters worse, there is no way (known to me) of limiting the size of a result set returned from Fluidinfo which would be helpful for querying the next book that needs tagging. To cut the hassle, I keep a full list of all object IDs associated with O'Reilly books in the local data store and use it for backend work (like tagging >2000 books, doh).

## Summary

The above is a tour de force through all the major design decision I made before sitting down to code Skillshelv.es. I think I'll be doing a pretty decent job at demonstrating how Fludinfo can be used as the main data storage location for a project. Obviously I am betting on my luck by planning on pulling this project off in less than two weekends while using technologies I am not very familiar with. We'll see how it goes. *[The Editor: It went ok.]*
