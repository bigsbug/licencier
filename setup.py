from setuptools import setup
from Cython.Build import cythonize

setup(
    name='license app',
    ext_modules=cythonize("license.py"),
    zip_safe=True,
)