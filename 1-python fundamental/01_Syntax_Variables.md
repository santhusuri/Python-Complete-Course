🧩 Level 1 — Python Fundamentals

🧱 Build your foundation in syntax, types, and control flow.

🔹 2. Basic Syntax and Variables

Comments, indentation, naming conventions

Keywords & identifiers

Variables and assignment

Dynamic typing

Multiple assignment & unpacking

## Comments, Indentation, Naming Conventions

### Comments:
- Single-line: `# This is a comment`
- Multi-line: Use triple quotes `"""` or `'''` for docstrings.

```python
# Single-line comment
"""
Multi-line comment
or docstring
"""
```

### Indentation:
- Python uses indentation (spaces or tabs) to define code blocks.
- Consistent indentation is crucial (4 spaces recommended).
- Incorrect indentation causes `IndentationError`.

```python
if True:
    print("Indented block")
```

### Naming Conventions:
- Variables: `snake_case` (e.g., `my_variable`)
- Constants: `UPPER_CASE` (e.g., `PI = 3.14`)
- Functions: `snake_case` (e.g., `calculate_sum`)
- Classes: `PascalCase` (e.g., `MyClass`)

## Keywords & Identifiers

### Keywords:
Reserved words with special meanings. Cannot be used as identifiers.

List of keywords (Python 3.11):
```
False      await      else       import     pass
None       break      except     in         raise
True       class      finally    is         return
and        continue   for        lambda     try
as         def        from       nonlocal   while
assert     del        global     not        with
async      elif       if         or         yield
```

### Identifiers:
Names for variables, functions, classes, etc.
- Start with letter or underscore.
- Can contain letters, digits, underscores.
- Case-sensitive.
- Cannot be keywords.

Valid: `var1`, `_private`, `myVar`
Invalid: `1var`, `for`, `my-var`

## Variables and Assignment

### Variables:
- Containers for storing data values.
- No need to declare type (dynamic typing).
- Assigned using `=`.

```python
x = 5
name = "Alice"
```

### Dynamic Typing:
- Variable type determined at runtime.
- Can reassign to different types.

```python
x = 10      # int
x = "hello" # str
```

## Multiple Assignment & Unpacking

### Multiple Assignment:
Assign multiple variables in one line.

```python
a, b, c = 1, 2, 3
```

### Unpacking:
Assign elements of iterable to variables.

```python
# List unpacking
x, y, z = [1, 2, 3]

# Tuple unpacking
a, b = (4, 5)

# String unpacking
p, q, r = "abc"

# Extended unpacking (Python 3)
first, *middle, last = [1, 2, 3, 4, 5]
# first=1, middle=[2,3,4], last=5
```

### Swapping Variables:
```python
a, b = b, a  # Swap a and b
