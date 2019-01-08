import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
  name='reactivehub-sdk-python',
  version='0.1',
  scripts=[''],
  author='reactivehub.io',
  author_email='luiz.gustavo@reactivehub.io',
  description='reactivehub.io Python SDK',
  long_description='The reactivehub.io Python SDK implements the methods to publish in Event api'
  url='https://github.com/reactivehub-io/reactivehub-sdk-python',
  packages=setuptools.find_packages(),
  classifiers=[
    "Programming Language :: Python :: 3",
    "License :: Apache 2.0",
    "Operating System :: OS Independent",
  ],
)