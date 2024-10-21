# -*- coding: utf-8 -*-

import os
import json
import tencent
from tencent.utils.agent_utils import function_to_schema

def execute_tool_call(tool_call, tools_map):
    name = tool_call.function.name
    args = json.loads(tool_call.function.arguments)
    print(f"Assistant: {name}({args})")
    # call corresponding function with provided arguments
    return tools_map[name](**args)

def execute_tool_call_from_json(tool_call, tools_map):
    """
        tool_call: json format of 
        {'functions': {'name': 'tencent_api_base',
          'parameters': {'arg1': '10',
           'arg2': '20',
           'arg3': '30',
           'arg4': '',
           'arg5': ''}}}
    """
    name = tool_call["function"]["name"]
    parameters = tool_call["function"]["parameters"]
    # args = json.loads(tool_call.function.arguments)
    print(f"Assistant: {name}({parameters})")
    # call corresponding function with provided arguments
    return tools_map[name](**parameters)

## FinanceAgentTools
def finance_stock_price_api(symbol_list: list, market: str):
    """
        symbol_list is list of json
        market is str
    """
    import FinanceAgent as fa
    stock_info_json = fa.api(symbol_list=symbol_list, market=market)
    return stock_info_json

def call_finance_api_agent_tools():
    """
        Reference: https://cookbook.openai.com/examples/orchestrating_agents
    """
    tools = [finance_stock_price_api]

    tool_schemas = [function_to_schema(tool) for tool in tools]
    print ("DEBUG: Agent API Schema:")
    [print(json.dumps(schema, indent=2)) for schema in tool_schemas]

    # history message
    user_input = "I am interested in Tencent(code:700) and Kuaishou (code:1024) stock price"

    ## construct request
    instruction = "You can fill the function with json format, the schema for the function is %s, the inputs includes %s,please output the executable function values in json format, with key as 'function'"
    
    prompt_list = []
    for tool in tool_schemas:
        prompt =instruction % (str(tool), str(user_input))
        prompt_list.append(prompt)
    final_prompt = "".join(prompt_list)
    print (final_prompt)
    ## Call LLM API to fill the functions


    ## Output
    functions_input = input("Input Functions:")
    print (functions_input)
    
    ## start LLM Calling
    tools_map = {tool.__name__: tool for tool in tools}
    messages = []
    key = os.environ.get("OPENAI_API_KEY")
    if key is not None:
        # set openai variable
        from openai import OpenAI
        from pydantic import BaseModel
        from typing import Optional
        client = OpenAI() 
        response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[{"role": "user", "content": instruction}],
                    tools=tool_schemas,
                )
        message = response.choices[0].message
        message.tool_calls[0].function

        tool_calls = message.tool_calls
        for tool_call in tool_calls:
            result = execute_tool_call(tool_call, tools_map)
            messages.append(result)
    else:
        openai_tools_call_json_list = '[{"function":{"name":"finance_stock_price_api","parameters":{"symbol_list":["700","1024"],"market":"HK"}}}]'
        tool_calls = json.loads(openai_tools_call_json_list)
        for tool_call in tool_calls:
            tool_call_result = execute_tool_call_from_json(tool_call, tools_map)
            messages.append(tool_call_result)
    # output messages
    print(messages)
    return messages

def main():
    call_finance_api_agent_tools()

if __name__ == '__main__':
    main()
