#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# class Node:
#     """
#     双向链表, 可在任意节点处增、删、查
#     """
#     def __init__(self, name) -> None:
#         self.name = name
#         self.next = None
#         self.prev = None
    
#     def __iter__(self):
#         Node = self
#         while Node is not None:
#             yield Node
#             Node = Node.next
            
#     def __str__(self) -> str:
#         return f"this is a node: {self.name}"
    
#     def append(self, new_node):
#         """插入: 在任意节点后面插入单个node"""
#         if self.next is None:
#             self.next, new_node.prev = new_node, self
#         else:
#             new_node.next = self.next
#             self.next = new_node
#             new_node.prev = self

#     def head_node(self):
#         """返回head node"""
#         node = self
        
#         if node.prev is None:
#             return node

#         while node.prev is not None:
#             node = self.prev
#             if node.prev is None:
#                 return node
            
#     def delete(self):
#         """删除 node"""
#         for n in self.head_node():
#             if n.next is self:
#                 n.next = self.next
#             elif n.prev is self:
#                 n.prev = self.prev
#             self.prev, self.next = None, None
    
#     def search(self, target):
#         """搜索: 确定链表中是否存在 name=target 的目标node"""
#         head_node = self.head_node()
#         for n in head_node:
#             if n.name == target:
#                 return True
#             if n.next is None:
#                 return False


# ----------------------------
class Node:
    """
    双向链表, 可在任意节点处增、删、查
    """
    def __init__(self, name) -> None:
        self.name = name
        self._next = None
        self._prev = None
    
    def __iter__(self):
        Node = self
        while Node is not None:
            yield Node
            Node = Node.next
            
    def __str__(self) -> str:
        return f"this is a node: {self.name}"
    @property
    def prev(self):
        return self._prev
    
    @prev.setter
    def prev(self, value):
        self._prev = value
        
    @property
    def next(self):
        return self._next
    
    @next.setter
    def next(self, value):
        self._next = value
    
    def append(self, new_node):
        """插入: 在任意节点后面插入单个node"""
        if self.next is None:
            self.next, new_node.prev = new_node, self
        else:
            new_node.next = self.next
            self.next = new_node
            new_node.prev = self

    def head_node(self):
        """返回head node"""
        node = self
        
        if node.prev is None:
            return node

        while node.prev is not None:
            node = self.prev
            if node.prev is None:
                return node
            
    def delete(self):
        """删除 node"""
        self.prev.next = self.next
        self.next.prev = self.prev
        self.next, self.prev = None, None
        # for n in self.head_node():
        #     if n.next is self:
        #         n.next = self.next
        #     elif n.prev is self:
        #         n.prev = self.prev
        #     self.prev, self.next = None, None
    
    def search(self, target):
        """搜索: 确定链表中是否存在 name=target 的目标node"""
        head_node = self.head_node()
        for n in head_node:
            if n.name == target:
                return True
            if n.next is None:
                return False

        
node1 = Node("Node 1")
node2 = Node("Node 2")
node3 = Node("Node 3")
node4 = Node("Node 4")

# # 增
node1.append(node4)
node3.append(node1)
node1.append(node2)

# # 查
print(node1.search("Node 3"))
print(node1.head_node().name)
print("--------从头遍历:")
for n in node1.head_node(): print(n)

# 删
node1.delete()
print("--------从头遍历:")
for n in node3.head_node(): print(n)
