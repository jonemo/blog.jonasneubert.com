---
title: "Migrating Projective Set from AngularJS v2 to VueJS v3"
slug: migrating-projective-set-v2
date: "2023-08-14"
tags: projective-set
published: true
---

Today I updated [a small web app](https://projectiveset.jonemo.de/) that I created a decade ago and haven't touched since then.[^1]

The tech stack of the old version was this:

* Bootstrap 2.3.2 (minified version included in repo)
* AngularJS 1.2.16 (embedded from http://ajax.googleapis.com CDN URL)
* jQuery 1.8.3 (also from CDN)
* Github Pages for hosting (using legacy deployment method)

In total there were five files in the repo:

```txt
CNAME             # config for Github Pages hosting
README.md         # to make something show up on the Github repo page
bootstrap.min.css # minified Bootstrap
controller.js     # all logic, 152 lines including whitespace
index.html        # template and inline CSS, 156 lines incl. whitespace
```

There was no build step. Just put these files into a web server directory and done.

For the new version I reached for VueJS, my go-to web framework for the last couple of years. I used the [create-vue](https://github.com/vuejs/create-vue) tool to create a standard VueJS project layout. I chose to use Typescript, ESLint, and Prettier as dev tooling. I did not include state management (Pinia or otherwise), a router, JSX support, or any test tooling.

I'm always a bit lost when it comes to design systems or component libraries. I've used Vuetify before, but it would have been overkill—the number of bytes didn't worry me because that can be optimized but the number of hours I'd spent lost in the docs did. After some "[research](https://npmtrends.com/@coreui/vue-vs-bootstrap-vue-vs-buefy-vs-element-plus-vs-vuetify)" I decided to give [CoreUI for Vue](https://coreui.io/vue/docs/getting-started/introduction.html) a try.

In the migration I added a few features: The results from previous rounds of play are now displayed. A few lines of game instructions are included and can be shown/hidden with a button. The difficulty level can be changed in between rounds without refreshing. I also lost one feature: Keyboard shortcuts are gone, not for any particular reason, I just forgot to port them over and only noticed while writing this post.

The tech stack of the new version is this:

* VueJS v3
* CoreUI v5
* Github Actions for deployment to Github Pages
* Vite as build tool
* Webpack, Prettier, Eslint

There are now more files than I care to enumerate in the repo. Nine of those files are config files whose content I understand but wouldn't have been able to come up with. Most code files are shorter than 50 lines and the code has become a lot more modular and encapsulated.

This isn't one of those blog posts that laments what happened to frontend development in the last years. My brain is still young and adjust to writing `v-for` instead of `ng-for` not problem! People have chosen to build evermore complex solutions in the frontend and thankfully the tooling has evolved to meet those needs while hiding as much complexity as possible. The biggest difference to me is that today it's difficult to avoid using build and developer tools even for trivial apps whereas ten years ago the browser was all I needed.

## Footnotes

[^1]: To be precise: The last meaningful update to the app was on May 20, 2014. Since then the repo had to commits, one for adding a CNAME file when I switched hosting to Github Pages and another for [Google Analytics' v4 migration](https://support.google.com/analytics/answer/11583528?hl=en). The full history is [here](https://github.com/jonemo/ProjectiveSet/commits/main).
