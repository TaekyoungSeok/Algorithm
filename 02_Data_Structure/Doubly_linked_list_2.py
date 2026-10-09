class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_first(self, data):
        newnode = Node(data)

        newnode.next = self.head

        if self.head is None:
            self.tail = newnode
        else:
            self.head.prev = newnode

        self.head = newnode

    def insert_last(self, data):
        newnode = Node(data)

        newnode.prev = self.tail

        if self.tail is None:
            self.head = newnode
        else:
            self.tail.next = newnode

        self.tail = newnode

    def insert_after(self, target, data):
        target = self.search(target)

        if target is None:
            return
        
        newnode = Node(data)

        newnode.prev = target
        newnode.next = target.next

        if target.next is None:
            self.tail = newnode
        else:
            target.next.prev = newnode

        target.next = newnode

    def delete_first(self):
        if self.head is None:
            return

        self.head = self.head.next

        if self.head is None:
            self.tail = None
        else:
            self.head.prev = None

    def delete_last(self):
        if self.tail is None:
            return

        self.tail = self.tail.prev

        if self.tail is None:
            self.head = None
        else:
            self.tail.next = None

    def delete(self, data):
        del_node = self.search(data)

        if del_node is None:
            return
        elif del_node.prev is None:
            self.delete_first()
        elif del_node.next is None:
            self.delete_last()
        else:
            del_node.prev.next = del_node.next
            del_node.next.prev = del_node.prev

    def search(self, data):
        find_node = self.head

        while find_node is not None:
            if find_node.data == data:
                return find_node

            find_node = find_node.next

        return None

    def print_forward(self):
        print_node = self.head

        while print_node is not None:
            print(print_node.data, end = ' ')

            print_node = print_node.next

        print("")

    def print_backward(self):
        print_node = self.tail

        while print_node is not None:
            print(print_node.data, end = ' ')

            print_node = print_node.prev

        print("")

if __name__ == '__main__':
    L = DoublyLinkedList()

    L.insert_first(20)
    L.insert_first(10)
    L.insert_last(30)
    L.insert_last(40)

    print("Forward : ", end = '')
    L.print_forward()

    print("backward : ", end = '')
    L.print_backward()

    L.insert_after(20, 25)

    print("After insert : ", end = '')
    L.print_forward()

    L.delete_first()
    L.delete_last()
    L.delete(25)

    print("After delete : ", end = '')
    L.print_forward()

    node = L.search(30)

    if node is not None:
        print("Found : ", node.data)
    else:
        print("Not Found")