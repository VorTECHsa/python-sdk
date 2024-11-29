from packaging.version import Version

from vortexasdk.version import __version__

if __name__ == "__main__":
    proposed = Version(__version__)

    if not proposed.is_prerelease:
        raise Exception(
            f"The proposed version {__version__} is not a pre-release version"
        )

    print(f"Proposed version {proposed} is allowed as a pre-release version")
