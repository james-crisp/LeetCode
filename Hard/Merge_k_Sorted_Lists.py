#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 19:14:31 2022

@author: jamescrisp
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        cur = dummy = ListNode()
        
        while lists:
            
            if lists[0] > lists[1]:
                cur.next = lists[0]
                lists[0] = lists[0].next
                cur = cur.next
            else:
                
        return