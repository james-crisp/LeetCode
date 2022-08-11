#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 11:06:05 2022

@author: jamescrisp
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        numbers = []
        
        def travelList(node):
            
            if node is None: return
            
            numbers.append(node.val)
            travelList(node.next)
            
            return
        
        travelList(head)
        numbersrev = numbers.copy()
        numbersrev.reverse()
        
        if numbers == numbersrev:
            return True
        else:
            return False
        

