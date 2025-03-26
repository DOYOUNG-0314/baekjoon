class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node

    def delete(self, data):
        cur = self.head
        if cur and cur.data == data:
            self.head = cur.next
            return
        prev = None
        while cur and cur.data != data:
            prev = cur
            cur = cur.next
        if cur:
            prev.next = cur.next

    def print_all(self):
        cur = self.head
        while cur:
            print(cur.data, end=" → ")
            cur = cur.next
        print("None")
