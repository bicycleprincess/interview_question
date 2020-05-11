class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    def reverse(self): 
        prev = None
        current = self.head
        while current is not None:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        self.head = prev

    def printList(self):
        temp = self.head 
        output = []

        while temp is not None:
            output.append(temp.data)
            temp = temp.next
        return ", ".join(output)

alist = LinkedList([str(x) for x in range(101)])
print(alist.printList())
alist.reverse()
print(alist.printList())

