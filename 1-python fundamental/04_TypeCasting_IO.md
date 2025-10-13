# Type Casting and Input/Output

## input() and print() Functions

### input() Function:
- Reads user input from the console.
- Always returns a string.
- Can take an optional prompt message.

```python
# Basic input
name = input()
print("Hello,", name)

# Input with prompt
name = input("Enter your name: ")
print("Hello,", name)
```

### print() Function:
- Outputs data to the console.
- Can print multiple items separated by spaces.
- Default separator is space, default end is newline.

```python
print("Hello, World!")  # Basic print
print("Hello", "World", sep="-")  # Custom separator: Hello-World
print("Hello", end=" ")  # No newline
print("World")  # Continues on same line
```

## String Formatting

### f-strings (Python 3.6+):
- Modern, readable way to format strings.
- Embed expressions inside string literals.

```python
name = "Alice"
age = 30
print(f"My name is {name} and I am {age} years old.")

# Expressions in f-strings
x = 5
y = 10
print(f"The sum of {x} and {y} is {x + y}.")
```

### format() Method:
- Older method for string formatting.
- Uses placeholders `{}`.

```python
name = "Bob"
age = 25
print("My name is {} and I am {} years old.".format(name, age))

# Named placeholders
print("My name is {name} and I am {age} years old.".format(name="Charlie", age=35))
```

### % Operator (Old-style):
- C-style string formatting.

```python
name = "David"
age = 40
print("My name is %s and I am %d years old." % (name, age))
```

## Type Conversions

Convert between different data types.

### int():
- Convert to integer.

```python
int("42")        # 42
int(3.14)        # 3 (truncates)
int(True)        # 1
int(False)       # 0
```

### str():
- Convert to string.

```python
str(42)          # "42"
str(3.14)        # "3.14"
str([1, 2, 3])   # "[1, 2, 3]"
```

### float():
- Convert to float.

```python
float("3.14")    # 3.14
float(42)        # 42.0
float("42")      # 42.0
```

### bool():
- Convert to boolean.

```python
bool(0)          # False
bool(1)          # True
bool("")         # False
bool("hello")    # True
bool([])         # False
bool([1, 2])     # True
```

### list(), tuple(), set():
- Convert to respective types.

```python
list("abc")      # ['a', 'b', 'c']
tuple([1, 2, 3]) # (1, 2, 3)
set([1, 2, 2, 3]) # {1, 2, 3}
```

## Handling Input Conversion

Since `input()` always returns a string, convert as needed:

```python
# Get integer input
age = int(input("Enter your age: "))

# Get float input
height = float(input("Enter your height in meters: "))

# Get multiple inputs
x, y = map(int, input("Enter two numbers: ").split())
```

## Output Formatting Examples

```python
# Aligning text
print("{:<10} {:<10} {:<10}".format("Name", "Age", "City"))
print("{:<10} {:<10} {:<10}".format("Alice", 30, "NYC"))

# Number formatting
pi = 3.14159265359
print(f"Pi to 2 decimal places: {pi:.2f}")
print(f"Pi in scientific notation: {pi:.2e}")

# Padding with zeros
print(f"Number: {42:05d}")  # 00042
```

## Error Handling in Type Conversion

Use try-except for safe conversion:

```python
try:
    num = int(input("Enter a number: "))
    print(f"You entered: {num}")
except ValueError:
    print("That's not a valid number!")
