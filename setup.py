from setuptools import setup

setup(
    name = "ProperME",
    version = '0.0.1',
    python_requires = ">=3.8",
    install_requires = [
        "dill",
        "numpy"
    ],
    packages = find_packages(),
    author = "Michael Engel",
    author_email = "m.engel@tum.de"
)