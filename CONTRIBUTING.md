# Contributing to VortexaSDK


## Suggesting new features / Reporting An Issue

First, check to see if there's an existing issue/pull request for the
bug/feature. All issues are at https://github.com/vortechsa/python-sdk/issues and pull reqs are at
https://github.com/vortechsa/python-sdk/pulls.

If there isn't an existing issue there, please file an issue. The
ideal report includes:

-  A description of the problem/suggestion.
-  How to recreate the bug (including the version on your python interpreter).
-  If possible, create a pull request with a (failing) test case
   demonstrating what's wrong. This makes the process for fixing bugs
   quicker & gets issues resolved sooner.

## Setting up your environment

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

To run the live tests, you'll need to have the `VORTEXA_API_KEY` environment variable set.

run tests
```
$ python setup.py test
```

serve documentation
```bash
$ ./docs/scripts/serve_docs.sh
```
…and view the docs at http://localhost:8000 in your web browser.

Install the git [pre-commit-hooks](https://pre-commit.com/#3-install-the-git-hook-scripts)
```bash
$ pre-commit install
```


:tada: Now you're ready to create a new branch, add a feature or fix a bug, then send us a pull request! :tada:

## Contributing Code

A good pull request:
-  Is clear.
-  Follows the existing style of the code base (PEP-8).
-  Has comments included as needed.
-  A test case that demonstrates the previous flaw that now passes with
   the included patch, or demonstrates the newly added feature.
-  If it adds/changes a public API, it must also include documentation
   for those changes.

Tips:
- If you're adding a new endpoint, adapt and use `./docs/generate_stubs.sh` to generate sample json data used for tests.

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

## How to release a new version of the SDK:

### First, deploy a new version to pypi
1. Make changes in a branch, and have the PR approved.
2. Merge PR to master
3. On your local machine, checkout master and pull the latest changes.
4. Change `version.py` as necessary, following semver for a major/minor/patch release.
5. Generate a github access token, used by the github changelog generator,
 (see full instructions to generate token here)[https://github.com/github-changelog-generator/github-changelog-generator].
Store this token in as environment variable `GITHUB_CHANGELOG_TOKEN`. No scopes are needed for this token,
and you'll only need to generate this token once.
6. Ensure your `TWINE_USERNAME` and `TWINE_PASSWORD` environment variables are set.
7. Run `./scripts/export_package.sh` to export package to pypi.

### Second, deploy a new version of the documentation to github pages

Follow the instructions in the (sadly) semi automated script `./scripts/docs/deploy_docs.sh` 


## Code of Conduct

Please see https://github.com/vortechsa/python-sdk/blob/master/CODE_OF_CONDUCT.md for the code of conduct.
