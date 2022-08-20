#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 19:14:55 2022

@author: jamescrisp
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        reversedList = ListNode()
        
        def reverseIt(node):
            if node is None: return
            
            reversedList.next = ListNode(node.val)
            reverseIt(node.next)
            
            
        reverseIt(head)
        
        return reversedList
            
            
        