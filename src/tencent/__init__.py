# -*- coding: utf-8 -*-
# @Time    : 2024/06/27

import os
import pkg_resources

from .base import *
from .contrib.api.stock_price_api import *
from .contrib.api.dialogue_visualization_api import *

from .utils.data_utils import *

def api(api_name, *args, **kwargs):
    """
        Args:
            api_name = ""
    """
    api_cls = BaseAPI(None)
    res_dict = {}
    try:
        if api_name in SUPPORTED_APIS:
            attrs = SUPPORTED_APIS[api_name]
            api_cls_name = attrs[KEY_IMPL] if KEY_IMPL in attrs else None
            if api_cls_name is not None:
                api_cls = api_cls_name(None)
                res_dict = api_cls.api(args, kwargs)
        else:
            print ("WARN: Input API NAME %s not supported" % api_name)
    except Exception as e:
        print (e)
    return res_dict

## API Registered Dict
SUPPORTED_APIS = {}
SUPPORTED_APIS[DemoAPI(None).name] = {KEY_IMPL: DemoAPI}
SUPPORTED_APIS[TencentStockPriceAPI(None).name] = {KEY_IMPL: TencentStockPriceAPI} 
SUPPORTED_APIS[DialogueVisualizationAPI(None).name] = {KEY_IMPL: DialogueVisualizationAPI} 

def greeting():
    """
        https://setuptools.pypa.io/en/latest/userguide/datafiles.html
    """
    import random
    from importlib.resources import files
    data_folder_path = str(files('tencent.data.greeting'))
    data_files = os.listdir(data_folder_path)
    screen_greeting_data_list=[]
    for filename in data_files:
        if filename.endswith('.txt'):
            data_path = os.path.join(data_folder_path, filename)
            # print ("DEBUG: Loading Data from File Path %s" % data_path)
            screen_greeting_data = read_data(data_path)
            screen_greeting_data_list.append(screen_greeting_data)
    index = random.randint(0,1)
    start_screen = screen_greeting_data_list[index]
    for line in start_screen:
        print (line)
    print ("Contributing API to tencent pypi package, Visit Github %s or the Developing Forum %s" % (START_SCREEN_CONTRIBE_GITHUB, START_SCREEN_CONTRIBE_FORUM))

## start
if START_SCREEN_ENABLE:
    greeting()
