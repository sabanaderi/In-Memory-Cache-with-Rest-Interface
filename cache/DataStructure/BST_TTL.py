# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 18:43:01 2021

@author: saba naderi
"""
import copy
class BSTNode:
    """
    A node in a Binary Search Tree 
    Each node stores values of key and ttl {"key": key, "val" :ttl}
    """
    def __init__(self, key=None, ttl=None):
        self.left = None
        self.right = None
        self.parent = None
        self.key = key
        self.ttl = ttl 
        
    def setLeft(self, left):
        """
        setLeft(left: BSTNode)
        Sets left child
        """
        self.left = left

    def setRight(self, right):
        """
        setRight(right: BSTNode)
        Sets right child
        """
        self.right = right
        
    def setParent(self, parent):
        """
        setParent(parent: BSTNode)
        Sets parent
        """
        self.parent = parent
        
    def setChild(self, old_child_data, new_child):
        """
        setChild(old_child_data, new_child: BSTNode)
        Sets a new child
        """
        if self.left is not None and self.left.ttl == old_child_data:
            self.setLeft(new_child)
        if self.right is not None and self.right.ttl == old_child_data:
            self.setRight(new_child)
            
    def deleteChild(self, ttl):
        """
        deleteChild(key)
        Deletes a child by key
        """
        if self.left is not None and self.left.ttl == ttl:
            self.left = None
        elif self.right is not None and self.right.ttl == ttl:
            self.right = None
        
            
class BinaryTree:
    
    def __init__(self):
        self.root = None
        
    def resetRoot(self):
        """
        resetRoot(parent: BSTNode)
        Resets root
        """
        self.root = None
        
    def updateRoot(self, node):
        """
        updateRoot(node: BSTNode)
        Updates root with node
        """
        self.root = node  
        self.root.parent = None
        
    def insertNode(self, key, ttl):
        """
        insertNode(node: BSTNode)
        inserts a node in BST
        """
        node = BSTNode(key,ttl)
        if self.root is None:
            self.root = node
            return node
        else:            
            root = self.root
            while True:
                if node.ttl < root.ttl:
                    if root.left is None:
                        root.setLeft(node)
                        node.setParent(root)
                        return root.left
                    root = root.left
                else:
                    if root.right is None:
                        root.setRight(node)
                        node.setParent(root)
                        return root.right
                    root = root.right
          
                
    def searchNode(self, value):
        """
        searchNode(value)
        Searches a node by value.
        """
        root = self.root
        while True:
            if root.ttl == value:
                return root
            if value < root.ttl:
                root = root.left
            else:
                root = root.right
                    
    def deleteNode(self, key):
        """
        deleteNode(Node: BSTNode)
        Deletes a node from Binary Search Tree
        """
        node = self.searchNode(key)
        fNodeIsRoot = 1 if node.parent is None else 0
        
        if not fNodeIsRoot and node.left == node.right is None:
            node.parent.deleteChild(key)
            
        elif fNodeIsRoot and node.left == node.right is None:
            self.resetRoot()
            
        elif fNodeIsRoot and node.left is not None and node.right is None:
            RootCopy = copy.deepcopy(self.root)
            node.deleteChild(node.left.key)            
            self.updateRoot(RootCopy.left)
            
        elif fNodeIsRoot and node.right is not None and node.left is None:             
            RootCopy = copy.deepcopy(self.root)
            node.deleteChild(node.right.key)            
            self.updateRoot(RootCopy.right)
            
        elif node.left is not None and node.right is None:
            node.parent.setChild(key, node.left)
            
        elif node.right is not None and node.left is None: 
            node.parent.setChild(key, node.right)
            
        else:
            min_right = self.findMinNode(node.right)
            self.deleteNode(min_right.ttl)
            node.key = min_right.key
            node.ttl = min_right.ttl
            
    def deepestLeftNode(self, root):
        """
        deepestLeftNode(root: BSTNode)
        Finds the deepest left node on Binary Search Tree
        """
        if root is None:
            return 
        if not root.left:
            return root
        
        return self.deepestLeftNode(root.left)     
    
    @staticmethod
    def findMinNode(node):
        """
        findMinNode(node: BSTNode)
        Searches for node with minimal value in subtree
        """
        while True:
            if node.left is None:
                return node
            node = node.left
        