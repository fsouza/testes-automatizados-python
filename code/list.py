class Node(object):

    def __init__(self, content, next=None):
        self.content = content
        self.next = next

class List(object):
    size = 0
    head = None
    tail = None

    def append(self, item):
        if self.size == 0:
            self.head = self.tail = Node(item)
        else:
            old_tail = self.tail
            self.tail = Node(item)
            old_tail.next = self.tail
        self.size += 1

    def insert(self, item):
        if self.size == 0:
            self.head = self.tail = Node(item)
        else:
            self.head = Node(item, next=self.head)
        self.size += 1

    def remove(self, index):
        if index < 0 or index + 1 > self.size:
            raise ValueError("negative index")
        if index == 0:
            self.head = self.head.next
            if self.size == 1:
                self.tail = self.head
        else:
            node = self.head
            for i in range(index-1):
                node = node.next
            node.next = node.next.next
            if index == self.size - 1:
                self.tail = node
        self.size -= 1

    def __iter__(self):
        node = self.head
        while node:
            content = node.content
            node = node.next
            yield content
