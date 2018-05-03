import os
# from distutils.core import setup
from setuptools import setup
from distutils.extension import Extension
from Cython.Build import cythonize

from Cython.Distutils import build_ext


os.environ["CC"] = "g++"
os.environ["CXX"] = "g++"

setup(
    name="hatshufflepy",
	version="0.0.1",

	author="Stefanos Chaliasos",
	author_email="stefanoshaliassos@gmail.com",
	description="Cython wrapper for hat shuffle implementation",
	license="MIT",
	keywords="mixnet",
	url="https://github.com/grnet/hat_shuffle",

    	install_requires=[
		"cython >= 0.22.1"
	],

    ext_modules=cythonize(
        Extension(
            "hatshufflepy",
            sources=["hatshufflepy/hatshufflepy.pyx"],
            language="c++",
            include_dirs=["hatshufflepy/libhatshuffle/include/libhatshuffle",
                          "hatshufflepy/libhatshuffle/include",
                          "libhatshuffle/include/libff"],
            library_dirs = ["/usr/local/lib",
                            "hatshufflepy/libhatshuffle/lib"],
            extra_compile_args = ["-std=c++11", "-fPIC", "-shared", "-w", "-static", "-O3"],
            extra_link_args = ["-lgmp", "-lzm", "-lff", "-lhatshuffle", "-fopenmp", "-g"]
        )
    ),
    cmdclass = {'build_ext': build_ext},
)
