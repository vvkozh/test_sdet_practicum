
def choose_largest_tool(received_tools):
    tools = received_tools.split('\n')
    largets_tool = tools[0]
    for tool in tools:
        if len(largets_tool) < len(tool):
            largets_tool = tool
    return largets_tool

def count_tolls(received_tools):
    tools = received_tools.split('\n')
    return len(tools)


