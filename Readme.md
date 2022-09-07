# blog.jonasneubert.com

## Requirements

| Requirement | Install instructions |
| --- | --- |
| Hugo | https://gohugo.io/getting-started/installing/ |
| node | https://github.com/nvm-sh/nvm#installing-and-updating |
| yarn | `corepack enable` |


## Build CSS using Tailwind

```sh
yarn install
yarn build-tw  # creates assets/css/style.css from main.css
```

## Run Hug

Create `/public` directory:

```sh
hugo --minify
```

Hugo dev server, watches for changes and serves on localhost:1313:

```sh
hugo server
```
