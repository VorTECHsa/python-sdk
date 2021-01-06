## Config

The VortexaSDK can be configured using environment variables.

| Environment Variable  | Default                         | Description              |
|:----------------------|:--------------------------------|:-------------------------|
| VORTEXA_API_KEY       | none                            | API Key used to access the VortexaAPI. Refer to [Vortexa API Authentication](https://docs.vortexa.com/reference/intro-authentication) for more details, including instructions on where to find your API key.|
| LOG_FILE              | none                            | Output log file          |
| LOG_LEVEL             | INFO                            | Configure the level of must be one of `["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]` |
| HTTP_PROXY            | none                            | Send API requests via a corporate http proxy. This environment variable is used by the requests library, [see here for further details](https://requests.readthedocs.io/en/master/user/advanced/#proxies) |
| HTTPS_PROXY           | none                            | Send API requests via a corporate https proxy. This environment variable is used by the requests library, [see here for further details](https://requests.readthedocs.io/en/master/user/advanced/#proxies) |
