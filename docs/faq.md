#### Why do my requests hang or run in an infinite loop or I get a RuntimeError ("An attempt has been made to start a new process...")?
On Windows, it may be that your script doesn't check `if __name__ == "__main__":`
before calling the SDK. Your script should contain this check, just like in [this example](https://vortechsa.github.io/python-sdk/examples/0_sample_load_cargo_movements/)
For more details on why `if __name__ == "__main__":` is required, check out those interesting stack overflow posts [here](https://stackoverflow.com/questions/20360686/compulsory-usage-of-if-name-main-in-windows-while-using-multiprocessi) and [here](https://stackoverflow.com/questions/18204782/runtimeerror-on-windows-trying-python-multiprocessing) on Windows multiprocessing.

#### How do I use the SDK with a corporate proxy?
To send SDK requests via a proxy, you can set the `HTTP_PROXY` or `HTTPS_PROXY` environment variables.
More detail is given in the requests library docs [here](https://requests.readthedocs.io/en/master/user/advanced/#proxies)

#### What's the difference between a cargo movement and a vessel movement?
A cargo movement is defined as the complete journey of a quantity of oil from its origin terminal to its destination terminal, including all ship to ship (STS) transfers in-between.
For example: Tanker X loads 1mn bl of crude from Houston and discharges onto another tanker Y offshore the US Gulf, which then discharges in Singapore.
The cargo movement is for 1mn bl of crude oil from Houston to Singapore.
The vessel movement for tanker X is Houston to US Gulf, while for tanker Y it is US Gulf to Singapore. When there is no STS transfer, a cargo movement and vessel movement is equivalent.

A more detailed explanation can be found [here](https://docs.vortexa.com/reference/intro-cargo-movement)

#### Where can I find a list of products?
Check out the Vortexa Glossary, which can be downloaded from [here](https://docs.vortexa.com/reference/intro-introduction)


#### What's the difference in a trading region and a geographic region?
Trading regions have been designed by Vortexa to try and group terminals,
ports and countries around oil market conventions
(e.g. northwest Europe, west Africa, etc) whereas geographic regions
are much wider in scope (e.g. North America, Asia, Africa).
Trading regions are more granular than geographic regions.