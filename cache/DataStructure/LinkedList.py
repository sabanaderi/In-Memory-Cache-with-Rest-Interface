# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 12:00:12 2021

@author: saba naderi
"""
class DLLNode:
    """
    A node in a doubly-linked list.
    """
    def __init__(self, key=None, data=None, ttl = None, prev=None, next=None):
        self.key = key
        self.data = data
        self.prev = prev
        self.next = next
        self.ttl = ttl

class DoublyLinkedList:
    def __init__(self):
        """
        Create a new doubly linked list.
        """
        self.head = None
        self.tail = None
        self.size = 0

    def moveToFront(self, node):
        """
        moveToFront(node: DLLNode)
        Move the node in to the beginning of the list.
        """
        if node is not self.head:
            self.removeNode(node)
            self.prepend(node.key, node.data, node.ttl)

    def prepend(self, key, data, ttl):
        """
        prepend(node: DLLNode)
        Insert a new element at the beginning of the lst.
        """
        new_head = DLLNode(key=key, data=data, ttl=ttl, next=self.head)
        if self.head:
            self.head.prev = new_head
        else:
            self.tail = new_head

        self.head = new_head
        self.size += 1

        return new_head

    def removeNode(self, node):
        """
        removeNode(node: DLLNode)
        Remove an element from the list.
        """
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        if node is self.head:
            self.head = node.next
        if node is self.tail:
            self.tail = node.prev

        node.prev = None
        node.next = None
        self.size -= 1