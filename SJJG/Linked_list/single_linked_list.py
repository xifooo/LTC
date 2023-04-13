#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
实现单链表的三种方式
"""

# class Node:
#     """
#     很low的做法, 无法for loop, 只能老老实实地重复 print(node.next)
#     """
#     def __init__(self, name) -> None:
#         self.name = name
#         self.next = None
#     def __str__(self) -> str:
#         return f"this is a node: {self.name}"

# node1 = Node("Node 1")
# node2 = Node("Node 2")
# node3 = Node("Node 3")
# node4 = Node("Node 4")

# node1.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = Node("Node 5")

# print(node1.next)
# print(node2.next)
# print(node3.next)
# print(node4.next)


# -----------------------------------------------

class Node:
    """
    iterable, 可在链表任意节点开始单向遍历
    """
    def __init__(self, name) -> None:
        self.name = name
        self.next = None
    
    def __iter__(self):
        Node = self
        while Node is not None:
            yield Node
            Node = Node.next
            
    def __str__(self) -> str:
        return f"this is a node: {self.name}"
    
    def append(self, new_node):
        """插入/追加插入: 单个node"""
        if self.next is None:
            self.next = new_node
        else:
            self.next, new_node.next = new_node, self.next
    
    def search(self, target):
        """单向搜索: 确定 当前node之后 是否存在 目标node"""
        for n in self:
            if n.name == target:
                return True
            if n.next is None:
                return False

    def head_node(self):
        """返回head node"""
        "单链表, 没办法"
            
    def delete(self):
        """ 删除node"""
        "单链表, 没办法"
        
node1 = Node("Node 1")
node2 = Node("Node 2")
node3 = Node("Node 3")
node4 = Node("Node 4")
node1.append(node4)
node3.append(node1)
node1.append(node2)

print(node1.search("Node 3"))


# -----------------------------------------------------
# node是一个对象, node之间的link也是一个对象
# class Node_iter:
#     def __init__(self, Node) -> None:
#         self.cur_node = Node
        
#     def __next__(self):
#         if self.cur_node is None:
#             raise StopIteration
#         Node, self.cur_node = self.cur_node, self.cur_node.next
#         return Node
    
#     def __iter__(self):
#         return self
        

# class Node:
#     def __init__(self, name) -> None:
#         self.name = name
#         self.next = None
    
#     def __iter__(self):
#         return Node_iter(self)
    
#     def __str__(self) -> str:
#         return f"this is a node: {self.name}"
    
    
# node1 = Node('node 1')
# node2 = Node('node 2')
# node3 = Node('node 3')
# node1.next = node2
# node2.next = node3

# for n in node1:
#     print(n)
    
    
# class Node_iter:
#     def __init__(self, Node) -> None:
#         self.cur_node = Node
        
#     def __next__(self):
#         if self.cur_node is None:
#             raise StopIteration
#         Node, self.cur_node = self.cur_node, self.cur_node.next
#         return Node
    
#     def __iter__(self):
#         return self
        

# class Node:
#     def __init__(self, name) -> None:
#         self.name = name
#         self.next = None
    
#     def __iter__(self):
#         return Node_iter(self)
    
#     def __str__(self) -> str:
#         return f"this is a node: {self.name}"
    
    
# node1 = Node('node 1')
# node2 = Node('node 2')
# node3 = Node('node 3')
# node1.next = node2
# node2.next = node3

# for n in node1:
#     print(n)

