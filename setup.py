from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
  name='reactivehub-sdk-python',
  version='0.1',
  scripts=[''],
  author='reactivehub.io',
  author_email='luiz.gustavo@reactivehub.io',
  description='reactivehub.io Python SDK',
  long_description='The Reactivehub Python SDK implements the methods needed to publish events'
  url='https://github.com/reactivehub-io/reactivehub-sdk-python',
  packages=setuptools.find_packages(),
  classifiers=[
    "Programming Language :: Python :: 3",
    "License :: Apache 2.0",
    "Operating System :: OS Independent",
  ],
)