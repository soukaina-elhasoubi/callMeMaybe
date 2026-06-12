from typing import Any, Dict, List
import re

from .models import FunctionDefinition


class FunctionCallGenerator:
    def __init__(
        self,
        model: Any,
        functions: List[FunctionDefinition]
    ) -> None:
        self.model = model
        self.functions = functions

    def generate_result(self, prompt: str) -> Dict[str, Any]:
        prompt_lower = prompt.lower()

        # 1. SUM FUNCTION
        if "sum" in prompt_lower or "add" in prompt_lower:
            numbers = re.findall(r"-?\d+\.?\d*", prompt)

            if len(numbers) >= 2:
                return {
                    "name": "fn_add_numbers",
                    "parameters": {
                        "a": float(numbers[0]),
                        "b": float(numbers[1])
                    }
                }

        # 2. GREET FUNCTION
        if "greet" or "hi" or "hello" in prompt_lower:
            words = prompt.split()
            name = words[-1]

            return {
                "name": "fn_greet",
                "parameters": {
                    "name": name
                }
            }

        # 3. REVERSE STRING
        if "reverse" in prompt_lower:
            match = re.search(r"'(.*?)'", prompt)

            if match:
                text = match.group(1)
            else:
                text = prompt.split()[-1]

            return {
                "name": "fn_reverse_string",
                "parameters": {
                    "s": text
                }
            }

        # FALLBACK
        return {
            "name": "",
            "parameters": {}
        }
