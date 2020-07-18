# Singly LinkedList
''' 
         head        second              third 
         |                |                  | 
         |                |                  | 
    +----+------+     +----+------+     +----+------+ 
    | 1  |  o-------->| 2  |  o-------->|  3 | null | 
    +----+------+     +----+------+     +----+------+  
'''
# Node class of a linked list
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
    
    # Returns the length of the linked list.
    def length(self):
        if self.head == None:
            return 0
        current_node = self.head
        total = 0 # Init count
        # Loop while end of linked list is not reached 
        while current_node:
            total += 1
            current_node = current_node.next
        return total

    # Converts a linked list back into a Python list
    def to_list(self):

        # Init as null
        node_data = []
        current_node = self.head

        while current_node:
            node_data.append(current_node.data)
            current_node = current_node.next
        return node_data
    # Returns the value of the node at 'index'.  
    def get(self, index):
        if index >= self.length() or index < 0:
            print("ERROR: 'Get' Index out of range!")
            return None
        current_idx  = 0
        current_node = self.head
        while current_node != None:
            if current_idx == index: 
                return current_node.data
            current_node  = current_node.next
            current_idx += 1
    # reverse a linked list
    def reverse_linkedlist(self):
        previous_node = None
        current_node = self.head
        while current_node != None:
            next = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next
        self.head = previous_node
    
    # Searching for an element is quite similar to counting or traversing a linked list
    def search_item(self, value):
        if self.head == None:
            print("List has no elements")
            return
        current_node = self.head
        while current_node != None:
            if current_node.data == value:
                print("Item found")
                return True
            current_node = current_node.next
        print("Item not found")
        return False


    # This function prints contents of linked list
    # starting from the head of the linked list
    # traverse function is as follows
    def display(self): 
        contents = self.head 
        # If the list is null
        if contents is None:
            print("List has no element")
        while contents: 
            print(contents.data)
            contents = contents.next
        print("----------") # to see better the lists

    # Deleting an element or item from the start
    def remove_at_start(self):
        if self.head == None:
            print("The list has no element to delete")
            return 
        self.head = self.head.next
    
    # Deleting an element or item at the end
    def remove_at_end(self):
        if self.head is None:
            print("The list has no element to delete")
            return
        current_node = self.head
        while current_node.next.next != None:
            current_node = current_node.next
        current_node.next = None

    # This remove a node with the specified value
    def remove_element_by_value(self, value):
        # Store head node  
        current_node = self.head  
  
        # If head node itself holds the value to be deleted  
        if current_node != None:  
            if current_node.data == value:  
                self.head = current_node.next
                current_node = None
                return
  
        # Search for the value to be deleted, keep track of the  
        # previous node as we need to change 'prev.next'  
        while current_node != None:  
            if current_node.data == value:  
                break
            prev = current_node  
            current_node = current_node.next
  
        # if value was not present in linked list  
        if current_node == None:  
            return
  
        # Unlink the node from linked list  
        prev.next = current_node.next
        current_node = None
    
    # Insert an item in a single linked list 
    # add an item at the start of the list
    def insert_at_start(self, data):
        new_node        = Node(data)
        new_node.next   = self.head
        self.head = new_node

    # Insert an item in a single linked list 
    # add an item at the end of the list   
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = new_node

    # Insert an item in a single linked list 
    # add an item at any index of the list
    def insert_at_index (self, index, data):
        if index == 1:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
        i = 1
        current_node = self.head
        while i < index-1 and current_node is not None:
            current_node = current_node.next
            i = i + 1
        if current_node is None:
            print("ERROR: Index out of range!")
        else: 
            new_node = Node(data)
            new_node.next = current_node.next 
            current_node.next  = new_node
	
# Test   
my_list = LinkedList()
my_list.display()
# Add the elements
my_list.append(3)
my_list.append(2)
my_list.append(7)
my_list.append(1)

my_list.display()

print("The total number of elements are: " + str(my_list.length()))
print(my_list.to_list()) # Python list
print("---------")
my_list.reverse_linkedlist() # Reverse linked list
my_list.display()

my_list.search_item(7)
my_list.search_item(77)

my_list.remove_at_start()
my_list.display()

my_list.remove_at_end()
my_list.display()

my_list.insert_at_start(1)
my_list.display()

my_list.insert_at_end(3)
my_list.display()

my_list.remove_element_by_value(3)
my_list.display()

my_list.insert_at_index(2, 88)
my_list.display()