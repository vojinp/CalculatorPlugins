from setuptools import setup, find_packages

setup(
    name="calculator-plugins",
    version="0.1",
    packages=find_packages(),
    namespace_packages=['calculator'],
    provides=['calculator'],
    zip_safe=False
)