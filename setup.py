from setuptools import setup, find_packages

setup(
    name='statcore',
    version='0.0.1',
    author='Andrew Barisser',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        "numpy>=1.21.0",
        ],
    tests_require=['pytest-cov', 'pytest'])