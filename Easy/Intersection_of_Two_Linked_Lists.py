#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 19:55:58 2022

@author: jamescrisp
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        curA = headA
        curB = headB
        
        while curA != curB:
            
            if curA:
                curA = curA.next
            else:
                curA = headA
            
            if curB:
                curB = curB.next
            else:
                curB = headB
        
        return curA