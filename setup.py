import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='vortexa-sdk',
    version='0.1.0-dev',
    author='Vortexa Developers',
    author_email='developers@vortexa.com',
    description='Vortexa SDK',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    url='https://github.com/V0RT3X4/python-sdk',
    license='Apache License 2.0',
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
