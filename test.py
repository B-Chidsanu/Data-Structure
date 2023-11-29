class PriNode:

    def __init__(self, data, next_pri=None, next_sec=None):
        self.data = data
        self.next_pri = next_pri
        self.next_sec = next_sec

    def __str__(self):
        return str(self.data)


class SecNode:

    def __init__(self, data, next_sec=None):
        self.data = data
        self.next_sec = next_sec

    def __str__(self):
        return str(self.data)


class TwoDLinkedList:

    def __init__(self):
        self.head = None

    def append_primary(self, pri_data):
        """
          append primary into 2d linkedlist if head is none else append after last primary node
        """
        pri_node = PriNode(pri_data)
        if self.head == None:
            self.head = pri_node
        else:
            point_pri_node = self.head
            while point_pri_node.next_pri != None:
                point_pri_node = point_pri_node.next_pri
            point_pri_node.next_pri = pri_node

    def delete_primary(self, pri_data):
        """
          delete primary from 2d linkedlist 
        """
        point_pri_node = self.head
        if point_pri_node.data == pri_data:
            self.head = point_pri_node.next_pri
            point_pri_node.next_pri = None
        else:
            ahead_pri_node = point_pri_node.next_pri
            while ahead_pri_node != None:
                if ahead_pri_node.data == pri_data:
                    temp = ahead_pri_node.next_pri
                    point_pri_node.next_pri = temp
                    ahead_pri_node.next_pri = None
                    break
                point_pri_node = point_pri_node.next_pri
                ahead_pri_node = point_pri_node.next_pri

    def append_secondary(self, pri_data, sec_data):
        """
          add sec into pri data
        """
        point_node = self.head
        while point_node != None:
            if point_node.data == pri_data:
                break
            point_node = point_node.next_pri
        else:
            return "Not Found"
        sec_node = SecNode(sec_data)
        if point_node.next_sec == None:
            point_node.next_sec = sec_node
        else:
            while point_node.next_sec != None:
                point_node = point_node.next_sec
            point_node.next_sec = sec_node

    def delete_secondary(self, pri_data, sec_data):
        """
         del sec from pri data
        """
        point_node = self.head
        ahead_sec_node = point_node.next_sec
        while point_node != None:
            if point_node.data == pri_data:
                break
            point_node = point_node.next_pri
        else:
            return "Not Found"
        ahead_sec_node = point_node.next_sec
        while ahead_sec_node != None:
            if ahead_sec_node.data == sec_data:
                temp = ahead_sec_node.next_sec
                point_node.next_sec = temp
                ahead_sec_node.next_sec = None
                break
            point_node = point_node.next_sec
            ahead_sec_node = point_node.next_sec

    def print_list(self):
        """
          print all sec node in all pri node
        """
        point_pri_node = self.head
        while point_pri_node != None:
            print(f"{point_pri_node} : ", end="")
            node_list = []
            point_sec_node = point_pri_node.next_sec
            while point_sec_node != None:
                node_list.append(str(point_sec_node))
                point_sec_node = point_sec_node.next_sec
            print(",".join(node_list))
            point_pri_node = point_pri_node.next_pri
        print()


t1 = TwoDLinkedList()
t1.append_primary("A")
t1.append_primary("B")
t1.append_primary("C")

t1.append_secondary("A", "A1")
t1.append_secondary("A", "A2")
t1.append_secondary("B", "B1")
t1.append_secondary("B", "B2")
t1.append_secondary("C", "C1")
t1.append_secondary("C", "C2")

t1.delete_secondary("C", "C2")
t1.print_list()
