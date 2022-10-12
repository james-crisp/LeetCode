#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 21:18:54 2022

@author: jamescrisp
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        cur = dummy = ListNode()
        start = head
        
        count = k
        
        while count > 0:
            if head.next is None:
                cur.next = head
                head = start
                count -= 1
                cur = cur.next
            cur.next = head
            head = head.next
            cur = cur.next
            
        return dummy.next