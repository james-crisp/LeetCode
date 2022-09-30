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
        
        temp = -101
        
        while head:
            if head.val == temp:
                head = head.next
                cur.next = head
            else:
                cur.next = head
                temp = head.val
                head = head.next
                cur = cur.next
            
        
        return dummy.next
        
        
            
        
        
        
        
            
        
        
        
            
        
        
        
        
            
        
        
        
        
            
        
        