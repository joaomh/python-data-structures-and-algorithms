"""
There is a collection of input strings and a collection of query strings. 
For each query string, determine how many times it occurs in the list of input strings.

Example given a input strings = ['ab', 'ab', 'abc'] and 
queries = ['ab',' abc', 'bc'] we find 2 instances of 'ab',
1 of 'abc' and 0 of 'bc'. For each query we add an element to our return array
results = [2, 1, 0]

Input Format

The first line contains and integer 'n', the size of strings.
Each of the next 'n' lines contains a string 'strings[i]'.
The next line contains 'q', the size of queries.
Each of the next 'q' lines contains a string 'q[i]'.
"""

def matching_strings(strings, queries):
    results = []
    for i in range(len(queries)):
        count = 0
        for j in range(len(strings)):
            if strings[j] == queries[i]:
               count += 1
        results.append(count)
    return results

strings = ['ab', 'ab', 'abc']
queries = ['ab','abc', 'bc']

print(matching_strings(strings, queries))