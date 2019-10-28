from setuptools import setup, find_packages

setup(
    name="addition-plugin",
    version="0.1",
    packages=find_packages(),
    install_requires=['calculator-plugins>=0.1'],
    namespace_packages=['addition'],
    entry_points={
        'operation':
            ['addition_plugin=addition.addition:Addition'],
    },
    zip_safe=True
)
