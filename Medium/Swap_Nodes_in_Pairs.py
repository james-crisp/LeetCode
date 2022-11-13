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
        
        if not head or not head.next:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        
        while cur.next and cur.next.next:
            print('a')
            prev = head
            cur.next = head.next
            cur = cur.next
            cur.next = prev
            cur = cur.next
            head = head.next
            print(head.val)
            
        
        return dummy.next