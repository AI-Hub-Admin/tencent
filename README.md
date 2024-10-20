# package: tencent

*** IMPORTANT LEGAL DISCLAIMER ***

"tencent" python package is not affiliated, endorsed, or vetted by Tencent Corporation. It's an open-source pakcage and crowd contributed API Wrapper of public available tencent products and services to help developers deploy and use these product or services easier. This package name is originally intended to serve as "ten cent(s)" or "one dime", quoted from one ex-Tencent-er.


Contributing API Wrapper to tencent pypi package, Visit Github [tencent package Github repo](https://github.com/AI-Hub-Admin/tencent) and follow the guidelines on forum [Tencent Pypi Developing Forum deepnlp.org](http://www.deepnlp.org/blog?category=tencent).


## Public Available API Wrappers

|  API NAME  | FUNCTIONS |  Status  |
|  -------- | --------  | --------  |
|  greeting  |  Greeting when import package |   Prod |
|  stock_price  |  Fetch Tencent Stock Price (HKEX: 700) Realtime Quote |   Prod     |
|  WechatServerVeriAPI  |  Wechat Server Verification 微信公众号订阅号服务器验证  |   Prod  |
|  WechatTextReplyBaseAPI  |  Wechat Message Text Reply 处理微信用户文本输入API的基类  |   Prod  |
|  WechatImageReplyBaseAPI  | Wechat Message Image Reply   处理微信用户图像输入基类API 基类 |   Prod  |


## Install
```
pip install tencent
```


## Usage

### Package Import Greeting
```
import tencent

tencent.greeting()

```
![tencent python package pony ma greeting preview](https://github.com/AI-Hub-Admin/tencent/blob/main/docs/greeting_ponyma.jpg?raw=true)


* note: if you want to display the greeting, just set variable START_SCREEN_ENABLE in constants.py to False



### Tencent(HKEX: 700) Stock Price Quote

```
import tencent

stock_dict = tencent.api("stock_price")
keys=["symbol", "avg_price", "high", "low", "change", "update_time", "market_capitalization", "source"]
print ("#### Tencent Stock Price #### ")
for key in keys:
    if key in stock_dict:
        print (key + "|" + stock_dict[key])
    else:
    	print (key + "|" + "")
```

Output

```
    symbol|700
    avg_price|420.400 HKD
    high|424.600 HKD
    low|412.600 HKD
    change|+3.400
    update_time|16 Oct 2024 09:36
    market_capitalization|3,901.15 B HKD
    source|HKEX, https://www.hkex.com.hk/Market-Data/Securities-Prices/Equities/Equities-Quote?sym=700&sc_lang=en
```


### Wechat Public Account Backend Automatic Reply 

微信公众号后台，python服务自动回复(文本/图像/语音)，一键验证和服务部署，依赖Flask的python框架

see /examples/wechat/main.py


```
    # start flask server backend
    python ./examples/wechat/main.py
```


执行效果

![tencent wechat backend](https://github.com/AI-Hub-Admin/tencent/blob/main/docs/wechat_account_autoreply.png?raw=true)



### Open AI Completions APIs and pass Tencent APIs as function Schema

see /tests/test_agent_api_tools.py for more details

```


import json
import tencent
from tencent.utils.agent_utils import function_to_schema

def tencent_api_base(arg1, arg2, arg3, arg4="value4", arg5 = "value5"):
    result = tencent.api("api_base", arg1, arg2, arg3, arg4=arg4, arg5 = arg5)
    print ("DEBUG: tencent_api_base result %s" % str(result))
    return result

def prepare_agent_api_schema():
    tools = [tencent_api_base]

    tool_schemas = [function_to_schema(tool) for tool in tools]
    print ("DEBUG: Agent API Schema")
    [print(json.dumps(schema, indent=2)) for schema in tool_schemas]
    
    return tool_schemas

prepare_agent_api_schema()


def call_openai_api_tools():
    """
        swarm, need openai keys
    """
    tool_schemas = prepare_agent_api_schema()

    response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": "Calling Tencent Service and Return Results"}],
                tools=tool_schemas,
            )
    message = response.choices[0].message
    message.tool_calls[0].function


call_openai_api_tools()

```




##### Blogs
[Tencent Python Package Contributing General Guidelines](http://www.deepnlp.org/blog/tencent-python-package-contributing-general-guidelines)
[Introduction to multimodal generative models](http://www.deepnlp.org/blog/introduction-to-multimodal-generative-models) <br>
[Generative AI Search Engine Optimization](http://www.deepnlp.org/blog/generative-ai-search-engine-optimization-how-to-improve-your-content) <br>
[AI Image Generator User Reviews](http://www.deepnlp.org/store/image-generator) <br>
[AI Video Generator User Reviews](http://www.deepnlp.org/store/video-generator) <br>
[AI Chatbot & Assistant Reviews](http://www.deepnlp.org/store/chatbot-assistant) <br>
[Best AI Tools User Reviews](http://www.deepnlp.org/store/pub/) <br>


## Related
### AI Services Reviews and Ratings <br>
[AI & Robotics User Reviews](http://www.deepnlp.org/store/) <br>
[AI & Robotics Best AI Tools List](http://www.deepnlp.org/store/pub/) <br>
##### Chatbot
[OpenAI o1 Reviews](http://www.deepnlp.org/store/pub/pub-openai-o1) <br>
[ChatGPT User Reviews](http://www.deepnlp.org/store/pub/pub-chatgpt-openai) <br>
[Gemini User Reviews](http://www.deepnlp.org/store/pub/pub-gemini-google) <br>
[Perplexity User Reviews](http://www.deepnlp.org/store/pub/pub-perplexity) <br>
[Claude User Reviews](http://www.deepnlp.org/store/pub/pub-claude-anthropic) <br>
[Qwen AI Reviews](http://www.deepnlp.org/store/pub/pub-qwen-alibaba) <br>
[Doubao Reviews](http://www.deepnlp.org/store/pub/pub-doubao-douyin) <br>
[ChatGPT Strawberry](http://www.deepnlp.org/store/pub/pub-chatgpt-strawberry) <br>
[Zhipu AI Reviews](http://www.deepnlp.org/store/pub/pub-zhipu-ai) <br>
##### AI Image Generation
[Midjourney User Reviews](http://www.deepnlp.org/store/pub/pub-midjourney) <br>
[Stable Diffusion User Reviews](http://www.deepnlp.org/store/pub/pub-stable-diffusion) <br>
[Runway User Reviews](http://www.deepnlp.org/store/pub/pub-runway) <br>
[GPT-5 Forecast](http://www.deepnlp.org/store/pub/pub-gpt-5) <br>
[Flux AI Reviews](http://www.deepnlp.org/store/pub/pub-flux-1-black-forest-lab) <br>
[Canva User Reviews](http://www.deepnlp.org/store/pub/pub-canva) <br>
##### AI Video Generation
[Luma AI](http://www.deepnlp.org/store/pub/pub-luma-ai) <br>
[Pika AI Reviews](http://www.deepnlp.org/store/pub/pub-pika) <br>
[Runway AI Reviews](http://www.deepnlp.org/store/pub/pub-runway) <br>
[Kling AI Reviews](http://www.deepnlp.org/store/pub/pub-kling-kwai) <br>
[Dreamina AI Reviews](http://www.deepnlp.org/store/pub/pub-dreamina-douyin) <br>
##### AI Education
[Coursera Reviews](http://www.deepnlp.org/store/pub/pub-coursera) <br>
[Udacity Reviews](http://www.deepnlp.org/store/pub/pub-udacity) <br>
[Grammarly Reviews](http://www.deepnlp.org/store/pub/pub-grammarly) <br>
##### Robotics
[Tesla Cybercab Robotaxi](http://www.deepnlp.org/store/pub/pub-tesla-cybercab) <br>
[Tesla Optimus](http://www.deepnlp.org/store/pub/pub-tesla-optimus) <br>
[Figure AI](http://www.deepnlp.org/store/pub/pub-figure-ai) <br>
[Unitree Robotics Reviews](http://www.deepnlp.org/store/pub/pub-unitree-robotics) <br>
[Waymo User Reviews](http://www.deepnlp.org/store/pub/pub-waymo-google) <br>
[ANYbotics Reviews](http://www.deepnlp.org/store/pub/pub-anybotics) <br>
[Boston Dynamics](http://www.deepnlp.org/store/pub/pub-boston-dynamic) <br>
##### AI Visualization Tools
[DeepNLP AI Tools](http://www.deepnlp.org/store/pub/pub-deepnlp-ai) <br>
[Multi-Turn Dialogue Visualization](http://www.deepnlp.org/workspace/dialogue_visualization) <br>
[Multi Asynchronous Agent Visualization](http://www.deepnlp.org/workspace/agent_visualization) <br>
##### AI Widgets
[Apple Glasses](http://www.deepnlp.org/store/pub/pub-apple-glasses) <br>
[Meta Glasses](http://www.deepnlp.org/store/pub/pub-meta-glasses) <br>
[Apple AR VR Headset](http://www.deepnlp.org/store/pub/pub-apple-ar-vr-headset) <br>
[Google Glass](http://www.deepnlp.org/store/pub/pub-google-glass) <br>
[Meta VR Headset](http://www.deepnlp.org/store/pub/pub-meta-vr-headset) <br>
[Google AR VR Headsets](http://www.deepnlp.org/store/pub/pub-google-ar-vr-headset) <br>
##### Social
[Character AI](http://www.deepnlp.org/store/pub/pub-character-ai) <br>
##### Self-Driving
[BYD Seal](http://www.deepnlp.org/store/pub/pub-byd-seal) <br>
[Tesla Model 3](http://www.deepnlp.org/store/pub/pub-tesla-model-3) <br>
[BMW i4](http://www.deepnlp.org/store/pub/pub-bmw-i4) <br>
[Baidu Apollo Reviews](http://www.deepnlp.org/store/pub/pub-baidu-apollo) <br>
[Hyundai IONIQ 6](http://www.deepnlp.org/store/pub/pub-hyundai-ioniq-6) <br>
