# -*- coding: utf-8 -*-#
# filename: main.py

import traceback
import hashlib

from ...base import BaseAPI
from ..wechat import reply
from .wechat_constants import *

class WechatServerVeriAPI(BaseAPI):

    @staticmethod
    def static_api(args, kwargs):
        return WechatServerVeriAPI(None).api(args, kwargs)

    def api(self, args, kwargs):
        """
            args tuple of variables
                request: flask request
                微信验证: GET Method, 字段: signature, echostr, nonce, timestamp
                ## 输入: token, timestamp, nonce, 验证通过本地的 hashcode == signature，如果通过就把回文回传给微信的服务器，证明服务器是公众号拥有的。
                ## 本例子中输入后台token 为 "dummy" 为例, 本地发起 请求，检查是否通过 GET 方法, 如果需要修改可以修改 wechat_constants.py 文件
            kwargs: dict of variables
        """
        if len(args) == 0:
            return WECHAT_RESPONSE_FAIL
        try:
            request = args[0]

            url_values = request.values
            signature = url_values["signature"]
            timestamp = url_values["timestamp"]
            nonce = url_values["nonce"]
            echostr = url_values["echostr"]
            token = WECHAT_BACKEND_TOKEN
            list = [token, timestamp, nonce]
            list.sort()
            sha1 = hashlib.sha1()
            sha1.update(list[0].encode('utf-8'))
            sha1.update(list[1].encode('utf-8'))
            sha1.update(list[2].encode('utf-8'))
            hashcode = sha1.hexdigest()
            print ("handle/GET input data: signature %s, timestamp %s, nonce %s, echostr %s" % (signature, timestamp, nonce, echostr))
            print ("handle/GET func: hashcode %s, signature: %s" % (hashcode, signature))
            if hashcode == signature:
                return echostr
            else:
                return ""
        except Exception as e:
            print ("DEBUG: Failed to process WechatServerVeriAPI...")
            print (e)
            s = traceback.format_exc()
            print (s)            
            return ""

class WechatTextReplyBaseAPI(BaseAPI):

    @staticmethod
    def static_api(args, kwargs):
        return WechatTextReplyBaseAPI(None).api(args, kwargs)

    def api(self, args, kwargs):
        """
            args: Msg obj
        """
        if len(args) == 0:
            return WECHAT_RESPONSE_FAIL
        recMsg = args[0]
        toUser = recMsg.FromUserName
        fromUser = recMsg.ToUserName
        content = self.process(recMsg)
        replyMsg = reply.TextMsg(toUser, fromUser, content)
        return replyMsg.send()

    def process(self, msg):
        """ process text request
        """
        input_text = msg.Content
        return MSG_AUTO_REPLY_TEXT

class WechatImageReplyBaseAPI(BaseAPI):

    @staticmethod
    def static_api(args, kwargs):
        return WechatImageReplyBaseAPI(None).api(args, kwargs)

    def api(self, args, kwargs):
        """
            args: Msg obj
            return:
                reply the same image that users send to wechat public account backend
        """
        if len(args) == 0:
            return WECHAT_RESPONSE_FAIL
        recMsg = args[0]
        mediaId = self.process(recMsg)
        toUser = recMsg.FromUserName
        fromUser = recMsg.ToUserName
        replyMsg = reply.ImageMsg(toUser, fromUser, mediaId)
        return replyMsg.send()

    def process(self, msg):
        """ process text request
        """
        mediaId = msg.MediaId
        return mediaId
