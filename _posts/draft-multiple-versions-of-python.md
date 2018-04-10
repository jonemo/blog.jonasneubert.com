---
layout: post
title: "How to install multiple version of Python on a Mac"
tags:
 - python
published: false
date: Dec 31, 2099
---

It is occasionally necessary to have multiple versions of Python installed on the same operating system. Pythonistas who use Python 3 daily might need to work on a legacy app written in Python 2. Others who still use Python 2 daily might want to update a project. Or maybe your team has agreed to use Python 3.6.0 but you really want to try out the [new syntax for default values in `NamedTuple`](https://docs.python.org/3/library/typing.html#typing.NamedTuple) added in Python 3.6.1.

For me these situations usually come up on my personal development machine (a hand-me-down 2013 MacBook Pro running macOS 10.12) which I use for working on many different projects. I'm also quick to try out new tools on this laptop, which has led me to "break" my Python installs more than once, often because of using two incompatible mechanisms for managing multiple Pythons.

This weekend I decided to once and for all investigate the options and write down my findings for future reference.


## Python Versions 101

First, a few bullet points to illustrate why this topic is confusing:

 * macOS 10.12 comes with Python `2.7.10` installed by default, at `/usr/bin/python`.
 * The current latest stable versions are Python `3.6.5` and `2.7.14`.[^latest-versions]
 * Using the Python installation that comes with the operating system is discouraged because any (intentional or inadvertent) changes to it could affect operating system behavior.
 * What gets executed when you type `python` into your command line prompt is (mostly) determined by the value of the `$PATH` environment variable.[^path-evn]
 * `which python` tells you the full path to the executable that is known as `python` given the value of `$PATH`in your current environment.[^which-links]
 * `/path/to/python --version` tells you the Python version of any Python executable.
 * You probably want to use `pip` which comes bundled with all recent Python versions but not older ones. Luckily every recent version of pip works with almost every version of Python.
 * If you have multiple versions of Python installed, you likely also have multiple installations of pip. The `pip` found on your current `$PATH` might or might not be the one that came with the `python` on your current `$PATH`.
 * The previous point matters when `pip install`-ing packages that dropped support for Python 2. For example: `pip install ipython` will install iPython 5.x when under Python 2, and iPython 6.x when under Python 3.
 * Further, you have to make sure that `pip install` places the packages in the `site-packages` folder that the install of Python you wish to use looks for them in.
 * However, you'll want to make sure that different Python installs do not share the same `site-packages` folder or else there is a risk of Python installations .
 * Finally, some packages contain executables, for example `pip install ipython` installs the `ipython` package and a command line tool (also called `ipython`). Whether the `ipython` found on your current `$PATH` is the one that you installed using the `pip` on your current `$PATH` and is compatible with the `python` on your current `$PATH` or not -- who knows?

Most of the potential pitfalls mentioned above come down to being aware what your `$PATH` is set to and what's on it. Using `virtualenv` will auto-magically manage this for you and almost always makes sense to use for isolating projects from each other, even when those projects use the same version of Python.

But how do you know which `virtualenv` is on your `$PATH` and which Python it will use as default? Ok, at this point I'm just trolling. Let's look at options for installing multiple Pythons on a Mac now.


## Option 1: brew

### brew conceptually

My first order of business with any new Mac is to install the [brew](https://brew.sh/)[^brew-terminology] package manager for Mac.

To use brew, you add `/usr/local/bin` to your path, and brew places symlinks to all the right things into this folder. The default brew "tap" (package repository) treats Python 2.7 and Python 3 as separate packages named [`python2`](http://formulae.brew.sh/formula/python3) and [`python3`](http://formulae.brew.sh/formula/python3) respectively.[^brew-python-2-3]

## brew practically

To install the latest stable Python 3.x.x, run:

```sh
$ brew install python3
```

You will now find a symlink at `/usr/local/bin/python3` that points to `/usr/local/Cellar/python3/3.6.3/bin/python3`. A couple of related executables came along for the ride and are also symlinked in `/urs/local/bin`:

```sh
$ ls /usr/local/Cellar/python3/3.6.3/bin/
2to3-3.6.           pydoc3.             python3.6m
easy_install-3.6.   pydoc3.6            python3.6m-config
idle3               python3             pyvenv
idle3.6.            python3-config      pyvenv-3.6
pip3                python3.6           wheel3
pip3.6              python3.6-config
```

Any packages installed with `pip3 install ...` end up in `/usr/local/lib/python3.6/site-packages`. Why there and how does Python know to look there? Like other package repositories, brew modifies the `site` module in the Python standard library and hard-codes this path into it.[^site-module] [Here](https://github.com/Homebrew/homebrew-core/blob/d1eda30dc18d0b9572cd80eb254713dc2d0250d0/Formula/python3.rb#L208-L224) is the code snippet in charge of this.

To additionally install Python 2.7, repeat the same steps as above but replace `python3` with `python2` everywhere.

In theory, brew allows for having multiple version of each "formula" installed, such as Python 3.6.0 next to 3.6.3. The `brew switch` command does the switching, and [this somewhat outdated Stackoverflow response](https://stackoverflow.com/questions/3987683/homebrew-install-specific-version-of-formula) explains how to get those versions in the first place. The latter is the troublesome part: You are not meant to install any previous versions with brew, and doing so anyway is appropriately difficult and involves digging through git history repos you wouldn't otherwise know exist.


### brew Pros & Cons




## Option 2: pyenv

pyenv is the most common answer to the question on Stackoverflow.

https://github.com/pyenv/pyenv-virtualenv
https://github.com/pyenv/pyenv-virtualenvwrapper


## Option 3: Docker

### Docker Conceptually

The idea behind [Docker](https://www.docker.com/what-container) is to bundle everything that is required to run an application into a "container image". In the case of a Python application, the "everything" in the previous sentence includes Python itself, all dependendencies of the app, and the code for the app itself. [Installing Docker for Mac](https://www.docker.com/docker-mac) is done through a GUI installer. Short of running your code on a separate (physical or virtual) machine, Docker containers are the closest to an isolated environment you can run your Python code in.

### Docker Practically

To run a specific version of Python in a Docker container, you'll have to write or find a `Dockerfile` that creates a Docker image with said Python version installed. You can then launch as many Docker containers ("instances") from this image as you wish.

Conveniently, there are pre-built Docker images based on open source `Dockerfile`s for all Python versions available [on Docker Hub](https://hub.docker.com/_/python/). You can simply reference them by their name, for example `python:3.6.3`:

```sh
$ docker run -it --rm -v "$PWD":/code \
    -w /code python:3.6.3 python my_script.py
```

If your Python project has Python package dependencies (listed in a `requirements.txt`), it is usually more convenient to use the image from Docker Hub as starting point for your own `Dockerfile`, for example:

```
# Dockerfile
FROM python:3.6.3

WORKDIR /code

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./my_script.py" ]
```

The build your custom Docker image and run it with [^docker-requirements]:

```
$ docker build -t my_docker_image .
$ docker run -it --rm my_docker_image
```

### Docker Pros & Cons

Given the original question about installing Python on a Mac, this solution is a bit of a cheat: Technically this installs Python in a container on a VM on your Mac. Docker for Mac hides this complexity quite well, but before using Docker daily you will have to master a few concepts and commands to avoid frustration. I see that as both good and bad: Good because Docker is a useful and frequently used tool for all stages of software development, knowing the basics is required for the well-rounded software engineer. Bad because learning takes time and nobody has time.

It works and is difficult to mess up: The number of Docker images you can store on your Mac is only limited by disk space and every Docker image could contain a different version of Python. And because every image is fully isolated and containers are (usually) ephemeral, it's almost impossible to accidentally "break" a carefully crafted Python environment with an inadvertent wrong command.

Docker containers are more resource intensive than the other solutions. For example, the Docker image downloaded from Docker Hub in the example above is 691MB large. When running, Docker containers consume less memory and CPU than an equivalent virtual machine would but more than running the Python script in macOS. If battery life is a concern for you, then Docker might not be your friend[^docker-resources].


## Others

* Macports package manager
* apt & apt-get
* Conda (and other distributions?)

Something about how tox works?


## Conclusions

* Decision tree?
* My preferred tools?



[^latest-versions]: Those were the latest versions at the time of writing in November 2017. Head to https://www.python.org/downloads/ to see the current latest versions.

[^brew-terminology]: Be warned: brew uses brewery inspired nomenclature involving taps, bottles, kegs, and formulae. As far as I know, this hasn't helped anyone ever.

[^brew-python-2-3]: All the details about brew and Python are documented [here](https://github.com/Homebrew/brew/blob/master/docs/Homebrew-and-Python.md).

[^site-module]: The question how Python knows where to look for `site-packages` had me stumped for a while. [This blog post on](https://leemendelowitz.github.io/blog/how-does-python-find-packages.html) eventually put me on the right track.

[^path-env]: Inspect it with `echo $PATH`. To make a change that "sticks", you can prepend values to it by placing a line like this in your `~/.bash_profile` file: `export PATH="/some/path/:$PATH".

[^which-links]: `which` will not resolve symbolic links. If you ever care to know the resolve path, you can use the `readlink` command, for example `which python | xargs readlink`.

[^docker-requirements]: If you write a `Dockerfile` like this, keep in mind that your requirements are "baked into" the Docker image. If you change the `requirements.txt` you will have to rebuild the Docker image.

[^docker-resources]: Note that this is likely specific to macOS and specifically does not apply to Linux where Docker containers are a native concept.
