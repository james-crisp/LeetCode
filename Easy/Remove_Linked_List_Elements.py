#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 18:31:50 2022

@author: jamescrisp
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        
        def removeIt(node):
            
            if node is None:
                return
            
            if node.next is None:
                return
            
            if node.val == val:
                print(node.val)
                temp = node
                node = node.next
                removeIt(node)
            else:
                print(node.val)
                removeIt(node.next)
            
            return
        
        removeIt(head)
        
        return head