#!/usr/bin/env python
# -*- encoding: utf-8 -*-

class BiTree:
    def __init__(self, Node) -> None:
        self.root = Node
        
    def insert(self,*args):
        if not args:
            return
        if not self.root:
            self.root = Node(args[0])
            args = args[1:]
        for i in args:
            seed = self.root
            while True:
                if i > seed.name:
                    if not seed.right:
                        node = Node(i)
                        seed.right = node
                        break
                    else:
                        seed = seed.right
                else:
                    if not seed.left:
                        node = Node(i)
                        seed.left = node
                        break
                    else:
                        seed = seed.left
        
    def __next__(self):
        if self.root is None:
            raise StopIteration
        Node, self.root = self.root, self.root.left
        return Node
    
    def __iter__(self):
        return self
        

class Node:
    def __init__(self, name) -> None:
        self.name = name
        self.left = None
        self.right = None
    
    def __iter__(self):
        return BiTree(self)

def pre_order(root):
    if not root:
        return
    print(root.name)
    pre_order(root.left)
    pre_order(root.right)
    