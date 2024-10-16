# -*- coding: utf-8 -*-
# @Time    : 2024/06/27

import json
import requests
from .constants import *

class BaseAPI(object):
    """docstring for ClassName"""
    def __init__(self, configs):
        self.configs = configs
        self.name = API_NAME_BASE

    def api(self, args, kwargs):
        """
            Args:
                args: tuple of args
                kwargs: key value dict
            Return:
                res_dict: dict, multi-modal text text, image, audio and video
        """
        res_dict={}
        return res_dict

class DemoAPI(BaseAPI):

    """docstring for ClassName"""
    def __init__(self, configs):
        super(DemoAPI, self).__init__(configs)
        self.name = API_NAME_DEMO

    def api(self, args, kwargs):
        """
            Args:
                args: tuple of args,  (input)
                kwargs: key value dict
            Return:
                res_dict: dict, multi-modal text text, image, audio and video
        """
        api_input = ""
        if len(args) > 0:
            api_input = args[1]

        res_dict = {}
        res_dict["output"] = api_input
        return res_dict
