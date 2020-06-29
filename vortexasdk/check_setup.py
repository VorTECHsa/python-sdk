import os

import requests

all_tests_pass = True


def check_api_key_present():
    global all_tests_pass
    api_key = os.getenv("VORTEXA_API_KEY")
    if api_key is None:
        print("🔸 Environment variable VORTEXA_API_KEY is not set.")
        print(
            "         Please set this environment variable, this is the recommended way to authenticate with the SDK."
            "\n         You may need to restart your python interpreter / bash terminal for the API Key to be ingested."
            "\n         Note: The SDK will work without an environment variable, you'll be prompted to interactively enter your password."
        )
    else:
        print("✅ Environment variable VORTEXA_API_KEY is set correctly.")


def check_can_connect_to_internet():
    global all_tests_pass
    # noinspection PyBroadException
    url = "https://api.github.com"

    try:
        status_code = requests.get(url).status_code
    except Exception:
        status_code = None

    if status_code is not None and status_code == 200:
        print("✅ You're connected to the internet")
    else:
        all_tests_pass = False
        print(f"❌ Python unable to connect to the internet.")
        print(f"         Python attempted to connect to {url}")
        print(f"         Check your internet connectivity / VPN settings.")


def check_can_connect_to_vortexa_api():
    global all_tests_pass

    url = "https://api.vortexa.com/health-check"
    reason, status_code = None, None
    try:
        response = requests.get(url)
        reason, status_code = response.reason, response.status_code
    except Exception:
        pass

    if status_code is not None and status_code == 200:
        print(f"✅ Python successfully connected to {url}")
    else:
        all_tests_pass = False
        print(f"❌ Python unable to connect to {url}")
        print(f"         status code: {status_code}")
        print(f"         reason: {reason}")


def check_can_import_vortexasdk():
    global all_tests_pass

    try:
        import vortexasdk

        print("✅ Python successfully imported vortexasdk")
    except ImportError:
        all_tests_pass = False
        print("❌ Python unable to import vortexasdk")


def check_can_retrieve_geographies():
    global all_tests_pass

    # noinspection PyBroadException
    try:
        from vortexasdk import Geographies

        europe = (
            "f39d455f5d38907394d6da3a91da4e391f9a34bd6a17e826d6042761067e88f4"
        )
        geography = Geographies().reference(europe)
        assert geography["id"] == europe
        print(
            "✅ Python successfully retrieved a sample piece of reference data"
        )
    except Exception as e:
        all_tests_pass = False
        print(e)
        print("❌ Python unable to retrieve a sample piece of reference data")


def run_all_checks():
    print("📚 Running Vortexa SDK setup check")
    check_api_key_present()
    check_can_connect_to_internet()
    check_can_connect_to_vortexa_api()
    check_can_import_vortexasdk()
    check_can_retrieve_geographies()

    if all_tests_pass:
        print("✅ All tests passed, the SDK is correctly setup!")
    else:
        print("❌ One or more tests have failed.")
    print()


if __name__ == "__main__":
    run_all_checks()
