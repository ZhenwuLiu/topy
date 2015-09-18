﻿#!/usr/bin/env python

from distutils.core import setup

setup(name='ToPy',
      version='0.1.2',
      description='Topology optimization with Python',
      author='William Hunter',
      url='https://github.com/williamhunter/ToPy',
      packages=['topy', 'topy.core', 'topy.core.data'],
      package_dir={'topy': ''}
     )
