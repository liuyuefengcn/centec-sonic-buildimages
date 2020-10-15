#!/usr/bin/env python

from __future__ import print_function

import time
import imp

try:
    from sonic_platform_base.psu_base import PsuBase
    from sonic_py_common import device_info
except ImportError as e:
    raise ImportError("%s - required module not found" % e)

class Psu(PsuBase):
    """DellEMC Platform-specific PSU class"""

    def __init__(self, index):
        self._index = index
        self._fan_list = []
        
        # Get path to platform and hwsku
        platform_path, hwsku_path = device_info.get_paths_to_platform_and_hwsku_dirs()

        module_file = "/".join([platform_path, "plugins", "psuutil.py"])
        module = imp.load_source("psuutil", module_file)
        psu_util_class = getattr(module, "PsuUtil")
        self._psuutil = psu_util_class()

    def _get_psuutil(self):
        return self._psuutil

    def get_presence(self):
        return self._get_psuutil().get_psu_presence(self._index)

    def get_powergood_status(self):
        return self._get_psuutil().get_psu_status(self._index)
