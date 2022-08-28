#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 16:38:53 2022

@author: jamescrisp
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        
        def findNumber(node,numList):
            
            if node is None: return
            
            findNumber(node.next,numList)
            numList.append(node.val)
            
            return
        
        number1 = []
        
        findNumber(l1,number1)
        
        number2 = []
        
        findNumber(l2,number2)
        
        number1 = ''.join(x for str(x) in number1)
        
        print(number1)
        
        return
            
            
        
        