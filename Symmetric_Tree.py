#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 14:17:02 2022

@author: jamescrisp
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        #recursive solve with binary tree
        
        
        def check(val):
            val.left
            if check(root.left) == check(root.right):
                root
                
        check(root)
        
        return