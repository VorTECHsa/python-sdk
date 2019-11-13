# VortexaSDK

<!-- [![CircleCI](https://circleci.com/gh/V0RT3X4/python-sdk.svg?style=svg&circle-token=d19ee8fc3460b88b36afc28f86539a5f4057d021)](https://circleci.com/gh/V0RT3X4/python-sdk) -->

The VortexaSDK is Vortexa's Software Development Kit (SDK) for Python, which allows
Data Scientists, Analysts and Developers to query [Vortexa's API](https://docs.vortexa.com)



## Quick Start

##### Installation

```bash
$ pip install vortexasdk
```

##### Authentication

Set your `VORTEXA_API_KEY` environment variable, that's all.

##### Example

```python
>>> from vortexasdk import CargoMovements
>>> df = CargoMovements() \
        .search(filter_time_min="2019-08-01T00:00:00.000Z", filter_time_max="2019-08-01T00:15:00.000Z")\
        .to_df()
```


## Documentation

Read the documentation at [VortexaSDK Docs](https://v0rt3x4.github.io/python-sdk/)

## Contributing

We welcome contributions! Please read our [Contributing Guide](https://github.com/V0RT3X4/python-sdk/blob/master/CONTRIBUTING.md) for ways to offer feedback and contributions.

## Glossary

The Glossary can be found at [Vortexa API Documentation](https://docs.vortexa.com)

This outlines key terms, functions and assumptions aimed at
helping to extract powerful findings from our data.

