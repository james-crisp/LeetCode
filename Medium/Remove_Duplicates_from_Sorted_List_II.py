#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 20:43:20 2022

@author: jamescrisp
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        cur = dummy = ListNode()
        
        value = head.val
        print(value)
        while head:
            print(value)
            if head.next is None:
                cur.next = head
            elif value == head.next.val:
                head = head.next
            else:
                value = head.val
                cur.next = head
                cur = cur.next
                head = head.next
        
        return dummy.next