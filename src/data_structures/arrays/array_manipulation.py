"""
Starting with a 1-indexed array of zeros and a list of operations, 
for each operation add a value to each of the array element between two given indices, inclusive. 
Once all operations have been performed, return the maximum value in your array.

For example, the length of your array of zeros n = 10. 
Your list of queries is as follows:

a b k
1 5 3
4 8 7
6 9 1

Add the values of 'k' between the indices 'a' and 'b' inclusive:

index->	 1 2 3  4  5 6 7 8 9 10
	    [0,0,0, 0, 0,0,0,0,0, 0]
	    [3,3,3, 3, 3,0,0,0,0, 0]
	    [3,3,3,10,10,7,7,7,0, 0]
	    [3,3,3,10,10,8,8,8,1, 0]

The largest value is 10 after all operations are performed.

Input Format
The first line contains two space-separated integers 'n' and 'm',
the size of the array and the number of operations.
Each of the next 'm' lines contains three space-separated integers 'a', 'b' and 'k', 
the left index, right index and summand.

Sample Input
5 3
1 2 100
2 5 100
3 4 100

Sample Output
200
"""

def array_manipulation(n, queries):
    """
    array_manipulation has the following parameters:
    n - the number of elements in your array
    queries - a two dimensional array of queries where
    each queries[i] contains three integers, a, b, and k.
    """
    arr = [0]*n
    for i in queries:
        """
        for j in range(i[0], i[1] + 1):
            arr[j - 1] += i[2]
    return max(arr)"""
        arr[i[0] - 1] += i[2]
        if i[1] != len(arr):
            arr[i[1]] -= i[2]
    
    # The insight here is that the sum only needs to be calculated for each step or fall 
    # in the array rather than every individual element. 
    # This is easier understand if you draw a picture, 
    # but ultimately it allows us to do a single loop for calculating 
    # the two steps in the array, and another for accounting for the maximum step height.
    # There still remains the edge-case where arr[i[1]] -= i[2] doesn’t work because 
    # if i[1] == len(arr), adding ‘fall’ to the ‘step’ is erroneous.
    # So simply add in a conditional before arr[i[1]] -= i[2] - line 54
    max_value = 0
    itk = 0
    print(arr)
    for q in arr:
        itk += q
        if itk > max_value:
            max_value = itk
    return max_value
    
n = 5
queries = [ [1, 2, 100],
            [2, 5, 100],     
            [3, 4, 100]]
print(array_manipulation(n,queries))