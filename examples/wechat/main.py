# -*- coding: utf-8 -*-#
# filename: main.py

from flask import Flask, jsonify, send_from_directory
from flask import request

import traceback
from tencent.contrib.wechat.wechat_api import *
from tencent.contrib.wechat import receive

app = Flask(__name__, static_folder="static")
app.config["JSON_AS_ASCII"] = False

@app.route('/wx_home')
def index():
    """
        Homepage for wechat backend
        URL: http://127.0.0.1/wx_home
    """
    return '<h1>Hello World!</h1>'

@app.route('/wx', methods=['GET', 'POST'])
def main_api():
    """
        Utils for Wechat backend verification, Note Wechat set: GET request, not post request
    """
    try:
        if request.method == "GET":
            return WechatServerVeriAPI.static_api(args=[request], kwargs={})
        elif request.method == 'POST':
            raw_data = request.data
            recMsg = receive.parse_xml(raw_data)
            if isinstance(recMsg, receive.Msg):
                if recMsg.MsgType == 'text':
                    return WechatTextReplyBaseAPI.static_api(args=[recMsg], kwargs={})
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
