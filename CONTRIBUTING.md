# Contributing to Open Source Guides

Thanks for checking out the Open Source Guides! We're excited to hear and learn from you. Your experiences will benefit others who read and use these guides.

We've put together the following guidelines to help you figure out where you can best be helpful.

Interested in making a contribution? Read on!

## How to contribute

If you'd like to contribute, start by searching through the [Issues](https://github.com/V0RT3X4/python-sdk/issues) and [Pull Requests](https://github.com/V0RT3X4/python-sdk/pulls) to see whether someone else has raised a similar idea or question.

If you don't see your idea listed, and you think it fits into the goals of this guide, do one of the following:
* **If your contribution is minor,** such as a typo fix, open a pull request.
* **If your contribution is major,** such as a new guide, start by opening an issue first. That way, other people can weigh in on the discussion before you do any work.

## Ground rules & expectations

Before we get started, here are a few things we expect from you (and that you should expect from others):

* Be kind and thoughtful in your conversations around this project. We all come from different backgrounds and projects, which means we likely have different perspectives on "how open source is done." Try to listen to others rather than convince them that your way is correct.
* Open Source Guides are released with a [Contributor Code of Conduct](./CODE_OF_CONDUCT.md). By participating in this project, you agree to abide by its terms.
* If you open a pull request, please ensure that your contribution passes all tests. If there are test failures, you will need to address them before we can merge your contribution.
* When adding content, please consider if it is widely valuable. Please don't add references or links to things you or your employer have created as others will do so if they appreciate it.


## Style guide

### Commit message formatting
We adopt the [Conventional Commits](https://www.conventionalcommits.org) convention to format commit messages.


### Documentation
We're using [Pydocmd](https://github.com/NiklasRosenstein/pydoc-markdown)
to automatically generate docs.

Documentation should follow the [Google Documentation Style Guide](https://developers.google.com/style/api-reference-comments)

#### Setting up your environment

##### Installation
```bash
$ pip3 install -r requirements.txt
```

##### Running

Pydocmd:
```bash
$ ./docs/serve_docs.sh
```

…and open http://localhost:8000 in your web browser.

## Community

Discussions about the VortexaSDK take place on this repository's [Issues](https://github.com/V0RT3X4/python-sdk/issues) and [Pull Requests](https://github.com/V0RT3X4/python-sdk/pulls) sections. Anybody is welcome to join these conversations.

Wherever possible, do not take these conversations to private channels, including contacting the maintainers directly. Keeping communication public means everybody can benefit and learn from the conversation.