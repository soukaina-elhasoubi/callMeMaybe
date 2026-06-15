def _choose_function(self, prompt: str) -> str:
    best_fn = None
    best_score = float("-inf")

    prompt_ids = self.model.encode(prompt)

    for fn in self.functions:
        function_text = f"{fn.name}. {fn.description}"
        function_ids = self.model.encode(function_text)

        # concat prompt + function description
        input_ids = prompt_ids.tolist() + function_ids.tolist()

        logits = self.model.get_logits_from_input_ids(input_ids)

        score = sum(logits)  # approximation simple mais LLM-driven

        if score > best_score:
            best_score = score
            best_fn = fn.name

    return best_fn