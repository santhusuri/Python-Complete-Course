🧩 Level 1 — Python Fundamentals

🧱 Build your foundation in syntax, types, and control flow.

🔹 3. Data Types

Numeric types: int, float, complex

Sequence types: str, list, tuple, range

Mapping types: dict

Set types: set, frozenset

Boolean type: bool

Binary types: bytes, bytearray, memoryview

## Numeric Types

### int (Integer):
- Whole numbers, positive or negative.
- No size limit in Python 3.

```python
x = 5
y = -10
z = 0
```

### float (Floating-point):
- Decimal numbers.
- Represented in scientific notation for large/small numbers.

```python
pi = 3.14159
scientific = 1.23e-4  # 0.000123
```

### complex (Complex Numbers):
- Real and imaginary parts.
- Imaginary part denoted by `j`.

```python
c = 3 + 4j
real_part = c.real  # 3.0
imag_part = c.imag  # 4.0
```

## Sequence Types

### str (String):
- Sequence of characters.
- Immutable.
- Enclosed in single, double, or triple quotes.

```python
single = 'Hello'
double = "World"
triple = """Multi-line
string"""
```

### list:
- Ordered, mutable sequence.
- Can contain mixed types.

```python
my_list = [1, 2, 3, "four", 5.0]
empty_list = []
```

### tuple:
- Ordered, immutable sequence.
- Similar to lists but cannot be modified.

```python
my_tuple = (1, 2, 3)
single_element = (5,)  # Note the comma
```

### range:
- Immutable sequence of numbers.
- Used in loops.

```python
r = range(5)  # 0, 1, 2, 3, 4
r2 = range(1, 10, 2)  # 1, 3, 5, 7, 9
```

## Mapping Types

### dict (Dictionary):
- Unordered collection of key-value pairs.
- Keys must be immutable (str, int, tuple).
- Mutable.

```python
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
empty_dict = {}
```

## Set Types

### set:
- Unordered collection of unique elements.
- Mutable.

```python
my_set = {1, 2, 3, 4}
empty_set = set()  # {} creates dict
```

### frozenset:
- Immutable version of set.

```python
frozen = frozenset([1, 2, 3])
```

## Boolean Type

### bool:
- Represents True or False.
- Subclass of int (True = 1, False = 0).

```python
is_true = True
is_false = False
```

## Binary Types

### bytes:
- Immutable sequence of bytes (0-255).

```python
b = b'hello'
```

### bytearray:
- Mutable version of bytes.

```python
ba = bytearray(b'hello')
ba[0] = 72  # 'H'
```

### memoryview:
- Allows access to internal data of objects supporting buffer protocol.

```python
mv = memoryview(b'hello')
```

## Type Checking

Use `type()` to check variable type:

```python
x = 5
print(type(x))  # <class 'int'>

y = "hello"
print(type(y))  # <class 'str'>
```

Use `isinstance()` for type checking:

```python
isinstance(x, int)  # True
isinstance(y, str)  # True
