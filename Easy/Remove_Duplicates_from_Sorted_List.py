#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 19:03:06 2022

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
        
        temp = head.val
        cur.next = head
        head = head.next
        
        while head:
            if head.val == temp:
                head = head.next
            else:
                cur.next = head
                temp = head.val
                head = head.next
            
        
        return dummy.next
        
        
            
        
        
        
        
            
        
        