"""
All tools that may be passed into an LLM instance.

If the file gets too large, break functions into sub-modules and export from here."""

from typing import Optional

from langchain_core.callbacks import (
    AsyncCallbackManagerForToolRun,
    CallbackManagerForToolRun,
)
from langchain_core.tools import BaseTool, tool
from langchain_core.tools.base import ArgsSchema
from langchain_community.tools import TavilySearchResults

from src.data_models import MultiplierInput


@tool
async def amultiply(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b


class CustomMultiplierTool(BaseTool):
    """EXAMPLE: A custom LLM tool that extends LangChain's
    [`BaseTool`](https://python.langchain.com/docs/how_to/custom_tools/#subclass-basetool).

    Note: `BaseTool` is a Pydantic class and requires type definitions for all fields"""

    name: str = "Multiplier"
    description: str = "useful for when you need to answer questions about math"
    args_schema: Optional[ArgsSchema] = MultiplierInput
    return_direct: bool = True

    def _run(
        self, a: int, b: int, run_manager: Optional[CallbackManagerForToolRun] = None
    ) -> str:
        """Use the tool."""
        return a * b

    async def _arun(
        self,
        a: int,
        b: int,
        run_manager: Optional[AsyncCallbackManagerForToolRun] = None,
    ) -> str:
        """Use the tool asynchronously. If the calculation is not cheap, delete this `_arun` method
        and use the sync method, since LangChain will provide a better async implementation.
        """
        return self._run(a, b, run_manager=run_manager.get_sync())


tavily_search = TavilySearchResults(max_results=2)
