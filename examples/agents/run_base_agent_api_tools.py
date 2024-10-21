# -*- coding: utf-8 -*-

import os
import json
import tencent
from tencent.utils.agent_utils import function_to_schema

def tencent_api_base(arg1, arg2, arg3, arg4="value4", arg5 = "value5"):
    result = tencent.api("api_base", arg1, arg2, arg3, arg4=arg4, arg5 = arg5)
    print ("DEBUG: tencent_api_base result %s" % str(result))
    return result

def execute_tool_call(tool_call, tools_map):
    name = tool_call.function.name
    args = json.loads(tool_call.function.arguments)
    print (f"Assistant: {name}({args})")
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

def call_base_agent_api_tools():

    tools = [tencent_api_base]

    tool_schemas = [function_to_schema(tool) for tool in tools]
    print ("DEBUG: Agent API Schema")
    [print(json.dumps(schema, indent=2)) for schema in tool_schemas]

    ## construct request
    instruction = "You can fill the function with json format, the schema for the function is %s, the inputs including arg1=10, arg2=20, arg3=30,please output the executable function values in json format, with key as 'function'"
    
    prompt_list = []
    for tool in tool_schemas:
        prompt =instruction % str(tool)
        prompt_list.append(prompt)
    final_prompt = "".join(prompt_list)
    print ("DEBUG: Prompt %s" % final_prompt)

    ## Output
    functions_input = input("Input Functions:")
    print ("DEBUG: Input Function %s" % str(functions_input))

    ## start LLM Calling
    
    ## end of LLM Calling
    ## save the LLM returned function name and function values
    openai_tools_call_json = '{"function":{"name":"tencent_api_base","parameters":{"arg1":"10","arg2":"20","arg3":"30","arg4":"","arg5":""}}}'
    tool_call = json.loads(openai_tools_call_json)
    tools_map = {tool.__name__: tool for tool in tools}

    # execute_tool_call(tool_call, tools_map)
    execute_tool_call_from_json(tool_call, tools_map)

def main():
    call_base_agent_api_tools()

if __name__ == '__main__':
    main()
