#!/usr/bin/env python

import os
import sys
from setuptools import setup
os.listdir

setup(
   name='48s4x',
   version='1.1',
   description='Module to initialize centec e530-48s4x platforms',
   
   packages=['48s4x'],
   package_dir={'48s4x': '48s4x/classes'},
)

