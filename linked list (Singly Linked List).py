linked list (Singly Linked List).py

class Node:
    def __init__(self, data):
        self.data = data  # stores the value
        self.next = None  # points to the next node (initially None)

class LinkedList:
    def __init__(self):
        self.head = None  # initializes the list as empty
    
    def append(self, data):
        new_node = Node(data)  # create a new node with given data
        if not self.head:  # if the list is empty, make the new node the head
            self.head = new_node
        else:
            current = self.head
            while current.next:  # find the last node
                current = current.next
            current.next = new_node  # make the last node point to the new node
    
    def display(self):
        current = self.head
        while current:  # traverse through the list
            print(current.data, end=" -> ")  # print the data
            current = current.next
        print("None")  # indicate the end of the list

# Example usage
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.display()  # Output: 10 -> 20 -> 30 -> None
