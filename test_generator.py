from src.generator import FunctionCallGenerator
from src.models import (
    FunctionDefinition,
    ParameterDefinition
)

functions = [
    FunctionDefinition(
        name="fn_add_numbers",
        description="add two numbers",
        parameters={
            "a": ParameterDefinition(type="number"),
            "b": ParameterDefinition(type="number")
        }
    )
]

generator = FunctionCallGenerator(
    model=None,
    functions=functions
)

result = generator.generate_result(
    "add 12 and 30"
)

print(result)