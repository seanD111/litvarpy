from setuptools import setup
import pathlib

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name='litvarpy',
    version='0.0.1',
    packages=['litvar'],
    install_requires=[
        'certifi'
    ],
    description="A Python interface for LitVar on NCBI",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/seanD111/litvarpy",
    author="Sean DeLong",
    author_email="sean_delong@hotmail.ca",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    extras_require={
        'test': [
            'pytest',
            'coverage',
            'pytest-cov'
        ],
    },
)
