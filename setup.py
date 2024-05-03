import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

version = {}
with open("./vortexasdk/version.py") as fp:
    exec(fp.read(), version)

setuptools.setup(
    name="vortexasdk",
    version=version["__version__"],
    author="Vortexa Developers",
    author_email="developers@vortexa.com",
    description="Vortexa SDK",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    url="https://github.com/vortechsa/python-sdk",
    license="Apache License 2.0",
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        "flatten-dict==0.4.2",
        "pandas>=0.25.2",
        "requests==2.31.0",
        "pydantic>=1.10.2,<2",
        "tqdm==4.64.1",
        "urllib3>=1.26"
    ],
    extras_require={
        "tests": [
            "flake8==3.7.9",
            "black==22.8.0",
            "mkdocs==1.2.4",
            "mypy==0.971",
            "pre-commit==1.20.0",
            "pytest==5.2.4",
            "pydoc-markdown==2.0.5",
            "pyyaml<6.0.0",
            "six==1.12.0",
            "tabulate==0.8.7",
            "xlrd==1.2.0",
            "openpyxl==3.0.7",
            "types-requests==2.28.9",
            "types-urllib3==1.26.23",
            "types-tabulate==0.8.11",
            "types-python-dateutil==2.8.19",
            "types-six==1.16.19",
            "jupyter==1.0.0",
            "statsmodels==0.13.2",
            "matplotlib>=3.5.3"
        ],
        "binder": [
            "jupyter==1.0.0",
            "statsmodels==0.13.2",
            "matplotlib>=3.5.3"
        ],
        "deploy": ["wheel==0.37.1", "twine==4.0.1"],
    },
)
