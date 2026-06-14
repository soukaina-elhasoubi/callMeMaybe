import json


class JsonState:
    def __init__(self) -> None:
        self.step = 0

    def advance(self) -> None:
        self.step += 1


class ConstrainedDecoder:

    def __init__(self, vocab_path: str) -> None:
        self.vocab_path = vocab_path
        self.vocabulary = self.load_vocabulary()

    def load_vocabulary(self):
        with open(self.vocab_path, "r", encoding="utf-8") as file:
            return json.load(file)

    def get_allowed_tokens(
            self,
            state: JsonState
            ) -> list[str]:

        if state.step == 0:
            return ["{"]

        if state.step == 1:
            return ['"name"']

        if state.step == 2:
            return [":"]

        if state.step == 3:
            return ['"fn_add_numbers']

        if state.step == 4:
            return ["}"]

        return []

    def filter_logits(
            self,
            logits: dict[str, float],
            state: JsonState
            ) -> dict[str, float]:
        allowed = self.get_allowed_tokens(state)
        filtered = {}
        for token, score in logits.items():
            if token in allowed:
                filtered[token] = score
            else:
                filtered[token] = float("-inf")
        return filtered

    def select_best_token(
            self,
            filtered_logits: dict[str, float]
    ) -> str:
        best_token = None
        best_score = float("-inf")

        for token, score in filtered_logits.items():
            if score > best_score:
                best_score = score
                best_token = token

        return best_token

# decoder = ConstrainedDecoder("./test_vocab.json")
# print(decoder.vocabulary)


decoder = ConstrainedDecoder("test_vocab.json")

fake_logits = {
    '"call"': 1.1,
    "{": 1.2,
    '"name"': 5.4,
    "banana": 9.7,
    "}": 3.1
}

state = JsonState()

# print(
#     decoder.get_allowed_tokens(state)
# )

# state.advance()

# print(
#     decoder.get_allowed_tokens(state)
# )

print(
    decoder.filter_logits(
        fake_logits,
        state
    )
)

fake_logits = {
    "{": 1.2,
    '"name"': -float("inf"),
    "banana": -float("inf"),
    "}": -float("inf")
}

print(
    decoder.select_best_token(
        fake_logits
    )
)

for _ in range(6):
    print(f"step: {state.step}",
          decoder.get_allowed_tokens(state)
          )
    state.advance()
state = JsonState()

output = ""

while True:
    allowed = decoder.get_allowed_tokens(state)

    if not allowed:
        break

    output += allowed[0]
    state.advance()

print(output)
