from src.generator import FunctionCallGenerator
from src.models import FunctionDefinition

functions = []

generator = FunctionCallGenerator(model=None, functions=functions)

print(generator.generate_result("What is the sum of 2 and 3?"))
print(generator.generate_result("Greet john"))
print(generator.generate_result("Reverse the string 'hello'"))
print(generator.generate_result("Hi soukaina"))
print(generator.generate_result("Hello girl"))
print(generator.generate_result("add 5 to 6 8 75"))

