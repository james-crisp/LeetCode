#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 21:27:35 2022

@author: jamescrisp
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        if left == right:
            return head
        
        nextt = ListNode()
        prev = ListNode()
        
        cur = head
        counter = 0
        
        if left > 1:
            for i in range(left-1):
                prev.next = head
                prev = prev.next
        
        while cur:
            nextt = cur.next
            cur.next, prev.next = prev.next, cur
            cur = nextt
        
        return prev.next
            
        
            
        
        