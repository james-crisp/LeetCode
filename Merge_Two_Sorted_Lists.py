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
        
        def iterList(lister):
            if lister == None:
                return
            else:
                list3.append(lister.val)
                iterList(lister.next)
        
        iterList(list1)
        iterList(list2)
        
        list3.sort()
        
        return list3
            
        