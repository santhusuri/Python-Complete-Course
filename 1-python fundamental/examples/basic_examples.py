"""
Basic Examples for Python Fundamentals Level 1

This file contains practical examples demonstrating concepts from all sections:
1. Introduction to Python
2. Basic Syntax and Variables
3. Data Types
4. Type Casting and Input/Output
5. Operators
"""

# Section 1: Introduction to Python
print("=== Section 1: Introduction to Python ===")

# Running Python scripts (this is a script!)
print("Hello, World!")

# Interactive shell example (commented out for script execution)
# >>> import this

# Section 2: Basic Syntax and Variables
print("\n=== Section 2: Basic Syntax and Variables ===")

# Comments
# This is a single-line comment
"""
This is a multi-line comment
or docstring
"""

# Variables and assignment
name = "Alice"
age = 30
height = 5.6

print(f"Name: {name}, Age: {age}, Height: {height}")

# Dynamic typing
x = 10
print(f"x is {x}, type: {type(x)}")
x = "hello"
print(f"x is {x}, type: {type(x)}")

# Multiple assignment
a, b, c = 1, 2, 3
print(f"a={a}, b={b}, c={c}")

# Unpacking
first, *middle, last = [1, 2, 3, 4, 5]
print(f"first={first}, middle={middle}, last={last}")

# Swapping
a, b = b, a
print(f"After swap: a={a}, b={b}")

# Section 3: Data Types
print("\n=== Section 3: Data Types ===")

# Numeric types
int_num = 42
float_num = 3.14159
complex_num = 2 + 3j

print(f"Integer: {int_num}, Float: {float_num}, Complex: {complex_num}")

# Sequence types
my_string = "Hello, Python!"
my_list = [1, 2, 3, "four", 5.0]
my_tuple = (1, 2, 3)
my_range = range(5)

print(f"String: {my_string}")
print(f"List: {my_list}")
print(f"Tuple: {my_tuple}")
print(f"Range: {list(my_range)}")

# Mapping type
my_dict = {"name": "Bob", "age": 25, "city": "London"}
print(f"Dictionary: {my_dict}")

# Set types
my_set = {1, 2, 3, 4, 4}  # Duplicates removed
my_frozenset = frozenset([1, 2, 3])
print(f"Set: {my_set}")
print(f"Frozenset: {my_frozenset}")

# Boolean type
is_python_fun = True
is_hard = False
print(f"Is Python fun? {is_python_fun}")
print(f"Is it hard? {is_hard}")

# Binary types
my_bytes = b'hello'
my_bytearray = bytearray(b'world')
my_memoryview = memoryview(my_bytes)
print(f"Bytes: {my_bytes}")
print(f"Bytearray: {my_bytearray}")
print(f"Memoryview: {my_memoryview[0]}")

# Section 4: Type Casting and Input/Output
print("\n=== Section 4: Type Casting and Input/Output ===")

# Type conversions
num_str = "42"
num_int = int(num_str)
num_float = float(num_str)
back_to_str = str(num_int)

print(f"String '{num_str}' -> int {num_int} -> float {num_float} -> string '{back_to_str}'")

# String formatting
name = "Charlie"
age = 35

# f-strings
print(f"Hello, my name is {name} and I am {age} years old.")

# format() method
print("Hello, my name is {} and I am {} years old.".format(name, age))

# % operator
print("Hello, my name is %s and I am %d years old." % (name, age))

# Custom print
print("Multiple", "items", sep=" | ", end="!\n")

# Section 5: Operators
print("\n=== Section 5: Operators ===")

# Arithmetic operators
a, b = 10, 3
print(f"a={a}, b={b}")
print(f"Addition: {a + b}")
print(f"Subtraction: {a - b}")
print(f"Multiplication: {a * b}")
print(f"Division: {a / b}")
print(f"Floor Division: {a // b}")
print(f"Modulus: {a % b}")
print(f"Exponentiation: {a ** b}")

# Comparison operators
print(f"a == b: {a == b}")
print(f"a != b: {a != b}")
print(f"a > b: {a > b}")
print(f"a < b: {a < b}")

# Logical operators
x, y = True, False
print(f"x={x}, y={y}")
print(f"x and y: {x and y}")
print(f"x or y: {x or y}")
print(f"not x: {not x}")

# Assignment operators
z = 5
print(f"Initial z: {z}")
z += 3
print(f"After z += 3: {z}")
z *= 2
print(f"After z *= 2: {z}")

# Identity operators
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1
print(f"list1 is list2: {list1 is list2}")  # False
print(f"list1 is list3: {list1 is list3}")  # True
print(f"list1 == list2: {list1 == list2}")  # True

# Membership operators
my_list = [1, 2, 3, 4, 5]
print(f"3 in my_list: {3 in my_list}")
print(f"6 in my_list: {6 in my_list}")
print(f"3 not in my_list: {3 not in my_list}")

# Operator precedence
result1 = 2 + 3 * 4
result2 = (2 + 3) * 4
print(f"2 + 3 * 4 = {result1}")
print(f"(2 + 3) * 4 = {result2}")

print("\n=== End of Examples ===")
