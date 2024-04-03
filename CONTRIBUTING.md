# Contributing to VortexaSDK

## Suggesting new features / Reporting An Issue

First, check to see if there's an existing issue/pull request for the
bug/feature. All issues are at https://github.com/vortechsa/python-sdk/issues and pull reqs are at
https://github.com/vortechsa/python-sdk/pulls.

If there isn't an existing issue there, please file an issue. The
ideal report includes:

- A description of the problem/suggestion.
- How to recreate the bug (including the version on your python interpreter).
- If possible, create a pull request with a (failing) test case
  demonstrating what's wrong. This makes the process for fixing bugs
  quicker & gets issues resolved sooner.

## Setting up your environment

**`Users of ARM-based Apple machines, please refer to the note at the end!`**

First, clone the repo, then `cd` into the repo.

```bash
$ git clone git@github.com:vortechsa/python-sdk.git
$ cd python-sdk
```

create a new virtual environment

```bash
$ python3.7 -m venv venv
```

activate your environment

```bash
$ . venv/bin/activate
```

install the required dependencies

```
$ pip install -e '.[tests]'
```

To run the live tests, you'll need to have the `VORTEXA_API_KEY` environment variable set - `export VORTEXA_API_KEY=xyz`

run tests

```
$ python setup.py test
```

If you're just looking to run tests in a single module (`test_vessels` in this case), you can do like this:

```bash
$ pytest -v tests/endpoints/test_vessels.py
```

Run all the 'try-me-out' notebooks, and then clear the cell outputs so the data isn't publicly visible.

```bash
jupyter nbconvert --to notebook --inplace --execute  docs/examples/try_me_out/*.ipynb
jupyter nbconvert --to notebook --inplace --clear-output docs/examples/try_me_out/*.ipynb
```

Serve documentation locally

```bash
$ ./docs/scripts/serve_docs.sh
```

…and view the docs at http://localhost:8000 in your web browser.

Install the git [pre-commit-hooks](https://pre-commit.com/#3-install-the-git-hook-scripts)

```bash
$ pre-commit install
```

:tada: Now you're ready to create a new branch, add a feature or fix a bug, then send us a pull request! :tada:

### Note about Apple ARM-based chips

To run the SDK on an Apple ARM chip, upgrade your Python version to 3.8 or higher and use the latest version of pip. This works for the SDK version 0.41.0 or higher.

The set up is almost identical as above except one command; to create a virtual environment for Python 3.8 you should run:

```bash
$ python3.8 -m venv venv
```

## Contributing Code

### Releasing a new package

New versions of the SDK are automatically released to pypi when your branch PR is merged into the master branch.

In the branch you're working on, you'll need to change the `version.py` file to the new version that you're looking to deploy.
The python-sdk follow strict semver, so you'll need to increment the MAJOR nunber if and only if you're introducing
a breaking change, the MINOR number if you're addind a new feature, or PATCH number if you've introduced a bug fix.

Once your branch is merged to master, CircleCI will do a few things:

- Deploy the new package to pypi https://pypi.org/project/vortexasdk/, using the version in `version.py`.
- Update the github pages documentation at https://vortechsa.github.io/python-sdk/
- Create a git tag, usign the version in `version.py`

### Pull requests:

A good pull request:

- Is clear.
- Follows the existing style of the code base (PEP-8).
- Has comments included as needed.
- A test case that demonstrates the previous flaw that now passes with
  the included patch, or demonstrates the newly added feature.
- If it adds/changes a public API, it must also include documentation
  for those changes.

Tips:

- If you're adding a new endpoint, adapt and use `./scripts/generate_stubs.sh` to generate sample json data used for tests.

### Contributing Jupyter Notebooks

Please include the version of the SDK and any other packages used to generate the Jupyter Notebook at the start of the notebook. This helps others to reproduce your results in the future.

## Style guide

#### Commit message formatting

We adopt the [Conventional Commits](https://www.conventionalcommits.org) convention to format commit messages.

#### Documentation

We're using [Pydocmd](https://github.com/NiklasRosenstein/pydoc-markdown)
to automatically generate docs.

Documentation should follow the [Google Documentation Style Guide](https://developers.google.com/style/api-reference-comments)

## Community

Discussions about the VortexaSDK take place on this repository's https://github.com/vortechsa/python-sdk/issues and https://github.com/vortechsa/python-sdk/pulls sections. Anybody is welcome to join these conversations.

Wherever possible, do not take these conversations to private channels, including contacting the maintainers directly. Keeping communication public means everybody can benefit and learn from the conversation.

## Code of Conduct

Please see https://github.com/vortechsa/python-sdk/blob/master/CODE_OF_CONDUCT.md for the code of conduct.
