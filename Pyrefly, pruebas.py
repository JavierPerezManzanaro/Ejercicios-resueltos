# Example: Basic Type Checking

def greet(name: str) -> str:
  return "Hello, " + name

# This works fine since both "World" is a string and greet expects a string
message = greet("World")

# Pyrefly catches this error before runtime due to a type misatch between 42 and "str"
# Error: Argument of type 'int' is not assignable to parameter of type 'str'
error_message = greet(42)
