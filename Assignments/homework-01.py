"""
Name: Mikhail Salter
Email: salter.mikhail@gmail.com
Assignment: Homework 1 - List and Dictionaries
Due: 19 Sep @ 1:00 p.m.
"""
A:What would Python print?
a = [1, 5, 4, 2, 3] 
print(a[0], a[-1])
# Prints: 1 3

a[4] = a[2] + a[-2]
Print(a)
# Prints: [1, 5, 4, 2, 6]

print(len(a))
# Prints: 5

print(4 in a)
# Prints: True

a[1] = [a[1], a[0]]
print(a)
# Prints: [1, [5, 1], 4, 2, 6]

B: Write a function that removes all instances of an element from a list.

def remove_all(el, lst):
"""Removes all instances of el from lst. 
Given: x = [3, 1, 2, 1, 5, 1, 1, 7]
Usage: remove_all(1, x)
Would result in: [3, 2, 5, 7]
"""
   pass
x = [3, 1, 2, 1, 5, 1, 1, 7]
def remove_all():
  
  while 1 in x:
   x.remove(1)

remove_all()
print(x)

C: Write a function that takes in two values, x and y, and a list, and adds as many y's to the end of the list as there are x's. Do not use the built-in function count.
def add_this_many(x, y, lst):
""" Adds y to the end of lst the number of times x occurs in lst. 
Given: lst = [1, 2, 4, 2, 1]
Usage: add_this_many(1, 5, lst)
Results in: [1, 2, 4, 2, 1, 5, 5]
"""
    pass

D: What would Python print?
a = [3, 1, 4, 2, 5, 3]
print(a[:4])
# [3, 1, 4, 2]

print(a)
# [3, 1, 4, 2, 5, 3]

print(a[1::2])
# Prints:[1, 2, 3]

print(a[:])
# [3, 1, 4, 2, 5, 3]

print(a[4:2])
# Prints: []

print(a[1:-2])
# Prints: [1, 4, 2]

print(a[::-1])
# Prints: [3, 5, 2, 4, 1, 3]
