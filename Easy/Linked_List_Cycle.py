#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 10:37:41 2022

@author: jamescrisp
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        if head is None: return False
        
        slow = head
        fast = head.next
        
        while slow != fast:
            
            if (fast is None) or (fast.next is None):
                return False
            
            slow = slow.next
            fast = fast.next.next
        
        return True