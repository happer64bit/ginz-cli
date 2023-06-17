from setuptools import setup, find_packages

with open("README.md") as file:
    long_description = file.read()

setup(
   name='ginz',
   version='1.0',
   license="MIT",
   description='Ginz is a command-line utility that simplifies the process of cloning multiple repositories from GitHub by allowing you to specify the repositories and their branches in a single configuration file.',
   author='Happer64Bit',
   author_email='happer64bit@gmail.com',
   long_description=long_description,
   install_requires=["toml", "python-git", "colorama"],
   package_directory="ginz",
)