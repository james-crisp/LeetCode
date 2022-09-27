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
        
        currentNode = headHold = ListNode()
        
        
        
        while list1 and list2:
            if list1.val < list2.val:
                currentNode = list1
                print(currentNode.val)
                list1 = list1.next
                currentNode = currentNode.next
                
            
            else:
                currentNode = list2
                print(currentNode.val)
                list2 = list2.next
                currentNode = currentNode.next
                
        
        if list1 or list2: 
            if list2 is None:
                currentNode = list1 
            else: 
                currentNode = list2
            print(currentNode.val)
        
        return headHold.next
            
            
            
            
        
            
            
            
            
        
            
            
            
            
        
            
            
            
        
            
            
            
            
            
        