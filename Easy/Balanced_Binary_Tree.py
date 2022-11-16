#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 19:20:01 2022

@author: jamescrisp
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        #count = 0
        
        def balance(node):
            #nonlocal count
            
            if node is None:
                return 0
                
            left = balance(node.left)
            right = balance(node.right)
            if left == -1 or right == -1 or abs(left-right) > 1:
                return -1
            return 1 + max(left,right)
        
        return balance(root) != -1