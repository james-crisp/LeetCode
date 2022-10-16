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
        
        #previous, current and next nodes
        
        nextt = ListNode(None)
        prev = ListNode(None)
        #cur = ListNode()
        cur = head
        
        while cur:
            nextt = cur.next
            cur.next = prev
            prev = cur
            cur = nextt
            
        return prev
        
        
            
            
        
            
            
        