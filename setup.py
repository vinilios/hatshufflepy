import os
from setuptools import setup, find_packages
from subprocess import call
from setuptools.command.install import install
from distutils.extension import Extension
from Cython.Build import cythonize
from Cython.Distutils import build_ext


#  os.environ['CC'] = 'g++'
#  os.environ['CXX'] = 'g++'

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))


class CustomBuild(install):
    def run(self):
        call(['bash', 'install_depends.sh'])
        install.run(self)


module = Extension('hatshufflepy',
                    sources = ['hatshufflepy/hatshufflepy.pyx'],
                    language = 'c++',
                    include_dirs = ['hatshufflepy/libhatshuffle/include/libhatshuffle',
                                    'hatshufflepy/libhatshuffle/include',
                                    'libhatshuffle/include/libff'],
                    libraries = ['zm', 'ff', 'hatshuffle'],
                    library_dirs = ['/usr/local/lib',
                                    'hatshufflepy/libhatshuffle/lib'],
                    runtime_library_dirs=[ROOT_PATH +
                                          '/hatshufflepy/libhatshuffle/lib'],
                    extra_compile_args = ['-std=c++11', '-fPIC',
                                          '-shared', '-w',
                                          '-static', '-O3'],
                    extra_link_args = ['-lgmp', '-fopenmp', '-g'])


setup(
    name='hatshufflepy',
	version='0.0.1',
    packages=find_packages(),
	author='Stefanos Chaliasos',
	author_email='stefanoshaliassos@gmail.com',
	description='Cython wrapper for hat shuffle implementation',
	license='MIT',
	keywords='mixnet ecc',
	url='https://github.com/StefanosChaliasos/hatshufflepy',

    install_requires=["cython >= 0.22.1"],
    ext_modules=cythonize(module),
    cmdclass = {'build_ext': build_ext, 'install': CustomBuild},
)
