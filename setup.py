from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='ginz',
    version='1.0.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'ginz = ginz.__main__:main',
        ],
    },
    install_requires=requirements
)
