## Example 1: 拆箱即用的"微信公众号/订阅号"服务python服务端代码

### Install
```
pip install Flask, tencent
```


### Run the server and deploy service at 80 port
```
python3 main.py
```

Visit Local Browser, you can see hello world of the service
http://127.0.0.1:80/wx_home


#### Use Curl to test local service
```
signature=xxxx
echostr=xxxx
timestamp=xxxx
nouce=xxxxx

curl "http://127.0.0.1:80/wx?signature=${signature}&echostr=${echostr}&timestamp=${timestamp}&nonce=${nouce}"
```

## Example 2: 打造查询股价的个人金融助理

```
python3 main_finance_agent.py
```

