from setuptools import setup, find_packages

setup(
    name="subtraction-plugin",
    version="0.1",
    packages=find_packages(),
    install_requires=['calculator-plugins>=0.1'],
    namespace_packages=['subtraction'],
    entry_points={
        'operation':
            ['subtraction_plugin=subtraction.subtraction:Subtraction'],
    },
    zip_safe=True
)
