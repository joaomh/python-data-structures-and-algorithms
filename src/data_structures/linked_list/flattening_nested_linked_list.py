"""
Suppose you have a linked list where the value of 
each node is a sorted linked list (i.e., it is a _nested_ list). 
Your task is to _flatten_ this nested list—that is, to combine all
nested lists into a single (sorted) linked list.
"""
# Use this class as the nodes in your linked list
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self, head):
        self.head = head

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        node = self.head
        while node.next is not None:
            node = node.next
        node.next = Node(value)

    def flatten_deep(self):
        value_list = []
        node = self.head

        while node.next is not None:
            value_list.append(node.value)
            node = node.next
        value_list.append(node.value)
        return value_list

def merge(list1, list2):
    merged = LinkedList(None)
    if list1 is None:
        return list2
    if list2 is None:
        return list1
    list1_elt = list1.head
    list2_elt = list2.head
    while list1_elt is not None or list2_elt is not None:
        if list1_elt is None:
            merged.append(list2_elt)
            list2_elt = list2_elt.next
        elif list2_elt is None:
            merged.append(list1_elt)
            list1_elt = list1_elt.next
        elif list1_elt.value <= list2_elt.value:
            merged.append(list1_elt)
            list1_elt = list1_elt.next
        else:
            merged.append(list2_elt)
            list2_elt = list2_elt.next
    return merged
    

class NestedLinkedList(LinkedList):
    def flatten(self):
        values = []
        for element in self.flatten_deep():
            values.append(element.flatten_deep())
        values = [item for sublist in values for item in sublist]
        values.sort()
        return values

linked_list = LinkedList(Node(1))
linked_list.append(3)
linked_list.append(5)

second_linked_list = LinkedList(Node(2))
second_linked_list.append(4)

nested_linked_list = NestedLinkedList(Node(linked_list))
nested_linked_list.append(second_linked_list)

"""
 Structure 'nested_linked_list' should now have 2 nodes.  
 The head node is a linked list containing '1, 3, 5'.  
 The second node is a linked list containing '2, 4'.

Calling 'flatten' should return a linked list containing '1, 2, 3, 4, 5'.
"""
solution = nested_linked_list.flatten()
print(solution == [1,2,3,4,5])