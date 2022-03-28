from setuptools import setup, find_packages, Extension
from Cython.Build import cythonize

setup(
    name='statcore',
    version='0.0.1',
    author='Andrew Barisser',
    license='MIT',
    packages=find_packages(),
    ext_modules=cythonize(
        [
            Extension(name="table", sources=["statcore/table.pyx"]),
       #     Extension(name="fibz", sources=["statcore/fib.pyx"]),
        ],
        compiler_directives={'language_level' : "3"},
        annotate=True
        ),# + [Extension(name="smath", sources=["statcore/math.cpp"])],
    zip_safe=False,
    install_requires=[
        ],
    tests_require=['pytest-cov', 'pytest'])