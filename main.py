#Nodes implementation
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#Linked list implementation
class linkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None

    def get(self,index):
        try:
            node = self.head
            for i in range(index):
                node = node.next
            return node.data
        except AttributeError:
            print("GET ERROR: Index out of range")
    
    def pushback(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

    def pushfront(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def popback(self):
        if self.tail is None:
            print("ERROR: Empty list")
        else:
            current_node = self.head
            while current_node.next.next:
                current_node = current_node.next
            temp = current_node.data
            current_node.next = None
            self.tail = current_node
            return temp

    def print(self):
        if self.head is None:
            print("ERROR: Empty list")
        else:
            current_node = self.head
            while current_node is not None:
                if current_node.next is None:
                    print(current_node.data, end="")
                else:
                    print(current_node.data, end=" ")
                current_node = current_node.next

list1 = input().split()
list2 = input().split()
linked1 = linkedList()
linked2 = linkedList()
length = len(list1)
listResult1 = linkedList()
listResult2 = linkedList()

for i in range(length):
    linked1.pushback(list1[i])
    linked2.pushback(list2[length - i - 1])

for i in range(length):
    if linked1.head.data !=  linked2.head.data:
        listResult1.pushback(linked1.head.data)
        listResult2.pushfront(linked2.head.data)
    linked1.head = linked1.head.next
    linked2.head = linked2.head.next

listResult1.print()
print()
listResult2.print()
