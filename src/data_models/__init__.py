"""All Pydantic subclasses that are used by the application. This excludes custom tool definitions,
as the models here may be used by Tools as inputs or response-schemas"""

from pydantic import BaseModel, Field


class MultiplierInput(BaseModel):
    """Argument input for `CustomBaseMultiplierTool` tool"""

    a: int = Field(description="first number")
    b: int = Field(description="second number")
