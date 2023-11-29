# class Node:
#     def __init__(self, data=None, next_node=None):
#         self.data = data
#         self.next_node = next_node

#     def __str__(self):
#         return str(self.data)


# class linklite:
#     def __init__(self):
#         self.head = None

#     def append(self, pri_data):
#         point_node = Node(pri_data)
#         if self.head == None:
#             self.head = point_node
#         else:
#             sec_point = self.head
#             while sec_point.next_node != None:
#                 sec_point = sec_point.next_node
#             sec_point.next_node = point_node

#     def print_list(self):
#         p = self.head
#         while p != None:
#             print(f'{p}--->', end='')
#             p = p.next_node
#         print("None")

#     def remove(self, pri_data):
#         p_node = self.head
#         if p_node == pri_data:
#             self.head = p_node.next_node
#             p_node.next_node = None
#         else:
#             s_p_n = p_node.next_node
#             while s_p_n != None:
#                 if s_p_n.data == pri_data:
#                     temp = s_p_n.next_node
#                     p_node.next_node = temp
#                     s_p_n.next_node = None
#                     break
#                 p_node = p_node.next_node
#                 s_p_n = p_node.next_node
#             print(f'Remove:{s_p_n} ', end='')


# llist = linklite()
# llist.append("A")
# llist.append("B")
# llist.append("C")
# llist.print_list()

# llist.remove("C")
# llist.print_list()

##---------------------------------------------------------------------------------------------##

# class Stack:
#     def __init__(self, list) :
#         if list == None:
#             self.items = []
#         else:
#             self.items = list

#     def __str__(self):
#         return str(self.items)

#     def push(self, i):
#         self.items.append(i)

#     def pop(self):
#         return self.items.pop()

#     def peek(self):
#         return self.items[-1]

#     def size(self):
#         return len(self.items)

#     def isEmpty(self):
#         return self.items == []

# s1 = Stack(["A", "B", "C"])
# s1.push("D")
# print(s1.items, 'peek-->',s1.peek(), 'isEmpty-->',s1.isEmpty())

# for i in range(0,s1.size()):
#     print(s1.pop())


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

  def PrintTree(self):
    if self.left:
      self.left.PrintTree()
    print( self.data),
    if self.right:
      self.right.PrintTree()

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

  def breadthFirst(self, root):
    b_res = []

    q_list = []
    q_list.append(root)
    while len(q_list) > 0:
      child_list = []
      n = q_list.pop(0)
      if n:
        b_res.append(n.data)
      if n.left:
        child_list.append(n.left)
      if n.right:
        child_list.append(n.right)
      for c in child_list:
        q_list.append(c)
    return b_res

root = Node(15)
for i in (3, 16, 9, 23, 11, 7, 5, 34, 19, 2):
  root.insert(i)
print(f"breadth-first: {root.breadthFirst(root)}")
