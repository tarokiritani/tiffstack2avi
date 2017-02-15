#!/usr/bin/env python

from distutils.core import setup

try:
    import pypandoc
    long_description=pypandoc.convert('README.md', 'rst')
except(IOError, ImportError):
    long_description=open('README.md').read()

setup(
  name = 'tiffstack2avi',
  packages = [],
  version = '1.1.2',
  py_modules = ['tiffstack2avi'],
  description = 'A small python wrapper for ffmpeg',
  author = 'Taro Kiritani',
  author_email = 'taro.kiritani@epfl.ch',
  url = 'https://github.com/tarokiritani/tiffstack2avi',
  download_url = 'https://github.com/tarokiritani/tiffstack2avi/tarball/1.1.2',
  keywords = ['ffmpeg', 'python', 'wrapper'],
  classifiers = [
                 'Programming Language :: Python :: 3.5'
                 
                 ],
  license='MIT',
  long_description=long_description,
)