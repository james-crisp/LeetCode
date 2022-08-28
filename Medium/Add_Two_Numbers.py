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
        
        num1 = ''.join(str(x) for x in number1)
        num2 = ''.join(str(x) for x in number2)
        num3 = int(num1) + int(num2)
        num3 = str(num3)
        
        
        return
            
            
        
        
        