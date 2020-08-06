"""
Given a linked list, swap the two nodes present at position 'i' and 'j'. 
The positions are based on 0-based indexing.
Note: You have to swap the nodes and not just the values. 

Example:
linked_list = 3 4 5 2 6 1 9
positions = 3 4
output = 3 4 5 6 2 1 9

Explanation: 
The node at position 3 has the value '2'
The node at position 4 has the value '6'
Swapping these nodes will result in a final order of nodes of '3 4 5 6 2 1 9'
"""

class Node:
    """LinkedListNode class to be used for this problem"""
    def __init__(self, data):
        self.data = data
        self.next = None

def swap_nodes(head, left_index, right_index):

    # if both the indices are same
    if left_index == right_index:
        return head
    
    
    left_previous = None
    left_current = None

    right_previous = None
    right_current = None

    count = 0
    temp = head
    new_head = None

    # find out previous and current node at both the indices
    while temp is not None:
        if count == left_index:
            left_current = temp
        elif count == right_index:
            right_current = temp
            break

        if left_current is None:
            left_previous = temp
        right_previous = temp
        temp = temp.next
        count += 1

    right_previous.next = left_current
    temp = left_current.next
    left_current.next = right_current.next

    # if both the indices are next to each other
    if left_index != right_index:
        right_current.next = temp

    # if the node at first index is head of the original linked list
    if left_previous is None:
        new_head = right_current
    else:
        left_previous.next = right_current
        new_head = head

    return new_head

def test_function(test_case):
    head = test_case[0]
    left_index = test_case[1]
    right_index = test_case[2]
    
    left_node = None
    right_node = None
    
    temp = head
    index = 0
    try:
        while temp is not None:
            if index == left_index:
                left_node = temp
            if index == right_index:
                right_node = temp
                break
            index += 1
            temp = temp.next

        updated_head = swap_nodes(head, left_index, right_index)

        temp = updated_head
        index = 0
        pass_status = [False, False]

        while temp is not None:
            if index == left_index:
                pass_status[0] = temp is right_node
            if index == right_index:
                pass_status[1] = temp is left_node

            index += 1
            temp = temp.next

        if pass_status[0] and pass_status[1]:
            print("Pass")
        else:
            print("Fail")
        return updated_head
    except Exception as e:
        print("Fail")

def create_linked_list(arr):
    if len(arr)==0:
        return None
    head = Node(arr[0])
    tail = head
    for data in arr[1:]:
        tail.next = Node(data)
        tail = tail.next
    return head

def print_linked_list(head):
    while head:
        print(head.data, end=" ")
        head = head.next
    print()

arr = [3, 4, 5, 2, 6, 1, 9]
head = create_linked_list(arr)
left_index = 3
right_index = 4

test_case = [head, left_index, right_index]
updated_head = test_function(test_case)