class Stack:
    def __init__(self, list=None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def __str__(self):
        s = 'stack of' + str(self.size())+'item : '
        for ele in self.item:
            s += str(ele)+''
        return s

    def push_left(self, i):
        self.items.insert(0, i)

    def push_right(self, i):
        self.items.append(i)

    def pop_left(self):
        return self.items.pop(0)

    def pop_right(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)


s1 = Stack()
s1.push_left('A')
s1.push_left('B')
s1.push_left('C')
s1.push_left('D')
print("Push left:", s1.items)
print("********** Pop left ***********")
for i in range(0, s1.size()):
    print(s1.pop_left())
print("*******************************")

s2 = Stack()
s2.push_right('A')
s2.push_right('B')
s2.push_right('C')
s2.push_right('D')
print("Pop right:", s2.items)
print("********** Pop right **********")
for i in range(0, s2.size()):
    print(s2.pop_right())
print("*******************************")

s3 = Stack()
s3.push_left('A')
s3.push_left('B')
s3.push_left('C')
s3.push_left('D')
print("Push left:", s3.items)
print("********** Pop right **********")
for i in range(0, s3.size()):
    print(s3.pop_right())
print("*******************************")

s4 = Stack()
s4.push_right('A')
s4.push_right('B')
s4.push_right('C')
s4.push_right('D')
print("Push right:", s4.items)
print("********** Pop left ***********")
for i in range(0, s4.size()):
    print(s4.pop_left())
print("*******************************")


## -------------------------------------------------------------------------------------------------------------------------- ##
class priNode:

    def __init__(self, data, next_node=None, next_sec=None):
        self.data = data
        self.next_node = next_node
        self.next_sec = next_sec

    def __str__(self):
        return str(self.data)


class secNode:

    def __init__(self, data, next_sec=None):
        self.data = data
        self.next_sec = next_sec

    def __str__(self):
        return str(self.data)


class TwoLinklist:

    def __init__(self):
        self.primary_node = None

    def Append_primary(self, pri_data):
        pri_node = priNode(pri_data)
        if self.primary_node == None:
            self.primary_node = pri_node
        else:
            p_pri_node = self.primary_node
            while p_pri_node.next_node != None:
                p_pri_node = p_pri_node.next_node
            p_pri_node.next_node = pri_node

    def Delete_primary(self, pri_data):
        p_pri_node = self.primary_node
        if p_pri_node.data == pri_data:
            self.primary_node = p_pri_node.next_node
            p_pri_node.next_node = None
        else:
            apri_node_pri_node = p_pri_node.next_node
            while apri_node_pri_node != None:
                if apri_node_pri_node.data == pri_data:
                    temp = apri_node_pri_node.next_node
                    p_pri_node.next_node = temp
                    apri_node_pri_node.next_node = None
                    break
                p_pri_node = p_pri_node.next_node
                apri_node_pri_node = p_pri_node.next_node

    def Append_secondary(self, pri_data, sec_data):
        p_node = self.primary_node
        while p_node != None:
            if p_node.data == pri_data:
                break
            p_node = p_node.next_node
        else:
            return "Can't find"
        sec_node = secNode(sec_data)
        if p_node.next_sec == None:
            p_node.next_sec = sec_node
        else:
            while p_node.next_sec != None:
                p_node = p_node.next_sec
            p_node.next_sec = sec_node

    def Delete_secondary(self, pri_data, sec_data):
        p_node = self.primary_node
        p_sec_node = p_node.next_sec
        while p_node != None:
            if p_node.data == pri_data:
                break
            p_node = p_node.next_node
        else:
            return "Can't find"
        p_sec_node = p_node.next_sec
        while p_sec_node != None:
            if p_sec_node.data == sec_data:
                temp = p_sec_node.next_sec
                p_node.next_sec = temp
                p_sec_node.next_sec = None
                break
            p_node = p_node.next_sec
            p_sec_node = p_node.next_sec

    def Print_List(self):
        p_pri_node = self.primary_node
        while p_pri_node != None:
            print(f"{p_pri_node} : ", end="")
            node_list = []
            point_sec_node = p_pri_node.next_sec
            while point_sec_node != None:
                node_list.append(str(point_sec_node))
                point_sec_node = point_sec_node.next_sec
            print(",".join(node_list))
            p_pri_node = p_pri_node.next_node
        print()


llist = TwoLinklist()
llist.Append_primary('A')
llist.Append_primary('B')
llist.Append_primary('C')


llist.Append_secondary('A', 'A1')
llist.Append_secondary('A', 'A2')
llist.Append_secondary('A', 'A3')
llist.Append_secondary('B', 'B1')
llist.Append_secondary('B', 'B2')
llist.Append_secondary('C', 'C1')
llist.Append_secondary('C', 'C2')

llist.Delete_primary('B')

llist.Delete_secondary('A', 'A2')
llist.Print_List()
