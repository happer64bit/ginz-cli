from setuptools import setup

with open("README.md") as file:
    long_description = file.read()

setup(
    name='ginz',
    version='1.2',
    license="MIT",
    description='Ginz is a command-line utility that simplifies the process of cloning multiple repositories from GitHub by allowing you to specify the repositories and their branches in a single configuration file.',
    url="https://github.com/happer64bit/ginz-cli",
    author='Happer64Bit',
    author_email='happer64bit@gmail.com',
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=["toml", "GitPython", "colorama", "tqdm", "requests"],
    packages=["ginz"],
    include_package_data=True,
)
