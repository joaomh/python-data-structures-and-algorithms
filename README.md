# Python Data Structures and Algorithms
This repository contains Python based examples of many 
data structures and algorithms.

This is the main reference for my YouTube Channel, 2001 Engenharia in PT-BR

[▶ Estrutura de Dados e Algoritmos em Python](https://www.youtube.com/playlist?list=PLE1UtdMhwaEonmSRDkSzpFV5m5zKiqM94)

Each algorithm and data structure has its own separate README
with related explanations and links for further reading.

## Data Structures
In computer science, a data structure is a data organization, management, and storage format that enables efficient access and modification. More precisely, a data structure is a collection of data values, the relationships among them, and the functions or operations that can be applied to the data.

Data structures are the building block for Computer Science and Software Engineering.

`B` - Beginner, `A` - Advanced

* `B` [Linked List](src/data_structures/linked_list)
* `B` [Doubly Linked List](src/data_structures/linked_list)
* `B` [Array](src/data_structures/arrays)
* `B` [Queue](src/data_structures/queue)
* `B` [Stack](src/data_structures/stack)
* `B` [Hash Table](src/data_structures/hash-table)
* `B` [Priority Queue](src/data_structures/priority-queue)
* `B` [Dictionaries](src/data_structures/dictionaries)
* `A` [Trie](src/data_structures/trie)
* `A` [Tree](src/data_structures/tree)
  * `A` [Binary Search Tree](src/data_structures/tree/binary-search-tree)
  * `A` [AVL Tree](src/data_structures/tree/avl-tree)
  * `A` [Red-Black Tree](src/data_structures/tree/red-black-tree)
  * `A` [Segment Tree](src/data_structures/tree/segment-tree)
  * `A` [Fenwick Tree](src/data_structures/tree/fenwick-tree)
* `A` [Graph](src/data_structures/graph) 
* `A` [Disjoint Set](src/data_structures/disjoint-set)
* `A` [Bloom Filter](src/data_structures/bloom-filter)

## Recursion 
In computer science Recursion is a technique for solving problems where the solution to a particular problem depends on the solution to a smaller instance of the same problem.

`B` - Beginner, `A` - Advanced

* `B` [Introduction to Recursion](src/recursion/intro_recursion.ipynb)
* `B` [Factorial Using Recursion](src/recursion/factorial_using_recursion.ipynb)
* `B` [Fibonacci Using Recursion](src/recursion/fibonacci_using_recursion.ipynb)

## Algorithm
In mathematics and computer science, an algorithm  is a finite sequence of well-defined, computer-implementable instructions, typically to solve a class of problems or to perform a computation. Algorithms are always unambiguous and are used as specifications for performing calculations, data processing, automated reasoning, and other tasks.


### Big O Notation

*Big O notation* is used to classify algorithms according to how their running time or space requirements grow as the input size grows.
On the chart below you may find most common orders of growth of algorithms specified in Big O notation.

![Big O graphs](./assets/big-o-graph.png)

Source: [Big O Cheat Sheet](http://bigocheatsheet.com/).

Below is the list of some of the most used Big O notations and their performance comparisons against different sizes of the input data.

| Big O Notation | Computations for 10 elements | Computations for 100 elements | Computations for 1000 elements  |
| -------------- | ---------------------------- | ----------------------------- | ------------------------------- |
| **O(1)**       | 1                            | 1                             | 1                               |
| **O(log n)**   | 3                            | 6                             | 9                               |
| **O(n)**       | 10                           | 100                           | 1000                            |
| **O(n log n)** | 30                           | 600                           | 9000                            |
| **O(n<sup>2</sup> )**     | 100                          | 10000                         | 1000000                         |
| **O(2<sup>n</sup> )**     | 1024                         | 1.26e+29                      | 1.07e+301                       |
| **O(n!)**      | 3628800                      | 9.3e+157                      | 4.02e+2567                      |

### Data Structure Operations Complexity

| Data Structure          | Access    | Search    | Insertion | Deletion  | Comments  |
| ----------------------- | :-------: | :-------: | :-------: | :-------: | :-------- |
| **Array**               | 1         | n         | n         | n         |           |
| **Stack**               | n         | n         | 1         | 1         |           |
| **Queue**               | n         | n         | 1         | 1         |           |
| **Linked List**         | n         | n         | 1         | n         |           |
| **Hash Table**          | -         | n         | n         | n         | In case of perfect hash function costs would be O(1) |
| **Binary Search Tree**  | n         | n         | n         | n         | In case of balanced tree costs would be O(log(n)) |
| **B-Tree**              | log(n)    | log(n)    | log(n)    | log(n)    |           |
| **Red-Black Tree**      | log(n)    | log(n)    | log(n)    | log(n)    |           |
| **AVL Tree**            | log(n)    | log(n)    | log(n)    | log(n)    |           |
| **Bloom Filter**        | -         | 1         | 1         | -         | False positives are possible while searching |

### Array Sorting Algorithms Complexity

| Name                  | Best            | Average             | Worst               | Memory    | Stable    | Comments  |
| --------------------- | :-------------: | :-----------------: | :-----------------: | :-------: | :-------: | :-------- |
| **Bubble sort**       | n               | n<sup>2</sup>       | n<sup>2</sup>       | 1         | Yes       |           |
| **Insertion sort**    | n               | n<sup>2</sup>       | n<sup>2</sup>       | 1         | Yes       |           |
| **Selection sort**    | n<sup>2</sup>   | n<sup>2</sup>       | n<sup>2</sup>       | 1         | No        |           |
| **Heap sort**         | n&nbsp;log(n)   | n&nbsp;log(n)       | n&nbsp;log(n)       | 1         | No        |           |
| **Merge sort**        | n&nbsp;log(n)   | n&nbsp;log(n)       | n&nbsp;log(n)       | n         | Yes       |           |
| **Quick sort**        | n&nbsp;log(n)   | n&nbsp;log(n)       | n<sup>2</sup>       | log(n)    | No        | Quicksort is usually done in-place with O(log(n)) stack space |
| **Shell sort**        | n&nbsp;log(n)   | depends on gap sequence   | n&nbsp;(log(n))<sup>2</sup>  | 1         | No         |           |
| **Counting sort**     | n + r           | n + r               | n + r               | n + r     | Yes       | r - biggest number in array |
| **Radix sort**        | n * k           | n * k               | n * k               | n + k     | Yes       | k - length of longest key |

## References

This project was based on 

- [JavaScript Algorithms and Data Structures](https://github.com/trekhleb/javascript-algorithms)

## Supporting the project

You may support this project via <3

- [Patreon](patreon.com/2001engenharia).          
