from setuptools import setup

setup(
   name='ginz',
   version='1.0',
   description='Ginz is a command-line tool for cloning multiple repositories from GitHub based on a configuration file. It simplifies the process of cloning multiple repositories by allowing you to specify the repositories and their branches in a single configuration file.',
   author='Happer64Bit',
   author_email='happer64bit@gmail.com',
   packages=['toml', "git", "colorama"],
   install_requires=['wheel', 'bar', 'greek'],
)