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
