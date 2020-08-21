print(dir(int), end='')
print(dir(float), end='')
a = 5
b = 2.5
print(a / b)
print(a + b)
print(a * b)

print(type(a))
print(type(b))
print(type(a - b))

print(b.is_integer())
print(5.5.is_integer())

# DECIMAL
from decimal import Decimal, getcontext
getcontext().prec = 4
print(Decimal(1.1) + Decimal(2.2))

import decimal
print(dir(decimal))
