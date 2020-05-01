#### How to install Python on Windows using Anaconda
- Download the Python3.7 Graphical installer from the [anaconda website](https://www.anaconda.com/distribution/)
- Follow the conda installation instructions



#### How do I install the SDK on Windows?
- First, open up an Anaconda Prompt. Hit the start button and type anaconda prompt.

![Anaconda prompt](img/anaconda_prompt.png)

- Use pip to install the sdk

Run `pip install --user vortexasdk` in the anaconda command prompt

![pip_install.png](img/pip_install.png)

You're done! The VortexaSDK has now been installed.



#### How do I install the SDK on Mac / Linux?
Type the following into a bash terminal
```bash
$ pip install vortexasdk
```



#### How do I add an environment variable on Windows?
- Hit the windows key, then type "environment" to open up a control panel settings page titled "Edit the system environment variables"

![edit_system_env_vars.png](img/edit_system_env_vars.png)

-  In the System Properties window, click on the Advanced tab, then click the Environment Variables button near the bottom of that tab.
- Add a new user variable

![add_env_var.png](img/add_env_var.png)


#### Where is my API Key?
Refer to [Vortexa API Authentication](https://docs.vortexa.com/reference/intro-authentication)
 for details, including instructions on where to find your API key.

#### How do I request an API Key?
You can [request a demo here](https://www.vortexa.com/request-demo-sdk).

More details are given in [docs.vortexa.com](https://docs.vortexa.com/reference/intro-authentication).

Alternatively, please get in touch at [www.vortexa.com](https://www.vortexa.com/).


#### How can I check the VortexaSDK is setup correctly?

You can run the `check_setup.py` file from your IDE, or from a bash console:

```
$ python -m vortexasdk check-setup 
```