# -*- coding: utf-8 -*-
# @Time    : 2024/06/27

import json
import requests
import FinanceAgent as fa


from ...base import BaseAPI
from ...constants import *

class TencentStockPriceAPI(BaseAPI):

    """docstring for ClassName"""
    def __init__(self, configs):
        super(TencentStockPriceAPI, self).__init__(configs)
        self.name = API_NAME_STOCK
        self.symbol_list = ["700"]

    def api(self, args, kwargs):
        """
            Args:
                args: tuple of args,  (input)
                kwargs: key value dict
            Return:
                res_dict: dict
        """
        res_dict = {}
        try:
            stock_json_list = fa.api(symbol_list=self.symbol_list, market="HK")
            if len(stock_json_list) > 0:
                # list of dict stock price info
                res_dict = stock_json_list[0]
            return res_dict
        except Exception as e:
            print (e)
            return res_dict
