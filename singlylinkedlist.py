class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.temp = None

    def create(self):
        size = int(input("Enter the size of the list: "))
        for i in range(size):
            value = int(input("Enter a value: "))
            newnode = Node(value)
            if self.head is None:
                self.head = newnode
                self.temp = newnode
            else:
                self.temp.next = newnode
                self.temp = newnode

    def display(self):
        self.temp = self.head
        while self.temp is not None:
            print(self.temp.data)
            self.temp = self.temp.next

    def insertfront(self):
        data = int(input("Enter the front value: "))
        newnode = Node(data)
        newnode.next = self.head
        self.head = newnode

    def insertend(self):
        data = int(input("Enter the back value: "))
        newnode = Node(data)
        self.temp = self.head
        while self.temp.next is not None:
            self.temp = self.temp.next
        self.temp.next = newnode

    def insertmid(self):
        position = int(input("Enter the position: "))
        data = int(input("Enter the mid value: "))
        newnode = Node(data)
        self.temp = self.head
        i = 1
        while i < position:
            self.temp = self.temp.next
            i += 1
        newnode.next = self.temp.next
    def deletefront(self):
        self.temp = self.head
        self.head = self.head.next
        del self.temp

    def deleteend(self):
        self.temp = self.head
        previous = None
        while self.temp.next is not None:
            previous = self.temp
            self.temp = self.temp.next
        previous.next = None
        del self.temp
    def deletemid(self):
        position = int(input("Enter the position to delete: "))
        self.temp = self.head
        prev = self.head
        i = 1
        while i < position:
            prev = self.temp
            self.temp = self.temp.next
            i += 1
        prev.next = self.temp.next
        self.temp=None
        del self.temp

    def count(self):
        self.temp = self.head
        count = 1
        while self.temp.next is not self.head:
            count += 1
            self.temp = self.temp.next
        print(count)

    def search(self):
        item = int(input("Enter an element to search: "))
        self.temp = self.head
        while self.temp:
            if self.temp.data == item:
                print(f"{item} is there")
                return
            self.temp = self.temp.next
        print(f"{item} is not there")


obj = LinkedList()
obj.create()
obj.insertfront()
obj.insertend()
obj.insertmid()
obj.deletefront()
obj.deleteend()
obj.deletemid()
obj.display()
