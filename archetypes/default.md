---
date: {{ .Date }}
draft: true
title: "{{ substr (replace .TranslationBaseName "-" " ") 11 | title }}"
slug: "{{ substr (.TranslationBaseName) 11 }}"
---

