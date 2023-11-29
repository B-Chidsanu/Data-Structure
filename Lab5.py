# #ข้อที่1
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
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


root = Node(15)
root.insert(3)
root.insert(16)
root.insert(9)
root.insert(23)
root.insert(11)
root.insert(7)
root.insert(5)
root.insert(34)
root.insert(19)
root.insert(2)
root.PrintTree()
## -------------------------------------------------------------------------------------------------------------------------##

# # ข้อที่2


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()

    def inorderTraversal(self, root):
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.data)
            res = res + self.inorderTraversal(root.right)
        return res

    def preorderTraversal(self, root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.preorderTraversal(root.left)
            res = res + self.preorderTraversal(root.right)
        return res

    def postorderTraversal(self, root):
        res = []
        if root:
            res = res + self.postorderTraversal(root.left)
            res = res + self.postorderTraversal(root.right)
            res.append(root.data)
        return res


root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
print('preorderTraversal-->', root.preorderTraversal(root))
print('postorderTraversal-->', root.postorderTraversal(root))
print('inorderTraversal-->', root.inorderTraversal(root))

## -------------------------------------------------------------------------------------------------------------------------##
# ช้อที่3


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
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


root = Node(15)
root.insert(3)
root.insert(16)
root.insert(9)
root.insert(23)
root.insert(11)
root.insert(7)
root.insert(5)
root.insert(34)
root.insert(19)
root.insert(2)
root.PrintTree()
## -------------------------------------------------------------------------------------------------------------------------##

# # ข้อที่3


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data >= self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data),
        if self.right:
            self.right.printTree()

    def inorderTraversal(self, root):
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.data)
            res = res + self.inorderTraversal(root.right)
        return res

    def preorderTraversal(self, root):
        pre_res = []
        if root:
            pre_res.append(root.data)
            pre_res += self.preorderTraversal(root.left)
            pre_res += self.preorderTraversal(root.right)
        return pre_res

    def postorderTraversal(self, root):
        post_res = []
        if root:
            post_res += self.postorderTraversal(root.left)
            post_res += self.postorderTraversal(root.right)
            post_res.append(root.data)
        return post_res

    def BST(self, root):
        bst_res = []
        queue_list = []
        queue_list.append(root)
        while len(queue_list) > 0:
            child_list = []
            a = queue_list.pop(0)
            if a:
                bst_res.append(a.data)
            if a.left:
                child_list.append(a.left)
            if a.right:
                child_list.append(a.right)
            for b in child_list:
                queue_list.append(b)
        return bst_res


root = Node(15)
for i in (3, 16, 9, 23, 11, 7, 5, 34, 19, 2):
    root.insert(i)
print(f'{root.BST(root)}')
