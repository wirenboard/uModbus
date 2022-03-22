#!/usr/bin/env python
"""
uModbus is a pure Python implementation of the Modbus protocol with support
for Python 2.7, 3.4, 3.5, 3.6, 3.7 and 3.8.

"""
from __future__ import unicode_literals
import os
from setuptools import setup
import codecs

cwd = os.path.dirname(os.path.abspath(__name__))

f = codecs.open(os.path.join(cwd, 'README.rst'), 'r', encoding='utf-8')
long_description = f.read()

setup(name='uModbus',
      version='1.0.4',
      author='Auke Willem Oosterhoff',
      author_email='a.oosterhoff@climotion.com',
      description='Implementation of the Modbus protocol in pure Python.',
      url='https://github.com/AdvancedClimateSystems/umodbus/',
      long_description=long_description,
      license='MPL',
      packages=[
          'umodbus',
          'umodbus.client',
          'umodbus.client.serial',
          'umodbus.server',
          'umodbus.server.serial',
      ],
      install_requires=[
          'pyserial~=3.4',
      ],
      classifiers=[
          'Development Status :: 6 - Mature',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Topic :: Software Development :: Embedded Systems',
      ])
