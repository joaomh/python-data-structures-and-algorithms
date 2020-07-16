# Doubly LinkedList
''' 
         head        second              third 
         |                |                  | 
         |                |                  | 
    +----+------+     +----+------+     +----+------+ 
    | 1  |  o-------->| 2  |  o-------->|  3 | null | 
    |    |  o<--------|    |  o<--------|    |      |
    +----+------+     +----+------+     +----+------+  
'''
# Node class of a linked list
class DoubleNode:
    # Constructor to create a new node 
    def __init__(self, data):
        self.data     = data 
        self.next     = None # Reference to next node
        self.previous = None # Reference to the previous node
    
class DoublyLinkedList:
    # Constructor for empty linked list
    def __init__(self):
        self.head = None
        self.tail = None
    
    # Given a reference to the head 
    # appends a new node at the end 
    def append(self, data):
        # Allocates node and put in the data
        new_node = DoubleNode(data) 

        # This new node is going to be the last node
        new_node.next = None

        # If the Linked List is empty,
        # make the new node as head 
        if self.head == None:
            new_node.previous = None
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        
        last_node.next = new_node

        new_node.previous = last_node
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

    def reverse_linked_list(self):
        if self.head is None:
            print("The list has no element to reverse")
            return 0
        # The next reference of the start node 
        # should be set none because the first node will
        # become the last node in the reversed list.
        # The previous reference of the last node should be set to None 
        # since the last node will become the previous node
        # The next references of the nodes (except the first and last node) in the original list 
        # Should be swapped with the previous references.
        current_node = self.head
        new_node = current_node.next
        current_node.next = None
        current_node.previous = new_node 
        while new_node  != None:
            new_node .previous = new_node .next
            new_node .next = current_node
            current_node = new_node 
            new_node  = new_node .previous
        self.head = current_node

    def display(self): 
        contents = self.head 
        # If the list is null
        if contents is None:
          print("List has no element")
        while contents: 
            print(contents.data)
            contents = contents.next
        print("----------") # to see better the lists

    # This insert a node at the start
    def insert_at_start(self, data):
        if self.head == None:
            new_node = DoubleNode(data)
            self.head = new_node
            print("Node inserted")
            return
        new_node = DoubleNode(data)
        new_node.next = self.head
        self.head.previous = new_node
        self.head = new_node

    # This insert a node at the end
    def insert_at_end(self, data):
        if self.head == None:
            new_node = DoubleNode(data)
            self.head = new_node
            return
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
        new_node = DoubleNode(data)
        current_node.next = new_node
        new_node.previous = current_node
    
    # Deleting Elements from the Start
    def remove_at_start(self):
        if self.head == None:
            print("The list has no element to delete")
            return 
        if self.head.next == None:
            self.head = None
            return
        self.head = self.head.next
        self.start_prev = None

    # Deleting Elements from the end
    def remove_at_end(self):
        if self.head == None:
            print("The list has no element to delete")
            return 
        if self.head.next == None:
            self.head = None
            return
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
        current_node.previous.next = None
    
    # This remove a node with the specified value
    def remove_element_by_value(self, value):
        if self.head == None:
            print("The list has no element to delete")
            return 
        if self.head.next == None:
            if self.head.item == value:
                self.head = None
            else:
                print("Item not found")
            return 

        if self.head.data == value:
            self.head = self.head.next
            self.head.previous = None
            return

        current_node = self.head
        while current_node.next != None:
            if current_node.data == value:
                break
            current_node = current_node.next
        if current_node.next != None:
            current_node.previous.next = current_node.next
            current_node.next.previous = current_node.previous
        else:
            if current_node.data == value:
                current_node.previous.next = None
            else:
                print("Element not found")


# Test   
my_list = DoublyLinkedList()
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
my_list.reverse_linked_list() # Reverse linked list
my_list.display()

my_list.remove_at_start()
my_list.display()

my_list.remove_at_end()
my_list.display()

my_list.insert_at_start(1)
my_list.display()

my_list.insert_at_end(3)
my_list.display()

my_list.remove_element_by_value(7)
my_list.display()
