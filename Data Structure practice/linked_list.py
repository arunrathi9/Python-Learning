class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        newNode = Node(data)
        if(self.head):
            current = self.head
            while(current.next):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode

    def print_(self):
        current = self.head
        while(current):
            print(current.data)
            current = current.next

single_linked_list = LinkedList()
for node in [1,2,3,4,5]:
    single_linked_list.insert(node)

single_linked_list.print_()