from typing import Dict, Literal

from pydantic import BaseModel


class ParameterDefinition(BaseModel):
    type: Literal["string", "number", "boolean"]


class ReturnDefinition(BaseModel):
    type: Literal["string", "number", "boolean"]
    # a  : int|bool|str


class FunctionDefinition(BaseModel):
    name: str
    description: str
    parameters: Dict[str, ParameterDefinition]
    returns: ReturnDefinition


class FunctionCallRequest(BaseModel):
    prompt: str
