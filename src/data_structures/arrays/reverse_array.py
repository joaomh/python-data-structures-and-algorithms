"""
Given an array of 'A' of 'N' integers, print each element in reverse order 
as a single line of space-separated integers.

Example:
Input  = 1 4 3 2
Output = 2 3 4 1
"""

# Reverse the array

# Method 1
# For loop
def reverseArray_1(a):
    b = []
    for i in a:
        b.insert(0, i)
    return b

# Method 2
# Copies the list prior to reversing it
def reverseArray_2(a):
    return a[::-1]

# Method 3
# The fastest way to reverse a long list
def reverseArray_3(a):
    a = a.reverse()
    return a

a = [1, 4, 3, 2]
print (reverseArray_1(a))
print (reverseArray_2(a))

reverseArray_3(a)
print(a)