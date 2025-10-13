🧩 Level 1 — Python Fundamentals

🧱 Build your foundation in syntax, types, and control flow.

🔹 5. Operators

Arithmetic, Assignment, Comparison

Logical and Bitwise operators

Identity (is) and Membership (in)

## Arithmetic Operators

Perform mathematical operations:

```python
a = 10
b = 3

print(a + b)  # Addition: 13
print(a - b)  # Subtraction: 7
print(a * b)  # Multiplication: 30
print(a / b)  # Division: 3.333...
print(a // b) # Floor Division: 3
print(a % b)  # Modulus: 1
print(a ** b) # Exponentiation: 1000
```

## Assignment Operators

Assign values to variables:

```python
x = 5      # Simple assignment
x += 3     # x = x + 3 → 8
x -= 2     # x = x - 2 → 6
x *= 4     # x = x * 4 → 24
x /= 2     # x = x / 2 → 12.0
x //= 3    # x = x // 3 → 4.0
x %= 2     # x = x % 2 → 0.0
x **= 3    # x = x ** 3 → 0.0
```

## Comparison Operators

Compare values and return boolean:

```python
a = 5
b = 10

print(a == b)  # Equal: False
print(a != b)  # Not equal: True
print(a > b)   # Greater than: False
print(a < b)   # Less than: True
print(a >= b)  # Greater or equal: False
print(a <= b)  # Less or equal: True
```

## Logical Operators

Combine conditional statements:

```python
x = True
y = False

print(x and y)  # Logical AND: False
print(x or y)   # Logical OR: True
print(not x)    # Logical NOT: False
```

## Bitwise Operators

Operate on binary representations:

```python
a = 5  # Binary: 101
b = 3  # Binary: 011

print(a & b)   # AND: 1 (001)
print(a | b)   # OR: 7 (111)
print(a ^ b)   # XOR: 6 (110)
print(~a)      # NOT: -6 (inverted bits)
print(a << 1)  # Left shift: 10 (1010)
print(a >> 1)  # Right shift: 2 (10)
```

## Identity Operators

Check if objects are the same (not just equal):

```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a is b)     # False (different objects)
print(a is c)     # True (same object)
print(a == b)     # True (equal values)
```

## Membership Operators

Check if value is in sequence:

```python
my_list = [1, 2, 3, 4, 5]
my_string = "hello"

print(3 in my_list)        # True
print(6 in my_list)        # False
print('h' in my_string)    # True
print('z' in my_string)    # False
print(3 not in my_list)    # False
```

## Operator Precedence

Order of operations (highest to lowest):

1. `()` Parentheses
2. `**` Exponentiation
3. `+x`, `-x`, `~x` Unary plus, minus, bitwise NOT
4. `*`, `/`, `//`, `%` Multiplication, division, floor division, modulus
5. `+`, `-` Addition, subtraction
6. `<<`, `>>` Bitwise shifts
7. `&` Bitwise AND
8. `^` Bitwise XOR
9. `|` Bitwise OR
10. `==`, `!=`, `>`, `<`, `>=`, `<=` Comparisons
11. `is`, `is not` Identity
12. `in`, `not in` Membership
13. `not` Logical NOT
14. `and` Logical AND
15. `or` Logical OR
16. `=`, `+=`, etc. Assignment

Use parentheses to control precedence:

```python
result = (2 + 3) * 4  # 20
result = 2 + 3 * 4    # 14
