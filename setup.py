import os
import sys
import shutil
from setuptools import setup, find_packages, Extension
from distutils.sysconfig import get_python_lib
from subprocess import call
from setuptools.command.build_ext import build_ext as BuildCommand
from Cython.Build import cythonize
from Cython.Distutils import build_ext


#  os.environ['CC'] = 'g++'
#  os.environ['CXX'] = 'g++'

major = str(sys.version_info.major)
minor = str(sys.version_info.minor)

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
VERSION = 'python' + major + '.' + minor
LIB_PATH = get_python_lib()

DEBUG = bool(os.environ.get('HATSHUFFLE_DEBUG', False))
COMPILE_ARGS = ['-std=c++11', '-shared', '-w', '-static', '-fPIC', '-O3']
LINK_ARGS = ['-lstdc++', '-lhatshuffle']
if DEBUG:
    COMPILE_ARGS.append('-g')
    LINK_ARGS.append('-g')


class CustomBuild(BuildCommand):
    def run(self):
        call(['bash', 'install_depends.sh'])
        BuildCommand.run(self)

module = Extension('hatshufflepy',
    sources=['hatshufflepy/hatshufflepy.pyx'],
    language='c++',
    libraries=['hatshuffle', 'stdc++'],
    include_dirs=['hatshufflepy_dist/include/libhatshuffle',
                  'hatshufflepy_dist/include/'],
    library_dirs=['hatshufflepy_dist/lib/'],
    runtime_library_dirs=['$ORIGIN/hatshufflepy_dist/lib/'],
    extra_compile_args=COMPILE_ARGS,
    extra_linker_args=LINK_ARGS
)


setup(
    name='hatshufflepy',
    version='0.0.6',
    packages=find_packages(),
    author='Stefanos Chaliasos',
    author_email='stefanoshaliassos@gmail.com',
    description='Cython wrapper for hat shuffle implementation',
    license='MIT',
    keywords='mixnet ecc',
    url='https://github.com/StefanosChaliasos/hatshufflepy',

    install_requires=["cython >= 0.29"],
    package_data= {
        'hatshufflepy_dist': ['lib/*.so']
    },
    include_package_data=True,
    ext_modules=cythonize(module, gdb_debug=True),
    cmdclass={'build_ext': CustomBuild},
)
