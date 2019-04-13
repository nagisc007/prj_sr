# storybuilder
![Build Status](https://travis-ci.org/nagisc007/storybuilder.svg?branch=master)
[![Coverage Status](https://coveralls.io/repos/github/nagisc007/storybuilder/badge.svg)](https://coveralls.io/github/nagisc007/storybuilder)

A tester and generator for a structure of a story.

## Description

storybuilder is a python library that use to test and generate a story.
the story is expressed by action objects that contain a few informations.

It is only made for N.T.Works. Currently, not want any contributer.

***DEMO:***

see contained example story.

## Features

- Test a story's elements
- Output to a markdown

## Requirement

- python 3.4 over

## Usage

1. Write a story code by python
1. Import storybuilder into the code and add the library path
    ```python
    import sys
    import os
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
    sys.path.append('storybuilder')
    ```
1. Write a test code
1. Check your story code: ``$ python3 setup.py test``
1. Output a markdown file in build dir: ``$ python3 your_package/your_story.py``

## Installation

Not recommend to install!!

## Author

[N.T.WORKS](https://twitter.com/nagi_tter)

## License

[MIT](http://b4b4r07.mit-license.org)


(C)2019 N.T.WORKS

