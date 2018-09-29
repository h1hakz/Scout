# Scout

Scout is a tool developed in python for people who want to find a group of keywords on a blink of an eye.

This tool has been optimized to find keywords in unencrypted files with extension. This tool also gives the freedom for users to add their on files extensions to exclude for searching.

Scout can be used on Web application, Mobile and secure source code audit assessment for finding hardcoded credentials or sensitive information in files.

# Why use Scout ???

We were trying to solve an issue and thought why not automate it and so Scout was born.

Scout is very fast, we optimized and made scout so fast that it can look for the keywords on the files within seconds or maybe less than that and can generate a consolidated report in csv format with all the details you want for your audit.

There is no open source tool like Scout till now which looks for a group of keyword at the same time on larger files without any delay of crashing the system performance.

## Installation

### Requirements
* Linux/Windows/Mac
* Python 2.7 and up

`$ git clone https://github.com/h1hakz/Scout.git`

`$ cd Scout`

## Usage

Please feel free to add your own keywords in keywordfile.txt before running.

There is also a functionality were you can blacklist the file extension to avoid looking on those.

For that simply edit fileBlackList.txt and customize as per your need. This is the most effective way were it will only look on to the extension which is in scope.

```
python scout.py /foldertolookin/ /pathofscout/Scout/keywordfile.txt
```

## Example

<img src="https://github.com/h1hakz/Scout/blob/master/Scout-Demo.gif"/>

## Collaborators

* Manoj Kumar - #cysmanojsah
* Ranjith Menon - #ranjith_menon16


## Contribution, Feature Requests & Bugs

mail us on h1hakz[at]gmail[dot]com or tweet to #h1hakz

## License
[GNU](https://github.com/h1hakz/Scout/blob/master/LICENSE)
