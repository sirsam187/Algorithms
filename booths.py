#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def booth_multiplication(multiplicand, multiplier):
    multiplicand = bin(multiplicand)[2:]
    multiplier = bin(multiplier)[2:]

    bit_length = max(len(multiplicand), len(multiplier))
    A = "0" * bit_length
    Q = multiplier.zfill(bit_length)
    Q_1 = '0'

    for _ in range(bit_length):
        if Q[-2:] == '01':
            A = bin(int(A, 2) + int(multiplicand, 2))[2:].zfill(bit_length)
        elif Q[-2:] == '10':
            A = bin(int(A, 2) - int(multiplicand, 2))[2:].zfill(bit_length)

        A = A[:-1]
        Q = Q[:-1]

        Q_1 = Q[-1]

        A = Q_1 + A
        Q = Q_1 + Q

    result = int(A + Q, 2)
    return result

multiplicand = 6
multiplier = 5
result = booth_multiplication(multiplicand, multiplier)
print(f"The result of {multiplicand} * {multiplier} is: {result}")

