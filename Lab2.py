# ข้อ 1.1
def remove_even(lst):
    # insert code here
    return [num for num in lst if num % 2 != 0]


A = [1, 2, 3, 4, 5, 6, 7]
B = remove_even(A)
print(B)  # [1,3,5,7]

# ข้อ 1.2


class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None


class Slinkedlink:
    def __init__(self):
        self.headval = None

    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval


list = Slinkedlink()
list.headval = Node("abcd")

n2 = Node("efgh")
n3 = Node("ijkl")
n4 = Node("mnop")
n5 = Node("qrst")
n6 = Node("uvw")
n7 = Node("xyz")

list.headval.nextval = n2
n2.nextval = n3
n3.nextval = n4
n4.nextval = n5
n5.nextval = n6
n6.nextval = n7
n7.nextval = list.headval

list.listprint()

# ข้อ 1.3
stack = []
name = str(input("Enter Your Name :"))
for i in name:
    stack.append(i)
print("Initial stack =", stack)
print("Elements popped from stack :")
for i in range(len(stack)):
    print("|" + stack.pop() + "|")

# ข้อ 1.4


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data > self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data < self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()


root = Node(3)
root.insert(1)
root.insert(0)
root.insert(2)
root.insert(5)
root.insert(4)
root.insert(7)

print("Output :")
root.PrintTree()
