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
        
        count = 0
        
        def balance(node):
            nonlocal count
            
            if node is None:
                return
            
            if node.left is None:
                
            balance(node.left)
            balance(node.right)
            
        
        boolean = balance(root)
        
        return boolean