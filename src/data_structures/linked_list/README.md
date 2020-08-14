# Linked List

In computer science, a **linked list** is a linear collection 
of data elements, in which linear order is not given by 
their physical placement in memory. Instead, each 
element points to the next. It is a data structure 
consisting of a group of nodes which together represent 
a sequence. Under the simplest form, each node is 
composed of data and a reference (in other words, 
a link) to the next node in the sequence. This structure
allows for efficient insertion or removal of elements 
from any position in the sequence during iteration. 
More complex variants add additional links, allowing 
efficient insertion or removal from arbitrary element 
references. A drawback of linked lists is that access 
time is linear (and difficult to pipeline). Faster 
access, such as random access, is not feasible. Arrays 
have better cache locality as compared to linked lists.

![Linked List](https://upload.wikimedia.org/wikipedia/commons/6/6d/Singly-linked-list.svg)

## Pseudocode for Basic Operations

### Insert

```text
Add(value)
  Pre: value is the value to add to the list
  Post: value has been placed at the tail of the list
  n ← node(value)
  if head = ø
    head ← n
    tail ← n
  else
    tail.next ← n
    tail ← n
  end if
end Add
```

```text
Prepend(value)
 Pre: value is the value to add to the list
 Post: value has been placed at the head of the list
 n ← node(value)
 n.next ← head
 head ← n
 if tail = ø
   tail ← n
 end
end Prepend
```

### Search

```text
Contains(head, value)
  Pre: head is the head node in the list
       value is the value to search for
  Post: the item is either in the linked list, true; otherwise false
  n ← head
  while n != ø and n.value != value
    n ← n.next
  end while
  if n = ø
    return false
  end if
  return true
end Contains
```
    
### Delete

```text
Remove(head, value)
  Pre: head is the head node in the list
       value is the value to remove from the list
  Post: value is removed from the list, true, otherwise false
  if head = ø
    return false
  end if
  n ← head
  if n.value = value
    if head = tail
      head ← ø
      tail ← ø
    else
      head ← head.next
    end if
    return true
  end if
  while n.next != ø and n.next.value != value
    n ← n.next
  end while
  if n.next != ø
    if n.next = tail
      tail ← n
    end if
    n.next ← n.next.next
    return true
  end if
  return false
end Remove
```

### Traverse

```text
Traverse(head)
  Pre: head is the head node in the list
  Post: the items in the list have been traversed
  n ← head
  while n != ø
    yield n.value
    n ← n.next
  end while
end Traverse
```

### Traverse in Reverse

```text
ReverseTraversal(head, tail)
  Pre: head and tail belong to the same list
  Post: the items in the list have been traversed in reverse order
  if tail != ø
    curr ← tail
    while curr != head
      prev ← head
      while prev.next != curr
        prev ← prev.next
      end while
      yield curr.value
      curr ← prev
    end while
   yield curr.value
  end if
end ReverseTraversal
```

## Complexities

### Time Complexity

| Access    | Search    | Insertion | Deletion  |
| :-------: | :-------: | :-------: | :-------: |
| O(n)      | O(n)      | O(1)      | O(n)      |

### Space Complexity

O(n)

# Doubly Linked List
In computer science, a **doubly linked list** is a linked data structure that 
consists of a set of sequentially linked records called nodes. Each node contains 
two fields, called links, that are references to the previous and to the next 
node in the sequence of nodes. The beginning and ending nodes' previous and next 
links, respectively, point to some kind of terminator, typically a sentinel 
node or null, to facilitate traversal of the list. If there is only one 
sentinel node, then the list is circularly linked via the sentinel node. It can 
be conceptualized as two singly linked lists formed from the same data items, 
but in opposite sequential orders.

![Doubly Linked List](https://upload.wikimedia.org/wikipedia/commons/5/5e/Doubly-linked-list.svg)

The two node links allow traversal of the list in either direction. While adding 
or removing a node in a doubly linked list requires changing more links than the 
same operations on a singly linked list, the operations are simpler and 
potentially more efficient (for nodes other than first nodes) because there 
is no need to keep track of the previous node during traversal or no need 
to traverse the list to find the previous node, so that its link can be modified.

## Pseudocode for Basic Operations

### Insert

```text
Add(value)
  Pre: value is the value to add to the list
  Post: value has been placed at the tail of the list
  n ← node(value)
  if head = ø
    head ← n
    tail ← n
  else
    n.previous ← tail
    tail.next ← n
    tail ← n
  end if
end Add
```
    
### Delete

```text
Remove(head, value)
  Pre: head is the head node in the list
       value is the value to remove from the list
  Post: value is removed from the list, true; otherwise false
  if head = ø
    return false
  end if
  if value = head.value
    if head = tail
      head ← ø
      tail ← ø
    else
      head ← head.next
      head.previous ← ø
    end if
    return true
  end if
  n ← head.next
  while n = ø and value !== n.value
    n ← n.next
  end while
  if n = tail
    tail ← tail.previous
    tail.next ← ø
    return true
  else if n = ø
    n.previous.next ← n.next
    n.next.previous ← n.previous
    return true
  end if
  return false
end Remove
```
    
### Reverse Traversal

```text
ReverseTraversal(tail)
  Pre: tail is the node of the list to traverse
  Post: the list has been traversed in reverse order
  n ← tail
  while n = ø
    yield n.value
    n ← n.previous
  end while
end Reverse Traversal
```
    
## Complexities

## Time Complexity

| Access    | Search    | Insertion | Deletion  |
| :-------: | :-------: | :-------: | :-------: |
| O(n)      | O(n)      | O(1)      | O(n)      |

### Space Complexity

O(n)

## References

- [GeeksforGeeks](https://www.geeksforgeeks.org/data-structures/linked-list/)
- [Wikipedia Linked List](https://en.wikipedia.org/wiki/Linked_list)
- [Wikipedia Doubly Linked List](https://en.wikipedia.org/wiki/Doubly_linked_list)

