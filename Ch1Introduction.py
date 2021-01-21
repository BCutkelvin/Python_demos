#!/usr/bin/env python3
#   Bryan Cutkelvin
#   2020
#   "Data Structure and Algorithmic Thinking with Python book"
#     -this code is written in Python3 as excerpt of the text for educational
#      purposes

# CH1 - Asymptotic Analysis: determining running time of algorithms:

# Logarithmic complexity = O( log n)
print('\nLogarithms O( log n)')


def Logarithms(n4):
    i2 = 1
    while i2 <= n4:
        i2 = i2 * 2
        print(i2)


Logarithms(5)

# if-then-else statement = O(n)
print('\nIf-then-else statements O(n)')
n2 = 3
if n2 == 1:
    print('wrong value!')
    print(n2)
else:
    for i in range(0, n2):
        print('Current number:', i)

# Consecutive statements = O(n^2)
print('\nConsecutive statements O(n^2)')
n1 = 3
for i in range(0, n1):
    print('Current number:', i)
    for i1 in range(0, n1):
        for j1 in range(0, n1):
            print('i1 value %d and j1 value %d' % (i1, j1))

# Nested Loops = O(n^2)
print('\nNested Loops O(n^2)')
x = 2
y = 2
for i in range(0, x):
    for j in range(0, y):
        print('i value %d and j value %d' % (i, j))

# Loops = O(n)
print('\nLoops O(n):')
n = 5
for i in range(0, n):
    print("current number:", i)
