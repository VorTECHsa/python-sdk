# python-template

Template repository for python projects

## Local check to make sure python files are formatted with black and obey flake8

Inspired by this [blog](https://ljvmiranda921.github.io/notebook/2018/06/21/precommits-using-black-and-flake8/).

To enable locally:

```
pip install requirements.txt
pre-commit install
```

this will create a local git hook which will perform the checks. The big
advantage of this is that now PRs can solely be checking actual code changes
rather than formatting changes. Although if this is enabled on an old badly
formatted repo it will require a bit of work to get it up to scratch, but from
that point onwards it's plain sailing.
