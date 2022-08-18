#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 10:51:42 2022

@author: jamescrisp
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        #Linked list problem
        list3 = ListNode()
        list3.val = 0
        list3.next = ListNode()
        list3.next.val = 4
        
        def mergeIt(node):
            
            if list1.val < list2.val:
                list3.val = list1.val
            else:
                list3.val = list2.val
            
            list3.next = ListNode()
            mergeIt(list3.next)
        
        mergeIt(list3)
        
        return list3
            
        
            
        
        