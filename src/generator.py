from typing import Any, Dict, List
# import re

from .models import FunctionDefinition


class FunctionCallGenerator:
    def __init__(
        self,
        model: Any,
        functions: List[FunctionDefinition]
    ) -> None:
        self.model = model
        self.functions = functions

    def _choose_function(
            self,
            prompt: str
    ) -> str:
        prompt_words = set(
            prompt.lower().split()
        )

        best_score = 0
        best_fn = ""

        for fn in self.functions:
            desc_words = set(
                fn.description.lower().split()
            )

            score = len(prompt_words & desc_words)
            if score > best_score:
                best_score = score
                best_fn = fn.name
        return best_fn

    def _extract_parameters(
            self,
            prompt: str,
            function_name: str
    ) -> Dict[str, Any]:
    
        definition = None

        for fn in self.functions:
            if fn.name == function_name:
                definition = fn
                break

        if definition is None:
            return {}

        result = {}

        for param_name, param_def in definition.parameters.items():
            print(
                param_name,
                param_def.type
            )
        return result

    def generate_result(self, prompt: str) -> Dict[str, Any]:
        function_name = self._choose_function(prompt)

        parameters = self._extract_parameters(prompt, function_name)

        return {
            "name": function_name,
            "parameters": parameters
        }
        # prompt_lower = prompt.lower()

        # # 1. SUM FUNCTION
        # if "sum" in prompt_lower or "add" in prompt_lower:
        #     numbers = re.findall(r"-?\d+\.?\d*", prompt)

        #     if len(numbers) >= 2:
        #         return {
        #             "name": "fn_add_numbers",
        #             "parameters": {
        #                 "a": float(numbers[0]),
        #                 "b": float(numbers[1])
        #             }
        #         }

        # # 2. GREET FUNCTION
        # if "greet" or "hi" or "hello" in prompt_lower:
        #     words = prompt.split()
        #     name = words[-1]

        #     return {
        #         "name": "fn_greet",
        #         "parameters": {
        #             "name": name
        #         }
        #     }

        # # 3. REVERSE STRING
        # if "reverse" in prompt_lower:
        #     match = re.search(r"'(.*?)'", prompt)

        #     if match:
        #         text = match.group(1)
        #     else:
        #         text = prompt.split()[-1]

        #     return {
        #         "name": "fn_reverse_string",
        #         "parameters": {
        #             "s": text
        #         }
        #     }

        # # FALLBACK
        # return {
        #     "name": "",
        #     "parameters": {}
        # }

        # def _choose_function(
        # self,
        # prompt: str
        # ) -> str:

        #     prompt_words = set(
        #         prompt.lower().split()
        #     )

        #     best_function = ""
        #     best_score = 0

        #     for fn in self.functions:

        #         description_words = set(
        #             fn.description.lower().split()
        #         )

        #         score = len(
        #             prompt_words &
        #             description_words
        #         )

        #         if score > best_score:
        #             best_score = score
        #             best_function = fn.name

        #     return best_function
# generator.generate_result(
#     "add 12 and 30"
# )