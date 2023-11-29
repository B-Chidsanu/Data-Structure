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

    def push(self, i):
        self.items.append(i)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)


s1 = Stack(['A', 'B', 'C', 'D', 'E', 'F'])
s1.push
print(s1.items)
for i in range(0, s1.size()):
    print(s1.pop())
