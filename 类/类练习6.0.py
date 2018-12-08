# 用面向对象的方法设计一个单向链表类，并实现追加元素，迭代元素，删除元素的方法
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
    def __repr__(self):
        return "<node:{}>".format(self.data)         # 魔术方法

    __str__ = __repr__

class LinkList:
    def __init__(self):    # 列表
        self.list = []
        self.head = None
        self.tail = None



    def append_node(self,node:Node):       # 追加
        if self.head is None:
            self.head = node

        else:
            pre = self.tail
            pre.next = node

        self.tail = node
        self.list.append(node)


    def iternode(self):
        current = self.head
        while current:                        # 迭代
            yield current
            current = current.next

    def popnode(self):
        if self.head is None:
            raise NotImplementedError         # 删除
        for node in self.iternode():
            x = node.next
            if x is not None:
                xx = x.next
                if xx is None:
                    node.next = None
                    self.tail = node
                    return x
            else:
                self.head = None
                return node

node1 = Node(3)
node2 = Node(5)
node3 = Node(6)
link = LinkList()
link.append_node(node1)
link.append_node(node2)
link.append_node(node3)
#link.popnoed()
#link.popnoed()
#link.popnoed()
for node in link.iternode():
    print(node)