# -*- coding: utf-8 -*-
# @Author  : Derek

import tencent

stock_dict = tencent.api("stock_price")
keys=["symbol", "avg_price", "high", "low", "change", "update_time", "market_capitalization", "source"]
print ("#### Tencent Stock Price #### ")
for key in keys:
	print (key + "|" + stock_dict[key])
