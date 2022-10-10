# VortexaSDK

[![CircleCI](https://circleci.com/gh/VorTECHsa/python-sdk.svg?style=svg)](https://circleci.com/gh/VorTECHsa/python-sdk)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![All Contributors](https://img.shields.io/badge/all_contributors-12-orange.svg?style=flat-square)](#contributors)

Welcome to Vortexa's Python Software Development Kit (SDK)! We built the SDK to
provide fast, interactive, programmatic exploration of our data. The tool lets
Data Scientists, Analysts and Developers efficiently explore the world’s
waterborne oil movements, and to build custom models & reports with minimum
setup cost.

The SDK sits as a thin python wrapper around
[Vortexa's API](https://docs.vortexa.com), giving you immediate access to pandas
DataFrames.

##### Example

In an interactive Python console, run:

```python
>>> from datetime import datetime
>>> from vortexasdk import CargoMovements
>>> df = CargoMovements()\
        .search(filter_activity='loading_state',
            filter_time_min=datetime(2017, 8, 2),
            filter_time_max=datetime(2017, 8, 3))\
        .to_df()
```

returns:

|     | quantity | vessels.0.name | product.group.label | product.grade.label | events.cargo_port_load_event.0.end_timestamp | events.cargo_port_unload_event.0.start_timestamp |
| --: | -------: | :------------- | :------------------ | :------------------ | :------------------------------------------- | :----------------------------------------------- |
|   0 |     1998 | ALSIA SWAN     | Clean products      | Lube Oils           | 2017-08-01T06:10:45+0000                     | 2017-08-27T14:38:15+0000                         |
|   1 |    16559 | IVER           | Dirty products      | nan                 | 2017-08-02T17:20:51+0000                     | 2017-09-07T07:52:20+0000                         |
|   2 |   522288 | BLUE SUN       | Crude               | Gharib              | 2017-08-02T04:22:09+0000                     | 2017-08-13T10:32:09+0000                         |

## Quick Start

Try me out in your browser:

[![Binder](https://img.shields.io/badge/try%20me%20out-launch%20notebook-579ACA.svg?logo=data:image/png;base64,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)](https://mybinder.org/v2/gh/VorTECHsa/python-sdk/master?filepath=docs%2Fexamples%2Ftry_me_out%2Fcargo_movements.ipynb)

##### Installation

```bash
$ pip install vortexasdk
```

The SDK requires Python version 3.7 or above, see
[Setup FAQ](https://vortechsa.github.io/python-sdk/faq_setup/) for more details.

To install the SDK on an Apple ARM-based machine, use Python version to 3.8 or higher and use the latest version of pip. This is supported in the SDK versions 0.41.0 or higher.

##### Authentication

Set your `VORTEXA_API_KEY` environment variable, that's all. Alternatively, the
SDK prompts to you enter your API Key when running a script interactively.

To get an API key and experiment with Vortexa's data, you can
[request a demo here](https://www.vortexa.com/demo).

##### Check Setup

To check the SDK is setup correctly, run the following in a bash console:

```bash
$ python -m vortexasdk.check_setup
```

A successful setup looks like this:

![check_setup.png](https://raw.githubusercontent.com/VorTECHsa/python-sdk/master/docs/img/check_setup.png)

## Next Steps

Learn how to call
[Endpoints](https://vortechsa.github.io/python-sdk/endpoints/about-endpoints/)

## Glossary

The Glossary can be found at
[Vortexa API Documentation](https://docs.vortexa.com). The Glossary outlines key
terms, functions and assumptions aimed at helping to extract powerful findings
from our data.

## Documentation

Read the documentation at
[VortexaSDK Docs](https://vortechsa.github.io/python-sdk/)

## Contributing

We welcome contributions! Please read our
[Contributing Guide](https://github.com/vortechsa/python-sdk/blob/master/CONTRIBUTING.md)
for ways to offer feedback and contributions.

Thanks goes to these wonderful contributors
([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="http://vortexa.com/"><img src="https://avatars1.githubusercontent.com/u/33626692?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Kit Burgess</b></sub></a><br /><a href="#design-KitBurgess" title="Design">🎨</a> <a href="https://github.com/VorTECHsa/python-sdk/commits?author=KitBurgess" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/cvonsteg"><img src="https://avatars2.githubusercontent.com/u/28671095?v=4?s=100" width="100px;" alt=""/><br /><sub><b>tinovs</b></sub></a><br /><a href="https://github.com/VorTECHsa/python-sdk/commits?author=cvonsteg" title="Code">💻</a> <a href="https://github.com/VorTECHsa/python-sdk/pulls?q=is%3Apr+reviewed-by%3Acvonsteg" title="Reviewed Pull Requests">👀</a></td>
    <td align="center"><a href="http://star-www.st-and.ac.uk/~ds207/"><img src="https://avatars3.githubusercontent.com/u/11855684?v=4?s=100" width="100px;" alt=""/><br /><sub><b>David Andrew Starkey</b></sub></a><br /><a href="https://github.com/VorTECHsa/python-sdk/commits?author=dstarkey23" title="Code">💻</a> <a href="https://github.com/VorTECHsa/python-sdk/commits?author=dstarkey23" title="Documentation">📖</a> <a href="#example-dstarkey23" title="Examples">💡</a></td>
    <td align="center"><a href="https://github.com/syed1992"><img src="https://avatars2.githubusercontent.com/u/45287337?v=4?s=100" width="100px;" alt=""/><br /><sub><b>syed</b></sub></a><br /><a href="https://github.com/VorTECHsa/python-sdk/pulls?q=is%3Apr+reviewed-by%3Asyed1992" title="Reviewed Pull Requests">👀</a></td>
    <td align="center"><a href="https://www.vortexa.com/"><img src="https://avatars0.githubusercontent.com/u/503380?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Jakub Korzeniowski</b></sub></a><br /><a href="#ideas-kujon" title="Ideas, Planning, & Feedback">🤔</a></td>
    <td align="center"><a href="https://github.com/eadwright"><img src="https://avatars0.githubusercontent.com/u/17048626?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Edward Wright</b></sub></a><br /><a href="#userTesting-eadwright" title="User Testing">📓</a></td>
    <td align="center"><a href="https://paddyroddy.github.io/"><img src="https://avatars3.githubusercontent.com/u/15052188?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Patrick Roddy</b></sub></a><br /><a href="#userTesting-paddyroddy" title="User Testing">📓</a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://github.com/rugg2"><img src="https://avatars3.githubusercontent.com/u/37453675?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Romain</b></sub></a><br /><a href="#userTesting-rugg2" title="User Testing">📓</a> <a href="#ideas-rugg2" title="Ideas, Planning, & Feedback">🤔</a></td>
    <td align="center"><a href="https://github.com/Natday"><img src="https://avatars3.githubusercontent.com/u/38128493?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Natday</b></sub></a><br /><a href="#business-Natday" title="Business development">💼</a> <a href="#ideas-Natday" title="Ideas, Planning, & Feedback">🤔</a> <a href="#userTesting-Natday" title="User Testing">📓</a></td>
    <td align="center"><a href="https://github.com/ArthurD1"><img src="https://avatars0.githubusercontent.com/u/44548105?v=4?s=100" width="100px;" alt=""/><br /><sub><b>ArthurD1</b></sub></a><br /><a href="#userTesting-ArthurD1" title="User Testing">📓</a></td>
    <td align="center"><a href="https://github.com/ChloeConnor"><img src="https://avatars2.githubusercontent.com/u/42340891?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Chloe Connor</b></sub></a><br /><a href="#userTesting-ChloeConnor" title="User Testing">📓</a></td>
    <td align="center"><a href="https://www.vortexa.com/"><img src="https://avatars1.githubusercontent.com/u/31421156?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Achilleas Sfakianakis</b></sub></a><br /><a href="#userTesting-asfakianakis" title="User Testing">📓</a></td>
    <td align="center"><a href="https://seanbarry.dev"><img src="https://avatars0.githubusercontent.com/u/7374449?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Sean Barry</b></sub></a><br /><a href="https://github.com/VorTECHsa/python-sdk/commits?author=SeanBarry" title="Code">💻</a> <a href="https://github.com/VorTECHsa/python-sdk/commits?author=SeanBarry" title="Documentation">📖</a></td>
    <td align="center"><a href="https://github.com/dufia"><img src="https://avatars1.githubusercontent.com/u/5569649?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Konrad Moskal</b></sub></a><br /><a href="https://github.com/VorTECHsa/python-sdk/commits?author=dufia" title="Code">💻</a></td>
  </tr>
  <tr>
    <td align="center"><a href="http://pawelpietruszka.net"><img src="https://avatars0.githubusercontent.com/u/17066202?v=4" width="100px;" alt=""/><br /><sub><b>Pawel Pietruszka</b></sub></a><br /><a href="https://github.com/VorTECHsa/python-sdk/commits?author=Selerski" title="Code">💻</a></td>
  </tr>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the
[all-contributors](https://github.com/all-contributors/all-contributors)
specification. Contributions of any kind welcome!
