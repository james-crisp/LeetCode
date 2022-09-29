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
        
        currentNode = dummy = ListNode()
        
        while list1 and list2:
            if list1.val < list2.val:
                currentNode.next = list1
                list1 = list1.next
                currentNode = currentNode.next
                
            
            else:
                currentNode.next = list2
                list2 = list2.next
                currentNode = currentNode.next
                
        
        if list1 or list2: 
            currentNode.next = list1 if list1 else list2
        
        return dummy.next
            
            
            
            
        
            
            
            
            
        
            
            
            
            
        
            
            
            
        
            
            
            
            
        
            
            
            
            
        
            
            
            
            
        
            
            
            
            
        
            
            
            
            
        
            
            
            
        
            
            
            
            
            
        