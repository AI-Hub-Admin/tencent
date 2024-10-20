# -*- coding: utf-8 -*-#

from flask import Flask, jsonify, send_from_directory
from flask import request
import traceback
import FinanceAgent as fa

from tencent.contrib.wechat.wechat_api import *
from tencent.contrib.wechat import receive

## setup Flask
app = Flask(__name__, static_folder="static")
app.config["JSON_AS_ASCII"] = False

class WechatTextReplyFinanceAPI(WechatTextReplyBaseAPI):

    @staticmethod
    def static_api(args, kwargs):
        return WechatTextReplyFinanceAPI(None).api(args, kwargs)
    
    def process(self, msg):
        """
            input: msg is a class of Wechat Msg(TextMsg/ImageMsg) defined in receive.py file, you can also access other input information 
                    toUser = msg.FromUserName
                    fromUser = msg.ToUserName
            output: str, the outer api method will process and wrap the Message Object
        """
        input_text = msg.Content
        ## implement_your_code_here
        stock_info_list = fa.api(symbol_list=['700'], market="HK")
        response_list = []
        for stock_info in stock_info_list:
            response = ""
            if len(stock_info) == 0:
                response= "%s，股价: %s, 最高价: %s, 最低价: %s, 数据更新时间: %s, 数据源: %s" % ("-", "-", "-", "-", "-", "-")
            else:
                response= "%s，股价: %s, 最高价: %s, 最低价: %s, 数据更新时间: %s, 数据源: %s" % (stock_info["symbol"], stock_info["avg_price"], stock_info["high"], stock_info["low"], stock_info["update_time"], stock_info["source"])
            response_list.append(response)
        output_text = ";".join(response_list)
        ## end of implementation
        return output_text

@app.route('/wx', methods=['GET', 'POST'])
def main_finance():
    """
        Utils for Wechat backend verification, Support Both GET method for verification, POST method to reply text and image messages.
    """
    try:
        if request.method == "GET":
            return WechatServerVeriAPI.static_api(args=[request], kwargs={})
        elif request.method == 'POST':
            raw_data = request.data
            recMsg = receive.parse_xml(raw_data)
            if isinstance(recMsg, receive.Msg):
                if recMsg.MsgType == 'text':
                    # Change WechatTextReplyBaseAPI to your customized API, e.g. WechatTextReplyFinanceAPI
                    return WechatTextReplyFinanceAPI.static_api(args=[recMsg], kwargs={})
                elif recMsg.MsgType == 'image':
                    return WechatImageReplyBaseAPI.static_api(args=[recMsg], kwargs={})
                else:
                    return "success"
            else:
                return "success"
        else:
            print ("DEBUG: Request Method not supported %s" % request.method)
            return "fail"
    except Exception as e:
        print (e)
        s = traceback.format_exc()
        print (s)            
        return "fail"

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80,debug=True)
