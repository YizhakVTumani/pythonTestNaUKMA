import math

class LinkedList:
    head = None
    class Node:
        data = None
        next_node = None
        def __init__(self, data, next_node = None):
            self.data = data
            self.next_node = None
    def append(self, data):
        if not self.head:
            self.head = self.Node(data)
            return data
        node = self.head
        while node.next_node:
            node = node.next_node
        node.next_node = self.Node(data)



    def find_n_element(self): # method that finds 2 * n / 3 - 1 element in the list
        if self.head is not None:
            node = self.head
            n = 0
            while node.next_node:
                node = node.next_node
                n += 1
            n = math.ceil(2 * n / 3 - 1)
            node = self.head
            for i in range(n):
                if node.next_node:
                    node = node.next_node
            print(node.data)
            return node.data
        else :
            print('list is null!')
            return None

LL = LinkedList()

LL.append(3)
LL.append(5)
LL.append(8)
LL.append(3)
LL.append(4)
LL.append(5)

LL.find_n_element()


