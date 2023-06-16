from setuptools import setup, find_packages

setup(
    name='ginz',
    version='1.0.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'ginz = ginz.__main__:main',
        ],
    },
)
