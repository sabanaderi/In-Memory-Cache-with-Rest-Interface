# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 12:00:12 2021

@author: saba naderi
"""
from .DataStructure.LinkedList import DoublyLinkedList
from .DataStructure.BST_TTL import BinaryTree
from Definition import CommonConstants
from Definition import EvictionPolicy
import time

class Cache:
    def __init__(self):
        self.capacity = CommonConstants.MAXIMUM_CACHE_ELEMENT_CAPACITY
        self.EvictionPolicy = EvictionPolicy.OLDEST_FIRST
        self.HashMapDDL = {}
        # Tail is the LRU and head is most recent
        self.DoublyLinkedList = DoublyLinkedList()         
        self.BinarySearchTree = BinaryTree()
        

    def get(self, key):
        """
        get(key)
        gets the data stored on the position "key"
        """
        node = self.HashMapDDL.get(key)

        if node:
            self.DoublyLinkedList.moveToFront(node)
            return node.data, node.ttl

        return None, None

    def update(self, key, data, ttl):
        """
        update(key, val, ttl)
        updates (val, ttl) stored on the position "key" 
        """
        nodeDDL = self.HashMapDDL.get(key)
        nodeDDL.data = data
        nodeDDL.ttl = ttl        
        self.DoublyLinkedList.moveToFront(nodeDDL)  
        
        nodeBST = self.BinarySearchTree.searchNode(ttl)
        nodeBST.data["val"] = ttl
        self.BinarySearchTree.insertNode(nodeBST)        

    def insert(self, key, data, ttl):
        """
        insert(key, val, ttl)
        inserts (key, val, ttl) into cache
        """
        # If key already exists, just move to front
        if key in self.HashMapDDL:
            self.update(key, data, ttl)
            return True
        
        if (self.EvictionPolicy == EvictionPolicy.REJECT and 
            self.DoublyLinkedList.size + 1 > self.capacity):
            return False
        
        nodeDDL = self.DoublyLinkedList.prepend(key, data, ttl)
        self.HashMapDDL[key] = nodeDDL
        
        self.BinarySearchTree.insertNode(key, ttl)

        # If exceeds capacity, remove based on eviction policy 
        if self.DoublyLinkedList.size > self.capacity:
            
            if self.EvictionPolicy == EvictionPolicy.OLDEST_FIRST:
                tail = self.DoublyLinkedList.tail 
                return self.remove(tail.key)          
                
            if self.EvictionPolicy == EvictionPolicy.NEWEST_FIRST: 
                head = self.DoublyLinkedList.head
                NewestKeyToRemove = head.next.key
                return self.remove(NewestKeyToRemove)
            

    def remove(self, key):
        """
        remove(key)
        removes object stored on the position "key" 
        """
        nodeDDL = self.HashMapDDL.get(key)

        if nodeDDL:     
            BSTKey = nodeDDL.ttl
            
            del self.HashMapDDL[key]
            
            self.DoublyLinkedList.removeNode(nodeDDL)
            self.BinarySearchTree.deleteNode(BSTKey)
            
            return True
            
        return False
    
    def autoCleanCahce(self):
        """
        autoCleanCahce()
        removes object if its ttl was passed
        """
        DeepestLeftNode = self.BinarySearchTree.deepestLeftNode(self.BinarySearchTree.root) 
        if DeepestLeftNode is None:
            return

        if DeepestLeftNode.ttl < int( time.time() ):
            key = DeepestLeftNode.key
            self.remove(key)
            print("object with key '{}' was removed because of ttl".format(key))            