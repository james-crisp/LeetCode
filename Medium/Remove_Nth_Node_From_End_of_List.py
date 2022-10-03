#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 19:49:48 2022

@author: jamescrisp
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        test = head
        cur = dummy = ListNode()
        
        
        count = 0
        
        #Count how long linked list is
        while test:
            count += 1
            test = test.next
        
        #Remove Nth Node
        count = count - n
        count2 = 0
        while head:
            if count2 == count:
                cur.next = head.next
                head = head.next
                cur = cur.next
            else:
                cur.next = head
                head = head.next
                cur = cur.next
            
        
        return dummy.next
                    