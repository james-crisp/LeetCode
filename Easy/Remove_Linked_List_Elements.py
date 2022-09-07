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
        
        if head is None:
            return head
        
        if head.val == val:
            head = head.next
        
        def removeIt(node):
            
            if node is None:
                return
            
            if node.next is None:
                return
            
            if node.next.val == val:
                node.next = node.next.next
            
            removeIt(node.next)
            
            return
        
        removeIt(head)
        removeIt(head)
        
        if head is None:
            return None
        
        if head.val == val:
            return None
        
        return head