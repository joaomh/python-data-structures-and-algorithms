"""
Problem Statement
Implement a function that detects if a loop exists in a linked list.
The way we'll do this is by having two pointers, called "runners", 
moving through the list at different rates. Typically we have a "slow" runner 
which moves at one node per step and a "fast" runner that moves at two nodes per step.

If a loop exists in the list, 
the fast runner will eventually move behind the slow runner
as it moves to the beginning of the loop. 
Eventually it will catch up to the slow runner and both runners
will be pointing to the same node at the same time. 
If this happens then you know there is a loop in the linked list. 

"""
class Node:

    # Constructor to create a new node 
    def __init__(self, data):
        self.data = data # Pointer to data
        self.next = None # Initialize next as null

# Linked List class contains a Node 
class LinkedList:

    # Constructor for empty linked list
    def __init__(self):
        self.head = None

    # Given a reference to the head,
    # appends a new node 
    def append(self, data):

        # Put the new node in the data
        new_node = Node(data)

        # If the Linked List is empty,
        # make the new node as head 
        if self.head == None:
            self.head = new_node
            return
        
        current_node = self.head

        # Now traverse till the new node
        while current_node.next:
            current_node = current_node.next

        # Change the next of the current node    
        current_node.next = new_node
        return


list_with_loop = LinkedList()
list_with_loop.append(2)
list_with_loop.append(-1)
list_with_loop.append(7)
list_with_loop.append(0)
list_with_loop.append(3)

# Creating a loop where the last node points back to the second node
loop_start = list_with_loop.head.next

node = list_with_loop.head
while node.next: 
    node = node.next   
node.next = loop_start

def is_circular(linked_list):
    """
    Determine wether the Linked List is circular or not

    Args:
       linked_list(obj): Linked List to be checked
    Returns:
       bool: Return True if the linked list is circular, return False otherwise
    """

    if linked_list.head is None:
        return False
    
    slow = linked_list.head
    fast = linked_list.head
    
    while fast and fast.next:
        # slow pointer moves one node
        slow = slow.next
        # fast pointer moves two nodes
        fast = fast.next.next
        
        if slow == fast:
            return True
    
    # If we get to a node where fast doesn't have a next node or doesn't exist itself, 
    # the list has an end and isn't circular
    return False
# Test Cases

# Creating a small loop
small_loop = LinkedList()
small_loop.append(1)
small_loop.head.next = small_loop.head

# Linked list without loop
test_loop = LinkedList()
test_loop.append(2)
test_loop.append(-1)
test_loop.append(7)
test_loop.append(0)
test_loop.append(3)

print ("Pass" if is_circular(list_with_loop) else "Fail")
print ("Pass" if not is_circular(test_loop) else "Fail")
print ("Pass" if is_circular(small_loop) else "Fail")
print ("Pass" if not is_circular(LinkedList()) else "Fail")
