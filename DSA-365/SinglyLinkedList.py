"""Singly Linked List in Python"""

# Prerequistes: object oriented programming

# 1.What are linked list?
# 2.What are the disadvantages of arrays that linked list try to overcome?
# 3.why we need linked list? what are the advantages?
# 4.what are the different operation of linked list?
# 5.how to master writing code for these operations?
# 6.Hands on workshop for writing code for the operation?

#Class  which represent the node in a singly linked list
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

# Class implements all the operation for singly linked list
class SinglyLinkedList:
    def __init__(self):
        self.head = None 
          
     
    #This function add the node at the beginning
    # This needs to handle two scenarios/cases
    # 1) When list is empty
    # 2) List has some elements
    def insert_at_beginning(self,data):
        # create anew node 
        new_node = Node(data)
        
        # case 1: If the list is empty, make the new node as head
        if (self.head == None):
            self.head = new_node
            return
        
        
        #driver code to test the above class
if __name__ == "__main__":
    #create a new singly linked list
    list = SinglyLinkedList()
            
    list.insert_at_beginning(10)
    list.insert_at_beginning(20)
    list.insert_at_beginning(30)
            
    print("List is created sucessfuly.")
    print("Head node data is:", list.head.data)
    print("Next node data is:", list.head.next.data)
    print("Next node data is:", list.head.next.next.data)