from codecs import open
from os.path import abspath, dirname, join
from subprocess import call

from setuptools import Command, find_packages, setup

from pythonanywhere_cli import __version__


this_dir = abspath(dirname(__file__))
with open(join(this_dir, "README.rst"), encoding="utf-8") as file:
    long_description = file.read()


class RunTests(Command):
    """Run all tests."""
    description = "run tests"
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        """Run all tests!"""
        errno = call(
            [
                "py.test",
                "--cov=pythonanywhere_cli",
                "--cov-report=term-missing",
            ]
        )
        raise SystemExit(errno)


setup(
    name = "pythonanywhere_cli",
    version = __version__,
    description = "PythonAnywhere Command Line Interface.",
    long_description = long_description,
    url = "https://github.com/cfc603/pythonanywhere_cli",
    author = "Trevor Watson",
    author_email = "wtrevor162@gmail.com",
    license = "MIT",
    classifiers = [
        "Intended Audience :: Developers",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords = "pythonanywhere_cli cli pythonanywhere",
    packages = find_packages(exclude=["docs", "tests*"]),
    install_requires = ["docopt", "pythonanywhere"],
    extras_require = {
        "test": [
            "coverage",
            "flake8",
            "pytest",
            "pytest-cov",
            "tox",
            "mock",
        ],
    },
    entry_points = {
        "console_scripts": [
            "pythonanywhere=pythonanywhere_cli.cli:main",
        ],
    },
    cmdclass = {"test": RunTests},
)