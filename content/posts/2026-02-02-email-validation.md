---
title: 'So you think this library can validate email addresses'
slug: email-address-validation
date: '2026-02-02'
tags: []
draft: false
---

> Let's add some validation for this email address form field!

I usually write software for automation, but like every software developer I'm not immune to email address validation.

## So you think you can validate email addresses

The FOSDEM 2018 talk "So you think you can validate email addresses" by [Stavros](https://www.stavros.io) has become a canonical reference for expressing the futility of all attempts to validate email addresses.
[You can watch it on Youtube](https://www.youtube.com/watch?v=xxX81WmXjPg).
In the talk, Stavros shows a series of email addresses and asks the audience to shout "valid" or "invalid" for each one.
After 26 examples (that include 32 @ symbols) Stavros recommends a two step process for email address validation:

Step 1: Check if the string contains at least one "@".

Step 2: Send an email to it. If that works, it was an email address.

## Email validation libraries

Not everyone agrees with this recommendation.
Email validation libraries exist in great numbers and most languages.

**How do email validation libraries compare when faced with the examples from Stavros' talk?**

That's the question I set out to answer in this blog post.

## Validation versus verification

Before we dive in: Terminology.

**Validation** is the process of deciding for a given string whether it follows the format rules for email addresses.

**Verification** is the process of deciding for a given valid email address whether it can receive email.

An email address can be valid but unverified, for example if its domain part is an unregistered domain, or if the domain points to a server that isn't running a server that accepts email.

Valid email addresses can be compared to various other patterns and lists.
A **Disposable Check** compares against a list of domain names and string patterns associated with [masked email services](https://en.wikipedia.org/wiki/Disposable_email_address).
A **Personal Email Check** compares against a list of domains commonly used by end users for personal use.
(Websites use this to coerce people into providing their work or business email address, for example in "sign up to download this whitepaper" flows.)

Many libraries offer some combination of validation, verification, and checks.
In this blog post I focus exclusively on validation.
For libraries that validate _and_ verify by default, I tried to disable the verification part to the extend possible.

## Request For Comment

The closest we have to a standard for the email address string format is a set of [RFCs](https://en.wikipedia.org/wiki/Request_for_Comments):

- [RFC 5322](https://www.rfc-editor.org/rfc/rfc5322) defines the email address format. Wouldn't it be nice if this list ended here?
- [RFC 5321](https://www.rfc-editor.org/rfc/rfc5321) defines the entire SMTP protocol (for email sending). The protocol defines a slightly stricter grammar for email addresses to which emails can be sent with SMTP.
- RFCs [6530](https://www.rfc-editor.org/rfc/rfc6530), [6531](https://www.rfc-editor.org/rfc/rfc6531), [6532](https://www.rfc-editor.org/rfc/rfc6532) all have something to say about international email addresses. Where "international" refers to alphabets that go beyond ASCII. And also [emojis](https://mailoji.com).
- The above RFCs generally say that the part after the "@" must be a valid domain name. [RFC 10356530](https://www.rfc-editor.org/rfc/rfc1035) defines those.

One difference between RFC 5322 and RFC 5321 features in two of Stavros' examples: The former has the concept of parentheses-enclosed comments like `(comment)name@domain.com` or `na(comment)me@domain.com`.

Separate from RFCs, [the HTML5 standard specifies a regular expression](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/email#validation) with which browsers should validate inputs for `<input type="email" />` form fields.

Some libraries declare that they implement [RFC 5321](https://www.rfc-editor.org/rfc/rfc5321) or [RFC 5322](https://www.rfc-editor.org/rfc/rfc5322) or the HTML5 standard, but most intentionally or unintentionally don't strictly follow either.

## Comparison Table

## Summary

| Library                  | Correct | False Negatives | False Positives |
| ------------------------ | ------- | --------------- | --------------- |
| aftership-email-verifier | 22      | 6               | 0               |
| apache-commons-validator | 22      | 4               | 2               |
| checkmail                | 25      | 2               | 1               |
| deep-email-validator     | 15      | 3               | 10              |
| django-emailvalidator    | 20      | 8               | 0               |
| egulias-email-validator  | 23      | 2               | 3               |
| email-addresses          | 25      | 1               | 2               |
| email-valid-perl         | 24      | 2               | 2               |
| email-validator          | 18      | 10              | 0               |
| emailvalidation-dotnet   | 21      | 7               | 0               |
| hibernate-validator      | 21      | 5               | 2               |
| joi                      | 19      | 9               | 0               |
| libvldmail               | 23      | 2               | 3               |
| mailaddress-dotnet       | 22      | 3               | 3               |
| mailkit-dotnet           | 25      | 1               | 2               |
| net-mail                 | 23      | 4               | 1               |
| php-filter-var           | 18      | 9               | 1               |
| pyisemail                | 21      | 6               | 1               |
| python-email-validator   | 22      | 6               | 0               |
| rust-email-address       | 24      | 3               | 1               |
| symfony-validator        | 16      | 10              | 2               |
| truemail                 | 16      | 10              | 2               |
| valid-email2             | 19      | 7               | 2               |
| validator-js             | 23      | 5               | 0               |
| validator-rust           | 17      | 8               | 3               |
| wordpress-is-email       | 16      | 10              | 2               |
| zod                      | 16      | 12              | 0               |

## Expected Valid Emails

- ✓ = correctly accepted
- ✗ = false negative (incorrectly rejected)

1. `foo@bar.com` - simple test case
2. `hi@stavros.io`
3. `hi+there@stavros.io` - plus is allowed
4. `stavros.k@stavros.io` - dot in local part is valid
5. `f*uck@stavros.io` - asterisks are allowed in local part
6. `#$%!^/&@stavros.io`
7. `(sta)vros@stavros.io` - (sta) is a comment
8. `stavros@stavros.io(io)` - (io) is a comment
9. `"hi@you"@stavros.io` - quoted at symbol in local part is allowed
10. `"hi you"@stavros.io` - quoted space in local part is allowed
11. `" "@stavros.io` - quoted space in local part is allowed
12. `"<\"@\\"".!#%$@stavros.io` - quotes are separated by dots
13. `cow@[dead::beef]` - IPv6 domain part
14. `stavros@io` - domain part is TLD
15. `我買@屋企.香港`
16. `1@[23456789]` - [23456789] is a decimal IPv4 address

| Library                  | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 10  | 11  | 12  | 13  | 14  | 15  | 16  |
| ------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| aftership-email-verifier | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✗   | ✗   | ✓   | ✓   | ✓   | ✗   | ✗   | ✗   | ✓   | ✗   |
| apache-commons-validator | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✗   | ✗   | ✓   | ✓   | ✓   | ✓   | ✓   | ✗   | ✓   | ✗   |
| checkmail                | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✗   | ✓   | ✓   | ✗   | ✓   |
| deep-email-validator     | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✗   | ✗   | ✓   | ✗   |
| django-emailvalidator    | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✗   | ✗   | ✓   | ✗   | ✗   | ✗   | ✓   | ✗   | ✗   | ✗   |
| egulias-email-validator  | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✗   | ✓   | ✓   | ✓   | ✗   | ✓   | ✓   | ✓   | ✓   |
| email-addresses          | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✗   | ✓   | ✓   | ✓   | ✓   |
| email-valid-perl         | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✗   | ✓   | ✓   | ✗   | ✓   |
| email-validator          | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✗   | ✗   | ✗   | ✗   | ✗   | ✗   | ✗   | ✗   | ✗   | ✗   |
| emailvalidation-dotnet   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✗   | ✗   | ✓   | ✓   | ✓   | ✗   | ✗   | ✗   | ✗   | ✗   |
| hibernate-validator      | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✗   | ✗   | ✓   | ✓   | ✓   | ✗   | ✗   | ✓   | ✓   | ✗   |
| joi                      | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✗   | ✗   | ✗   | ✗   | ✗   | ✗   | ✗   | ✗   | ✓   | ✗   |
| libvldmail               | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✗   | ✓   | ✓   | ✓   | ✗   | ✓   | ✓   | ✓   | ✓   |
| mailaddress-dotnet       | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✗   | ✗   | ✓   | ✓   | ✓   | ✗   | ✓   | ✓   | ✓   | ✓   |
| mailkit-dotnet           | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✗   | ✓   | ✓   | ✓   | ✓   |
| net-mail                 | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✗   | ✓   | ✓   | ✓   | ✓   | ✗   | ✗   | ✓   | ✓   | ✗   |
| php-filter-var           | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✗   | ✗   | ✓   | ✗   | ✗   | ✗   | ✗   | ✗   | ✗   | ✗   |
| pyisemail                | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✗   | ✗   | ✓   | ✓   | ✓   | ✗   | ✗   | ✓   | ✗   | ✗   |
| python-email-validator   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✗   | ✗   | ✓   | ✓   | ✓   | ✗   | ✗   | ✗   | ✓   | ✗   |
| rust-email-address       | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✗   | ✗   | ✓   | ✓   | ✓   | ✗   | ✓   | ✓   | ✓   | ✓   |
| symfony-validator        | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✗   | ✗   | ✗   | ✗   | ✗   | ✗   | ✗   | ✗   | ✗   | ✗   |
| truemail                 | ✓   | ✓   | ✓   | ✓   | ✓   | ✗   | ✗   | ✗   | ✗   | ✗   | ✗   | ✗   | ✗   | ✗   | ✓   | ✗   |
| valid-email2             | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✗   | ✗   | ✓   | ✓   | ✓   | ✗   | ✗   | ✗   | ✗   | ✗   |
| validator-js             | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✗   | ✗   | ✓   | ✓   | ✓   | ✗   | ✓   | ✗   | ✓   | ✗   |
| validator-rust           | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✗   | ✗   | ✗   | ✗   | ✗   | ✗   | ✓   | ✓   | ✗   | ✗   |
| wordpress-is-email       | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✗   | ✗   | ✗   | ✗   | ✗   | ✗   | ✗   | ✗   | ✗   | ✗   |
| zod                      | ✓   | ✓   | ✓   | ✓   | ✗   | ✗   | ✗   | ✗   | ✗   | ✗   | ✗   | ✗   | ✗   | ✗   | ✗   | ✗   |

## Expected Invalid Emails

- ✓ = correctly rejected
- ✗ = false positive (incorrectly accepted)

1. `f o o@bar.com` - contains spaces
2. `hi@` - missing domain part
3. `stavros.@stavros.io` - dot at end of local part is invalid
4. `stavros..k@stavros.io` - two dots in sequence in local part
5. `!#$%&'*(-/=?@stavros.io`
6. `h(a)i@stavros.io` - parentheses in name part
7. `em@il@stavros.io` - two at symbols
8. `"<\"@\"".!#%$@stavros.io` - illegal characters
9. `<\"@\\".!#%$@stavros.io` - illegal characters
10. `hi"@"you@stavros.io` - the quotes must be dot-separated
11. `hi\ there@stavros.io` - spaces must be quoted even if escaped
12. `1@23456789` - 23456789 is not a valid TLD

| Library                  | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 10  | 11  | 12  |
| ------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| aftership-email-verifier | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   |
| apache-commons-validator | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✗   | ✓   | ✓   | ✗   | ✓   |
| checkmail                | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✗   |
| deep-email-validator     | ✗   | ✓   | ✗   | ✗   | ✗   | ✗   | ✗   | ✗   | ✗   | ✗   | ✗   | ✓   |
| django-emailvalidator    | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   |
| egulias-email-validator  | ✓   | ✓   | ✓   | ✓   | ✓   | ✗   | ✓   | ✓   | ✓   | ✓   | ✗   | ✗   |
| email-addresses          | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✗   | ✓   | ✓   | ✓   | ✗   |
| email-valid-perl         | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✗   | ✓   | ✓   | ✓   | ✗   |
| email-validator          | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   |
| emailvalidation-dotnet   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   |
| hibernate-validator      | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✗   | ✓   | ✓   | ✓   | ✗   |
| joi                      | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   |
| libvldmail               | ✓   | ✗   | ✓   | ✓   | ✓   | ✓   | ✓   | ✗   | ✓   | ✓   | ✓   | ✗   |
| mailaddress-dotnet       | ✓   | ✓   | ✗   | ✗   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✗   |
| mailkit-dotnet           | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✗   | ✓   | ✓   | ✓   | ✗   |
| net-mail                 | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✗   |
| php-filter-var           | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✗   | ✓   | ✓   | ✓   | ✓   |
| pyisemail                | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✗   |
| python-email-validator   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   |
| rust-email-address       | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✗   |
| symfony-validator        | ✓   | ✓   | ✗   | ✗   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   |
| truemail                 | ✓   | ✓   | ✗   | ✗   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   |
| valid-email2             | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✗   | ✓   | ✗   | ✓   | ✓   |
| validator-js             | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   |
| validator-rust           | ✓   | ✓   | ✗   | ✗   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✗   |
| wordpress-is-email       | ✓   | ✓   | ✗   | ✗   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   |
| zod                      | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   |

## Methodology

You can see the scripts I used for validating Stavros' collection of strings against each library below in the Appendix.
The test harness and complete scripts are in [this Github repo](https://github.com/jonemo/email-validation-olympics).
Please open a PR there if you see issues with any of the test scripts or to add additional libraries.

Full disclosure: I used Claude Code to write most of the test scripts.
I lack time and skill to write all these scripts myself.

For the test harness, the input and output file formats of the test scripts are standardized and intentionally simple:
The input is simply one string to validate per line, the output prefixes each of those input lines with eight characters, either `"valid   "` or `"invalid "`.
This way I avoid unintentional transformations of the string by the test harness.
My first version used comma separated values (CSV) files but quickly realized that CSV parsers and strings with quotes and backslash characters don't mix well.

## The Test Cases

I transcribed the email addresses shown in Stavros' talk, hopefully without typos:

```
hi@stavros.io
hi@
hi+there@stavros.io
stavros.k@stavros.io
stavros.@stavros.io
stavros..k@stavros.io
!#$%&'*(-/=?@stavros.io
f*uck@stavros.io
#$%!^/&@stavros.io
h(a)i@stavros.io
(sta)vros@stavros.io
stavros@stavros.io(io)
em@il@stavros.io
"<\"@\"".!#%$@stavros.io
<\"@\\".!#%$@stavros.io
"hi@you"@stavros.io
"hi you"@stavros.io
" "@stavros.io
hi"@"you@stavros.io
"<\"@\\"".!#%$@stavros.io
hi\ there@stavros.io
cow@[dead::beef]
stavros@io
我買@屋企.香港
1@23456789
1@[23456789]
```

Notes:

- `(sta)vros@stavros.io` - The characters in parentheses are comments according to RFC 5322 (nobody supports them)
- `"hi you"@stavros.io` - Spaces are generally not allowed, but quoted strings allow spaces.
- `cow@[dead::beef]` and `1@[23456789]` - Instead of a domain you are allowed to use an IP addresses (RFC 5321). These two examples happen to be a valid IPv6 address and a valid IPv4 address written in decimal representation, respectively.
- `stavros@io` - TLD-only addresses are technically valid per RFC.
- `我買@屋企.香港` - Internationalized addresses are coverd in RFC 6531. A side effect of this RFC is that emojis and other Unicode characters are allowed in email addresses.

## The Libraries

| Name                         | Repository                                                                            | Package                                                                                 | Language   |
| ---------------------------- | ------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ---------- |
| **validator.js**             | [validatorjs/validator.js](https://github.com/validatorjs/validator.js)               | [NPM](https://www.npmjs.com/package/validator)                                          | JavaScript |
| **deep-email-validator**     | [mfbx9da4/deep-email-validator](https://github.com/mfbx9da4/deep-email-validator)     | [NPM](https://www.npmjs.com/package/deep-email-validator)                               | JavaScript |
| **email-validator**          | [manishsaraan/email-validator](https://github.com/manishsaraan/email-validator)       | [NPM](https://www.npmjs.com/package/email-validator)                                    | JavaScript |
| **Zod**                      | [colinhacks/zod](https://github.com/colinhacks/zod)                                   | [NPM](https://www.npmjs.com/package/zod)                                                | JavaScript |
| **Joi**                      | [hapijs/joi](https://github.com/hapijs/joi)                                           | [NPM](https://www.npmjs.com/package/joi)                                                | JavaScript |
| **email-addresses**          | [jackbearheart/email-addresses](https://github.com/jackbearheart/email-addresses)     | [NPM](https://www.npmjs.com/package/email-addresses)                                    | JavaScript |
| **python-email-validator**   | [JoshData/python-email-validator](https://github.com/JoshData/python-email-validator) | [PyPI](https://pypi.org/project/email-validator/)                                       | Python     |
| **pyIsEmail**                | [michaelherold/pyIsEmail](https://github.com/michaelherold/pyIsEmail)                 | [PyPI](https://pypi.org/project/pyIsEmail/)                                             | Python     |
| **Django EmailValidator**    | [django/django](https://github.com/django/django)                                     | [PyPI](https://pypi.org/project/Django/)                                                | Python     |
| **PHP** `filter_var()`       | N/A                                                                                   | N/A                                                                                     | PHP        |
| **EmailValidator**           | [egulias/EmailValidator](https://github.com/egulias/EmailValidator)                   | [Packagist](https://packagist.org/packages/egulias/email-validator)                     | PHP        |
| **WordPress**                | [WordPress/WordPress](https://github.com/WordPress/WordPress)                         | N/A                                                                                     | PHP        |
| **Symfony Validator**        | [symfony/validator](https://github.com/symfony/validator)                             | [Packagist](https://packagist.org/packages/symfony/validator)                           | PHP        |
| **Apache Commons Validator** | [apache/commons-validator](https://github.com/apache/commons-validator)               |                                                                                         | Java       |
| **Hibernate Validator**      | [hibernate/hibernate-validator](https://github.com/hibernate/hibernate-validator)     | [Maven](https://mvnrepository.com/artifact/org.hibernate.validator/hibernate-validator) | Java       |
| **AfterShip/email-verifier** | [AfterShip/email-verifier](https://github.com/AfterShip/email-verifier)               |                                                                                         | Go         |
| **net/mail**                 | [golang/go](https://github.com/golang/go)                                             | [pkg.go.dev](https://pkg.go.dev/net/mail)                                               | Go         |
| **checkmail**                | [badoux/checkmail](https://github.com/badoux/checkmail)                               | [pkg.go.dev](https://pkg.go.dev/github.com/badoux/checkmail)                            | Go         |
| **truemail**                 | [truemail-rb/truemail](https://github.com/truemail-rb/truemail)                       |                                                                                         | Ruby       |
| **valid_email2**             | [micke/valid_email2](https://github.com/micke/valid_email2)                           |                                                                                         | Ruby       |
| **MailAddress**              | [dotnet/runtime](https://github.com/dotnet/runtime)                                   | N/A                                                                                     | .NET       |
| **EmailValidation**          | [jstedfast/EmailValidation](https://github.com/jstedfast/EmailValidation)             | [NuGet](https://www.nuget.org/packages/EmailValidation/)                                | .NET       |
| **MailKit**                  | [jstedfast/MailKit](https://github.com/jstedfast/MailKit)                             | [NuGet](https://www.nuget.org/packages/MailKit)                                         | .NET       |
| **email_address**            | [johnstonskj/rust-email_address](https://github.com/johnstonskj/rust-email_address)   | [crates.io](https://crates.io/crates/email_address)                                     | Rust       |
| **validator**                | [Keats/validator](https://github.com/Keats/validator)                                 | [crates.io](https://crates.io/crates/validator)                                         | Rust       |
| **Email::Valid**             | [Perl-Email-Project/Email-Valid](https://github.com/Perl-Email-Project/Email-Valid)   | [CPAN](https://metacpan.org/pod/Email::Valid)                                           | Perl       |
| **libvldmail**               | [dertuxmalwieder/libvldmail](https://github.com/dertuxmalwieder/libvldmail)           | N/A                                                                                     | C          |

### validator.js

- Github: https://github.com/validatorjs/validator.js
- NPM: https://www.npmjs.com/package/validator
- Version tested: 13.15.26 (published December 2025)
- [Test code](https://github.com/jonemo/email-validation-olympics/tree/main/libraries/validator-js)

A library of string validators and sanitizers for JavaScript with over 23,000 Github stars.
Provides an `isEmail()` function with configurable options for allowing display names, UTF-8 local parts, and more.

```js
import isEmail from 'validator/lib/isEmail'

validator.isEmail('foo@bar.com', { allow_ip_domain: true })
```

By default, IP addresses in the domain part are rejected. For an accurate comparison with the test cases, the `allow_ip_domain` option is enabled.

Configuration options:

- `allow_display_name` - Allow display names like `Name <email@example.com>`. Default: `false`.
- `require_display_name` - Require a display name. Default: `false`.
- `allow_utf8_local_part` - Allow UTF-8 characters in the local part. Default: `true`.
- `allow_ip_domain` - Allow IP addresses in the domain part. Default: `false`.
- `domain_specific_validation` - Extra validation for Gmail addresses. Default: `false`.
- `blacklisted_chars` - String of characters not allowed in the local part.

### email-validator (Javascript)

- Github: https://github.com/manishsaraan/email-validator
- NPM: https://npmjs.com/package/email-validator
- Version tested: 2.0.4 (published May 2018)
- [Test code](https://github.com/jonemo/email-validation-olympics/tree/main/libraries/email-validator)

The second most downloaded email validation library on NPM, by a wide margin, behind validator.js.
Advertised as "a simple module", and simple it is:
The entire library is 33 lines of code in a single file, plus 100 lines of tests.
Within those 33 lines is no room for parameters or config options.
The last update was pushed in 2018, which some may call "abandoned" and others "finished".

```js
const validator = require('email-validator')

validator.validate('foo@bar.com') // true
```

The library correctly rejects all of Stavros' invalid test cases, as well as 10 out of 16 valid test cases.

### email-addresses (Javascript)

- Github: https://github.com/jackbearheart/email-addresses
- NPM: https://www.npmjs.com/package/email-addresses
- Version tested: 5.0.0 (published November 2020)
- [Test code](https://github.com/jonemo/email-validation-olympics/tree/main/libraries/email-addresses)

Neck to neck with email-validator in terms of downloads, but quite different in terms of LOC:
This one has 1098 lines of code plus a couple of hundred lines of test coverage.

The library is implements as a recursive decent parser for the grammar specified in RFC 5322.
This means that for any valid email address, this library yields a AST of the components that match definitions in the RFC which you can query individually.

For the test script I used `parseOneAddress()` which returns null for invalid addresses.

An RFC 5322 email address parser that handles full email address formats including display names and comments. For validating just the address portion (RFC 5321), the documentation recommends using node-address-rfc2821 instead.

```js
const addrs = require('email-addresses')

// Returns address object if valid, null if invalid
const parsed = addrs.parseOneAddress('test@example.com')
parsed.local // => test
parsed.domain // => example.com

// Or use addrs() to get access to the AST
const parsed2 = addrs('test@example.com')
parsed.ast.children // => tree object
```

There are a few configuration options, all of which I kept the default values for:

- `rfc6532` enables Unicode support. Warning: Depending on which function you use, the default value changes.
- `strict` turns off features of RFC 5322 marked "Obsolete".
- `rejectTLD` requires at least one dot in the domain part. This one was tricky: Enabling it would have removed one false positive from the results but added a false negative.

The strict adherence to RFC 5322 means that email-addresses supports display names (`"Display Name" <display.name@gmail.com>`) which Stavros examples don't cover.
The docs recommend [node-address-rfc2821](https://www.npmjs.com/package/address-rfc2821) as a similar parser implementation for just the address part.
A future version of this post should include that one, I saw the reference too late to include it this time around.

### deep-email-validator (Javascript, Node.js only)

- Github: https://github.com/mfbx9da4/deep-email-validator
- NPM: https://npmjs.com/package/deep-email-validator
- Version tested: 0.1.21 (published December 2021)
- [Test code](https://github.com/jonemo/email-validation-olympics/tree/main/libraries/deep-email-validator)

The "deep" in the name refers to the list of features beyond validation: Typos, disposable check, DNS lookup, and SMTP.

```js
import validate from 'deep-email-validator'

const main = async () => {
  await validate({
    email: 'name@example.org',
    sender: 'name@example.org',
    validateRegex: true,
    validateMx: true,
    validateTypo: true,
    validateDisposable: true,
    validateSMTP: true,
  })
}
```

The validation part is rather simple:

> Validates email looks like an email i.e. contains an "@" and a "." to the right of it.

Ironically this is still more strict than Stavro's suggested method because the requirement for a "." rules out top level domains, for example "lewis@[ferrari](https://icannwiki.org/.ferrari)". Using top-level domains like that has been banned by ICANN since 2013, so maybe not a big deal.

deep-email-validator was last updated in 2021. I include it here as an example for the deep bench of [email validation packages on NPM](https://www.npmjs.com/search?q=keywords:email-validation) that gained modest traction by Github stars and downloads.

Note that deep-email-validator is Node.js only Javascript, so no good for your web form.

### Zod (Javascript)

- Github: https://github.com/colinhacks/zod
- NPM: https://www.npmjs.com/package/zod
- Version tested: 4.3.5 (published January 2026)
- [Test code](https://github.com/jonemo/email-validation-olympics/tree/main/libraries/zod)

Zod is a Javascript object validation library that has a [field type for email addresses](https://zod.dev/api#emails):

```js
import { z } from 'zod'

z.string().email()
```

Zod intentionally does not support many RFC-compliant but unusual email formats.
For example: No comments, no quotes, no IP addresses, no emojis.
From their docs:

> By default, Zod uses a comparatively strict email regex designed to validate normal email addresses containing common characters.
> It's roughly equivalent to the rules enforced by Gmail.
> To learn more about this regex, refer to [this post](https://colinhacks.com/essays/reasonable-email-regex).
>
> ```
> /^(?!\.)(?!.*\.\.)([a-z0-9_'+\-\.]*)[a-z0-9_+-]@([a-z0-9][a-z0-9\-]*\.)+[a-z]{2,}$/i
> ```

The library also bundles a handful of alternative email regexes and allows you to bring your own.

### Joi (Javascript)

- Github: https://github.com/hapijs/joi
- NPM: https://www.npmjs.com/package/joi
- Version tested: 18.0.2 (published November 2025)
- [Test code](https://github.com/jonemo/email-validation-olympics/tree/main/libraries/joi)

[Joi](https://joi.dev) is another Javascript validation library that includes a [field type for email addresses](https://joi.dev/api/?v=17.13.3#stringemailoptions):

```js
const Joi = require('joi')

const schema = Joi.string().email()
```

The documentation mentions one edge case:

> Note that quoted email addresses (e.g. "test"@example.com) are not supported and will fail validation.

These config options exist:

- `allowFullyQualified` - if true, domains ending with a . character are permitted. Defaults to false.
- `allowUnicode` - if true, Unicode characters are permitted. Defaults to true.
- `ignoreLength` - if true, ignore invalid email length errors. Defaults to false.
- `minDomainSegments` - number of segments required for the domain. The default setting excludes single segment domains such as example@io which is a valid email but very uncommon. Defaults to 2.
- `maxDomainSegments` - maximum number of allowed domain segments. Default to no limit.
- `tlds` - options for TLD (top level domain) validation. By default, the TLD must be a valid name listed on the IANA registry. To disable validation, set tlds to false.

### python-email-validator

- Github: https://github.com/JoshData/python-email-validator
- PyPI: https://pypi.org/project/email-validator/
- Version tested: 2.3.0 (published August 2025)
- [Test code](https://github.com/jonemo/email-validation-olympics/tree/main/libraries/python-email-validator)

This is currently the most popular option for Python with 20 million weekly PyPI downloads.
[Pydantic uses it](https://docs.pydantic.dev/latest/api/networks/#pydantic.networks.EmailStr) for its `EmailStr` field type.

```python
from email_validator import validate_email, EmailNotValidError

try:
    emailinfo = validate_email(
        "my+address@example.org",
        check_deliverability=False,
        allow_quoted_local=True,
        allow_domain_literal=True,
    )
except EmailNotValidError as e:
    print(str(e))  # Prints a human-readable explanation.
```

The default settings allow UTF-8 and verifies with a DNS check, but disallow quotes and IP addresses.
I enable the default-off flags for a fair comparison against Stavros' examples.

The Readme declares:

> This is an opinionated library. You should definitely also consider using the less-opinionated pyIsEmail if it works better for you.

In the test, python-email-validator rejects all invalid test cases and 6 valid ones, validating the "opinionated" statement.

By the way, while the test script ignores the validation failure messages, you should not. They are quite specific:

- `f o o@bar.com` → "The email address contains invalid characters before the @-sign: SPACE"
- `stavros.@stavros.io` → "An email address cannot have a period immediately before the @-sign"
- `stavros..k@stavros.io` → "An email address cannot have two periods in a row"
- `em@il@stavros.io` → "The part after the @-sign contains invalid characters: '@'"
- `hi\ there@stavros.io` → "The email address contains invalid characters before the @-sign: "\", SPACE"

### pyIsEmail (Python)

- Github: https://github.com/michaelherold/pyIsEmail
- PyPI: https://pypi.org/project/pyIsEmail/
- Version tested: 2.0.1 (published 2018)
- [Test code](https://github.com/jonemo/email-validation-olympics/tree/main/libraries/pyisemail)

A Python port of [the `is_email` PHP library](https://github.com/dominicsayers/isemail) (which is not covered again in this blog post).
Provides detailed diagnostic information when validation fails.

```python
from pyisemail import is_email

address = "test@example.com"
bool_result = is_email(address)
detailed_result = is_email(address, diagnose=True)
```

Configuration options:

- `check_dns` - Validate that the domain has MX records. Default: `False`.
- `diagnose` - Return detailed diagnostic information instead of a boolean. Default: `False`.

### Django EmailValidator (Python)

- Github: https://github.com/django/django
- PyPI: https://pypi.org/project/Django/
- Docs: https://docs.djangoproject.com/en/6.0/ref/validators/#django.core.validators.EmailValidator
- Version tested: 5.2.10 (published January 2026)
- [Test code](https://github.com/jonemo/email-validation-olympics/tree/main/libraries/django-emailvalidator)

Django's built-in email validator is used throughout the framework for model fields and form validation. It's one of the most widely deployed email validators given Django's popularity in Python web development.

```python
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError

validator = EmailValidator()
try:
    validator("test@example.com")
    # Valid
except ValidationError:
    # Invalid
```

The validator uses a regex-based approach that aims to match the HTML5 email input specification while allowing some RFC 5322 edge cases. It's designed to be practical for web forms rather than strictly RFC-compliant.

Configuration options:

- `allowlist` - Allowlist of domains (e.g., `['example.com']`). Only these domains will be accepted.
- `message` - Custom error message for validation failures.
- `code` - Custom error code for validation failures.

Django requires minimal settings configuration to use the validator standalone (outside of a Django project).

### PHP Standard Library

- Version tested: 8.3.30 (published January 2026)
- [Test code](https://github.com/jonemo/email-validation-olympics/tree/main/libraries/php-filter-var)

PHP has an email validator built into the standard library:

```php
filter_var($email, FILTER_VALIDATE_EMAIL)
```

It's not easily discovered in [the documentation](https://www.php.net/manual/en/function.filter-var.php) because it is a flag to the more general `filter_var` function.
There are no configuration options available.

The PHP docs advertise RFC 5321 compliance.
But the PHP docs also allow for comments to be posted under each page.
Naturally there are comments pointing out deviations from the standard, including [this highly upvoted one from 2013](https://www.php.net/manual/en/function.filter-var.php#112492).

The test results suggest that PHP is overly strict about the local part of the email and quite flexible about the domain part:
It accepts the IPv6 address and the naked TLD (both correct per RFC) but also the numbers-only domain (incorrect).

### WordPress (PHP)

- Github: https://github.com/WordPress/WordPress
- Version tested: 6.9 (published January 2026)
- [Test code](https://github.com/jonemo/email-validation-olympics/tree/main/libraries/wordpress-is-email)

The [`is_email()`](https://developer.wordpress.org/reference/functions/is_email/) function is WordPress's built-in email validator.
WordPress powers over 40% of websites, this is likely one of the most widely executed email validation functions in existence.

Because Wordpress' internal functions aren't normally used as a library, for my test I copied the `is_email` source code from [wp-includes/formatting.php](https://github.com/WordPress/WordPress/blob/master/wp-includes/formatting.php). Then the usage becomes trivial:

```php
$result = is_email($email);  // returns email if valid, false otherwise
```

The function performs these checks:

- Minimum length of 6 characters
- Must contain `@` after the first position
- Local part: only allows `a-z0-9!#$%&'*+/=?^_`{|}~.-`
- Domain: must have at least two parts, each containing only `a-z0-9-`
- No leading/trailing hyphens or whitespace in domain parts

The docs are refreshingly honest about its limitations:

> "Does not grok i18n domains." [...] "Not RFC compliant."

The test results confirm this: The function rejects all the theoreticaly valid but unusual strings and slips up only on the two invalid cases that contain dots in the wrong places.

No configuration options available.

### Symfony Validator (PHP)

- Github: https://github.com/symfony/validator
- Version tested: 7.4.3 (published December 2025)
- [Test code](https://github.com/jonemo/email-validation-olympics/tree/main/libraries/symfony-validator)

Symfony's Validator component provides an `Email` constraint with multiple validation modes.
In `strict` mode, it uses [egulias/EmailValidator](https://github.com/egulias/EmailValidator).
The default mode is `VALIDATION_MODE_HTML5` and uses a regex that you can see in [this file](https://github.com/symfony/validator/blob/c65aa0495769dd03d2c094f784545dc202c2b675/Constraints/EmailValidator.php#L12).

```php
use Symfony\Component\Validator\Constraints\Email;
use Symfony\Component\Validator\Validation;

$validator = Validation::createValidator();
$constraint = new Email(['mode' => Email::VALIDATION_MODE_HTML5]);
$violations = $validator->validate($email, $constraint);
```

Configuration options:

- `VALIDATION_MODE_HTML5` - Uses the HTML5 regex pattern (default). Good for web forms.
- `VALIDATION_MODE_STRICT` - Uses egulias/EmailValidator for strict RFC compliance. Requires `egulias/email-validator` to be installed.

### EmailValidator (PHP)

- Github: https://github.com/egulias/EmailValidator
- Version tested: 4.0.4 (published March 2025)
- [Test code](https://github.com/jonemo/email-validation-olympics/tree/main/libraries/egulias-email-validator)

The most comprehensive PHP validator with multiple validation strategies.
Supports strict RFC 5321/5322 compliance and can warn about technically-valid-but-unusual addresses that you may want to reject in practice.

```php
use Egulias\EmailValidator\EmailValidator;
use Egulias\EmailValidator\Validation\RFCValidation;

$validator = new EmailValidator();
$validator->isValid("example@example.com", new RFCValidation());
```

**Validation strategies:**

- `RFCValidation` - Validates according to RFC 5321/5322 (used for this comparison).
- `NoRFCWarningsValidation` - Fails on RFC warnings (stricter than RFCValidation).
- `DNSCheckValidation` - Checks if the domain has valid DNS records.
- `SpoofCheckValidation` - Detects spoofing attempts using similar-looking characters.

### Apache Commons Validator (Java)

- Github: https://github.com/apache/commons-validator
- Maven: https://mvnrepository.com/artifact/commons-validator/commons-validator
- Version tested: 1.10.1 (published November 2025)
- [Test code](https://github.com/jonemo/email-validation-olympics/tree/main/libraries/apache-commons-validator)

Part of the Apache Commons project.
Provides an `EmailValidator` [class](https://github.com/apache/commons-validator/blob/43ff9695d7bb4ca8d7ac2284d209e0bfd84b61a3/src/main/java/org/apache/commons/validator/routines/EmailValidator.java#L35) that can be configured to allow local addresses and TLDs.

```java
import org.apache.commons.validator.routines.EmailValidator;

EmailValidator validator = EmailValidator.getInstance();
boolean isValid = validator.isValid("test@example.com");
```

Configuration options:

- `getInstance()` - Default instance, no local addresses or TLD-only domains.
- `getInstance(allowLocal)` - Allow local addresses (e.g., `user@localhost`).
- `getInstance(allowLocal, allowTld)` - Also allow TLD-only domains (e.g., `user@io`).

The docs are [here](https://commons.apache.org/proper/commons-validator/apidocs/org/apache/commons/validator/routines/EmailValidator.html).

This code is nearly 20 years old and references a long-gone website https://javascript.internet.com as inspiration, and it's still [getting polished](https://github.com/apache/commons-validator/commit/c8d4a8f6270f7714a0cac0a5ea82c7a39bbd5940) today.

### Hibernate Validator (Java)

- Github: https://github.com/hibernate/hibernate-validator
- Maven: https://mvnrepository.com/artifact/org.hibernate.validator/hibernate-validator
- Version tested: 9.1.0.Final (published November 2025)
- [Test code](https://github.com/jonemo/email-validation-olympics/tree/main/libraries/hibernate-validator)

I am way out of my depth on this, but Claude asked me to tell you:

> This is the reference implementation of Jakarta Bean Validation (formerly JSR 380).
> Provides the `@Email` annotation for declarative validation.
> Widely used in Spring Boot and Jakarta EE applications.

To keep the test script minimal, ~I use~ Claude uses `validateValue()` to validate the strings directly without creating full bean instances:

```java
import jakarta.validation.constraints.Email;

public class EmailWrapper {
    @Email
    private String email;
}

// Validate using:
validator.validateValue(EmailWrapper.class, "email", emailString);
```

No configuration options available for the basic `@Email` annotation.

### Go net/mail (Standard Library)

- pkg.go.dev: https://pkg.go.dev/net/mail
- Version tested: 1.23 (published August 2024)
- [Test code](https://github.com/jonemo/email-validation-olympics/tree/main/libraries/net-mail)

Go's standard library `net/mail` package provides RFC 5322 email address parsing via `mail.ParseAddress()`.

This is a parser rather than a dedicated validator, so it may accept some unusual but technically valid RFC 5322 addresses.

```go
import "net/mail"

_, err := mail.ParseAddress("test@example.com")
if err == nil {
    // Valid
}
```

No configuration options available.

### checkmail (Go)

- Github: https://github.com/badoux/checkmail
- Version tested: 1.2.4 (published January 2024)
- [Test code](https://github.com/jonemo/email-validation-olympics/tree/main/libraries/checkmail)

127 lines of Go that cover format validation, DNS lookup, and verification with SMTP.

For the test I call `ValidateFormat()` which performs syntax validation using a simple regexp based on the W3C HTML5 email specification:

```go
import "github.com/badoux/checkmail"

err := checkmail.ValidateFormat("test@example.com")
if err == nil {
    // Valid format
}
```

**Available functions:**

- `ValidateFormat()` - Syntax validation only (used for this comparison).
- `ValidateHost()` - Validates format + checks DNS MX records.
- `ValidateHostAndUser()` - Validates format + DNS + verifies mailbox via SMTP.

The library intentionally uses a simple validation approach. From its documentation:

> Format (simple regexp, see: https://www.w3.org/TR/html5/forms.html#valid-e-mail-address and https://davidcel.is/posts/stop-validating-email-addresses-with-regex/)

### email-verifier (Go)

- Github: https://github.com/AfterShip/email-verifier
- Version tested: 1.4.1 (published September 2024)
- [Test code](https://github.com/jonemo/email-validation-olympics/tree/main/libraries/aftership-email-verifier)

A full-featured Go library that supports syntax validation, MX lookup, SMTP verification, disposable email detection, and typo suggestions.
For this comparison, I disabled all verification features and only tested syntax validation via `ret.Syntax.Valid`.

```go
import emailverifier "github.com/AfterShip/email-verifier"

verifier := emailverifier.NewVerifier().
    DisableSMTPCheck().
    DisableDomainSuggest().
    DisableAutoUpdateDisposable()

ret, _ := verifier.Verify("test@example.com")
isValid := ret != nil && ret.Syntax.Valid
```

Configuration options:

- `.DisableSMTPCheck()` - Disable SMTP verification.
- `.DisableDomainSuggest()` - Disable typo suggestions.
- `.DisableAutoUpdateDisposable()` - Disable auto-updating disposable email list.

### truemail (Ruby)

- Github: https://github.com/truemail-rb/truemail
- Rubygems: https://rubygems.org/gems/truemail
- Version tested: 3.3.1 (published April 2024)
- [Test code](https://github.com/jonemo/email-validation-olympics/tree/main/libraries/truemail)

truemail offers the full menu of checks: Domain allow/deny lists, regex (the part we care about here), DNS check, SMTP check.

> By default this validation not performs strictly following RFC 5322 standard, so you can override Truemail default regex pattern if you want.

To run syntax validation only:

```rb
require 'truemail'

Truemail.configure do |config|
  config.verifier_email = 'verifier@example.com'
  config.default_validation_type = :regex  # syntax-only, no DNS/SMTP
end

def valid?(email)
  Truemail.valid?(email)
end
```

To use a custom regex:

```rb
Truemail.configure do |config|
  config.verifier_email = 'verifier@example.com'
  config.default_validation_type = :regex  # syntax-only, no DNS/SMTP
  config.email_pattern = /regex_pattern/  # <-- your custom regex here
end
```

To add allow list or deny list checking:

```rb
Truemail.configure do |config|
  config.verifier_email = 'verifier@example.com'
  config.default_validation_type = :regex  # syntax-only, no DNS/SMTP
  config.whitelist_validation=true
  config.whitelisted_domains=['stavros.io']
  config.blacklist_validation=true
  config.blacklisted_domains=['jonasneubert.com']
```

You can also provide a list of allowed or denied emails in `whitelisted_emails` and `blacklisted_emails`.
But if you do that, then why use a validation library at all?

[truemail-go](https://github.com/truemail-rb/truemail-go) is a Go port of the truemail's syntax validation features only.
Both Ruby original and Go port received their most recent commit in 2024.

### valid_email2 (Ruby)

- Github: https://github.com/micke/valid_email2
- Rubygems: https://rubygems.org/gems/valid_email2
- Version tested: 7.0.13 (published May 2025)
- [Test code](https://github.com/jonemo/email-validation-olympics/tree/main/libraries/valid-email2)

This is widely used in Rails applications because it integrates with [ActiveModel](https://guides.rubyonrails.org/active_model_basics.html), Rails' system for object validation. It's probably the most common choice in the Ruby ecosystem.

```ruby
require 'valid_email2'

email = ValidEmail2::Address.new("test@example.com")
email.valid?  # true
```

The validation process is not configurable.
Use `.valid_mx?`, `.disposable?`, `.blacklisted?` for the other checks offered by the library.

### System.Net.Mail.MailAddress (.NET Standard Library)

- GitHub: https://github.com/dotnet/runtime
- Version tested: .NET 8.0
- [Test code](https://github.com/jonemo/email-validation-olympics/tree/main/libraries/mailaddress-dotnet)

.NET's built-in email address parser.
As is typical for .NET, the [documentation](https://learn.microsoft.com/en-us/dotnet/api/system.net.mail.mailaddress?view=net-10.0) goes into detail about what is and what isn't supported.
One interesting detail:

> .NET 9 and earlier ONLY: Consecutive and trailing dots in user names. For example, `user...name..@host`. (Starting in .NET 10, consecutive dots aren't allowed.)

```csharp
using System.Net.Mail;

try {
    var addr = new MailAddress(email);
    bool isValid = addr.Address == email;
} catch {
    // Invalid
}
```

Note that MailAddress also accepts "Display Name <email>" format, so validation should verify that `Address` matches the original input to ensure that part of your input string wasn't interpreted as display name.

No configuration options available.

### EmailValidation (.NET)

- Github: https://github.com/jstedfast/EmailValidation
- NuGet: https://www.nuget.org/packages/EmailValidation/
- Version tested: 1.3.0 (published March 2025)
- [Test code](https://github.com/jonemo/email-validation-olympics/tree/main/libraries/emailvalidation-dotnet)

Simple, correct .NET validator with RFC 6531 (internationalized) support. Written by Jeffrey Stedfast, who also authored MailKit.

```csharp
using EmailValidation;

bool isValid = EmailValidator.Validate("test@example.com");
```

No configuration options available.

### MailKit (.NET)

- Github: https://github.com/jstedfast/MailKit
- NuGet: https://www.nuget.org/packages/MailKit
- Version tested: 4.10.0 (published January 2025)
- [Test code](https://github.com/jonemo/email-validation-olympics/tree/main/libraries/mailkit-dotnet)

MailKit is a cross-platform mail client library for .NET, written by Jeffrey Stedfast (who also wrote EmailValidation). While primarily an IMAP/SMTP client, it includes email address parsing via `MailboxAddress.TryParse()` from the MimeKit dependency.

```csharp
using MimeKit;

bool isValid = MailboxAddress.TryParse("test@example.com", out var _);
```

The validation behavior differs slightly from EmailValidation because MailKit's parser is designed for real-world email handling rather than strict validation.

No configuration options available.

### email_address (Rust)

- Github: https://github.com/johnstonskj/rust-email_address
- crates.io: https://crates.io/crates/email_address
- Version tested: 0.2.9 (published July 2024)
- [Test code](https://github.com/jonemo/email-validation-olympics/tree/main/libraries/rust-email-address)

A Rust [newtype](https://doc.rust-lang.org/rust-by-example/generics/new_types.html) for email address strings.
The docs claim RFC 5322 compliance and support for UTF-8 addresses.

```rust
use email_address::EmailAddress;

let is_valid = EmailAddress::is_valid("test@example.com");
```

No configuration options available.

Among our contenders its performance against the Stavros test suite is among the top 4, in part because it does not allow for comments in the address.

### validator (Rust)

- Github: https://github.com/Keats/validator
- crates.io: https://crates.io/crates/validator
- Version tested: 0.20.0 (published January 2025)
- [Test code](https://github.com/jonemo/email-validation-olympics/tree/main/libraries/validator-rust)

Comprehensive validation library for Rust, akin to Zod in Node and Pydantic in Python.
Validates email addresses based on the HTML5 spec rather than RFC 5322.

```rust
use validator::ValidateEmail;

fn validate(email: &str) -> bool {
    email.validate_email()
}
```

No configuration options available for email validation.

### Email::Valid (Perl)

- Github: https://github.com/Perl-Email-Project/Email-Valid
- CPAN: https://metacpan.org/pod/Email::Valid
- Version tested: 1.204 (published January 2024)
- [Test code](https://github.com/jonemo/email-validation-olympics/tree/main/libraries/email-valid-perl)

The closest I've ever come to Perl is as a marketing (sic) intern at Nestoria where I was sitting next to some Perl wizards.
Lacking first hand knowledge I have no choice but to believe the Google wisdom that this library with 18 Github stars is indeed the premier Perl solution for email validation.

The syntax of the basic usage example looks Perlish indeed:

```perl
use Email::Valid;

my $email = 'example@domain.com';
my $valid = Email::Valid->address(-address => $email, -fqdn => 0);
print $valid ? "Valid email" : "Invalid email";
```

Of the config parameters mentioned in the docs, two are relevant to our test cases:

- `allow_ip` defaults to true and allows for IP addresses for the domain part. Sadly, the library still fails the two IP address examples which are an IPv6 and a decimal format IPv4.
- `fqdn` defaults to true and requires the domain part to be fully qualified. For a fair comparison with other libraries, I set `-fqdn => 0` to allow single-segment domains like `stavros@io`, which are technically valid per RFC standards.

### libvldmail (C)

- Github: https://github.com/dertuxmalwieder/libvldmail
- Version tested: git master (latest commit November 2025)
- [Test code](https://github.com/jonemo/email-validation-olympics/tree/main/libraries/libvldmail)

A C library for email syntax validation only.
Follows RFC 6531 by default with fallback to RFC 5321.

```c
#include <vldmail.h>

valid_mail_t validator = validate_email(L"foo@bar.com");
if (validator.success != 0) {
    // Valid
}
```

Two configuration options are available:

- `NO_UNICODE_MAIL_PLEASE` - A very polity flag for restricting validation to ASCII characters only.
- `STRICT_VALIDATION` - Apply stricter RFC standards, marking deprecated formats as invalid.

Overall, libvldmail does quite well on Stavros' test cases.
It's the only library that lets the `hi@` example slip through as valid, something I'd consider a bug.

## Other Options not Reviewed

- **pydantic** because it delegates email validation to python-email-validator.
- [**skeggse/isemail**](https://github.com/skeggse/isemail) because it is no longer maintained. Just like `pyIsEmail`, it is a port of the [`is_email` PHP library](https://github.com/dominicsayers/isemail).
- [**go-mail**](https://github.com/wneessen/go-mail) because it delegates email validation to Go's standard library `net/mail`. Note: The naming history is confusing - go-gomail/gomail was the original (~2016), go-mail/mail was a fork (~2019), and wneessen/go-mail is the currently maintained version (2022+).
- [**Mailchecker**](https://github.com/FGRibreau/mailchecker) is a cross-language library that primarily compares an email address against a list of disposable email address providers. It also offers validation and defers this to PHP's `filter_var` and to the regex from **validator.js** for all other languages.
- [**mailcheck.js**](https://github.com/mailcheck/mailcheck)) because it is not a full validator, it finds domain misspellings for a fixed list of domains. And because it's been unmaintained for 10 years, after a successful run as jQuery plugin.
- Libraries that send each email address to an API, for example [email-verifier](https://www.npmjs.com/package/email-verifier).

## Further Reading

- [Falsehoods about Email](https://beesbuzz.biz/code/439-Falsehoods-programmers-believe-about-email)
- [I Knew How to Validate an Email Address Until I Read the RFC](https://haacked.com/archive/2007/08/21/i-knew-how-to-validate-an-email-address-until-i.aspx/)
- [Your E-Mail Validation Logic is Wrong](https://www.netmeister.org/blog/email.html)
