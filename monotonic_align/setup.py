from setuptools import setup
from Cython.Build import cythonize
import numpy
import os

output_dir = os.path.join(os.getcwd(), 'monotonic_align')

setup(
    name='monotonic_align',
    ext_modules=cythonize("core.pyx", language_level="3"),
    include_dirs=[numpy.get_include()],
    script_args=["build_ext", "--build-lib", output_dir]
)
