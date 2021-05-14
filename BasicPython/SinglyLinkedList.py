class Node:

    def __init__(self, value):
        self.next = None
        self.prev = None
        self.value = value


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add(self,value):
        node = Node(value)
        if self.tail is None:
            self.head = node
            self.tail = node
            self.size +=1
        else:
            self.tail.next = node
            node.prev = self.head
            self.tail = node
            self.size +=1

    def __str__(self):
        vals =[]
        node = self.head
        while node is not None:
            vals.append(node.value)
            node = node.next
        return f"[{','.join(str(vals) for val in vals)}]"


my_list = DoubleLinkedList();
my_list.add(5)
my_list.add(6)
my_list.add(7)
print(my_list)
print(my_list.size)
