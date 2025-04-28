"""Export all LLM instances or agents available in this application.
You may structure the directory in the way that best suits your project."""

# Import relevant functionality
from langchain_anthropic import ChatAnthropic
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import create_react_agent

from src.tools import tavily_search

#  MODEL definitions: please set and use `.env` variables for API keys
anthropic = ChatAnthropic(model_name="claude-3-sonnet-20240229")


# AGENT definitions

memory = MemorySaver()  # debug only!
anthropic_search = create_react_agent(anthropic, [tavily_search], checkpointer=memory)

# EXAMPLE USAGE:
# for step in anthropic_search.stream(
#     {"messages": [HumanMessage(content="hi im bob! and i live in sf")]},
#     {"configurable": {"thread_id": "abc123"}}, # optional thread/session tracker
#     stream_mode="values",
# ):
#     step["messages"][-1].pretty_print()
