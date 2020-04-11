# # Big O Notation

# The goal of this lesson is to develop your ability to look at some code and indentify its time complexity, using Big O notation.

# Comparison computacional complexity
import matplotlib.pyplot as plt
from scipy.special import gamma
import math
import numpy as np
n = np.linspace(1,101,100)
O1 = gamma(n)
O2 = 2**n
O3 = n**2
O4 = n*np.log(n) / np.log(2)
O5 = n
O6 = np.sqrt(n)
O7 = np.log(n) / np.log(2)
plt.plot(n, O1, '--k', label='n!') 
plt.plot(n, O2, '--r', label='2^n')  
plt.plot(n, O3, '--g', label='n^2') 
plt.plot(n, O4, 'y', label='nlog(n)') 
plt.plot(n, O5, 'c', label='n') 
plt.plot(n, O6, '--m', label='sqrt(n)') 
plt.plot(n, O7, 'b', label='log(n)') 
axes = plt.gca()
axes.set(xlim=(0, 100), ylim=(0, 100))
leg = axes.legend()
plt.show()

# O(N!)
# This is the Heap's algorithm, which is used for generating all possible permutation of n objects
# Another example could be the Travelling Salesman Problem
def Permutation(data, n):
    if n == 1:
        print(data)
        return
    for i in range(n):
        Permutation(data, n - 1)
        if n % 2 == 0:
            data[i], data[n-1] = data[n-1], data[i]
        else:
            data[0], data[n-1] = data[n-1], data[0]
data = [1, 2]
Permutation(data,len(data))
get_ipython().run_line_magic('time', '')

# O(2^n)
# Recursive calculation of Fibonacci numbers
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(20))
get_ipython().run_line_magic('time', '')

# O(N^2)
# Print pair of numbers in the data

def Print_Pair(some_list):
    for i in some_list:
        for j in some_list:

            print("Items: {}, {}".format(i,j))
Print_Pair([1, 2, 3, 4])      
get_ipython().run_line_magic('time', '')

# O(nlog(n))
# Mergesort algorithm
def Merge_Sort(data):
    if len(data) <= 1:
        return
    
    mid = len(data) // 2
    left_data = data[:mid]
    right_data = data[mid:]
    
    Merge_Sort(left_data)
    Merge_Sort(right_data)
    
    left_index = 0
    right_index = 0
    data_index = 0
    
    while left_index < len(left_data) and right_index < len(right_data):
        if left_data[left_index] < right_data[right_index]:
            data[data_index] = left_data[left_index]
            left_index += 1
        else:
            data[data_index] = right_data[right_index]
            right_index += 1
        data_index += 1
    
    if left_index < len(left_data):
        del data[data_index:]
        data += left_data[left_index:]
    elif right_index < len(right_data):
        del data[data_index:]
        data += right_data[right_index:]
    
data = [9, 0, 8, 6, 2, 5, 7, 3, 4, 1]
Merge_Sort(data)
print(data)
get_ipython().run_line_magic('time', '')

# O(n)
# Just print some itens

def Print_Item(data):
    for i in data:
        print(i)

Print_Item([1, 2, 3, 4])
get_ipython().run_line_magic('time', '')

# Linear search
def Linear_Search(data, value):
    for index in range(len(data)):
        if value == data[index]:
            return index
    raise ValueError('Value not found in the list')
data = [1, 3, 7, 4, 5, 9, 0, 11]
print(Linear_Search(data,9))
get_ipython().run_line_magic('time', '')

# O(log(n))
# This algorithms with logarithmic time complexity are commonly found on binary trees
for idx in range(0, len(data), 3):
    print(data[idx])
get_ipython().run_line_magic('time', '')

# Binary search
def binary_search(data, value):
    n = len(data)
    left = 0
    right = n - 1
    while left <= right:
        middle = (left + right) // 2
        if value < data[middle]:
            right = middle - 1
        elif value > data[middle]:
            left = middle + 1
        else:
            return middle
    raise ValueError('Value is not in the list')

data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(binary_search(data, 8))

# O(0n + 1)

def First_Idx(data):
    return data[0]
    
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(First_Idx(data))
get_ipython().run_line_magic('time', '')

