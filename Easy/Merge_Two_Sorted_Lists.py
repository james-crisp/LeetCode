#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 09:35:41 2022

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
        
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        
        dummy = ListNode()
        currentNode = dummy
        
        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                list1 = list1.next
            
            else:
                list1 = list2
        
        return list1
            
            
            
            
        