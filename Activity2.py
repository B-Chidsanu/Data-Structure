class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)


class linkList:
    def __init__(self):
        self.head = None

    def append(self, data):
        p = Node(data)
        if self.head == None:
            self.head = p
        else:
            t = self.head
            while t.next != None:
                t = t.next
            t.next = p

    def print_insert(self):
        p = self.head
        print("Insert After")
        while p != None:
            print(f'{p.data}  ', end="")
            p = p.next
        print("")

    def insertAfter(self, prev_node, new_data):
        p = self.head
        while p != None:
            if prev_node == p.data:
                break
            p = p.next
        new_node = Node(new_data, p.next)
        p.next = new_node


llist = linkList()
llist.append('A')
llist.append('B')
llist.append('C')
llist.append('D')
llist.append('E')
llist.append('F')
llist.print_insert()
llist.insertAfter('C', 'X')
llist.insertAfter('X', 'Y')
llist.insertAfter('Y', 'Z')
llist.print_insert()
