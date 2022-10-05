#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 21:13:15 2022

@author: jamescrisp
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        cur = dummy = ListNode()
        
        while head:
            print('a')
            cur.next = head.next
            cur = cur.next
            cur.next = head
            cur = cur.next
            head = head.next
            head = head.next
        
        return dummy.next