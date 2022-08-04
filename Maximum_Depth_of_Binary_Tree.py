#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 17:06:34 2022

@author: jamescrisp
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        final = 0
        test = 0
        
        def depth(root):
            global test
            
            if root is None: 
                if test > final:
                    final = test
                test = 0
                return
            
            test = test + 1
            depth(root.left)
            depth(root.right)
            return
        
        depth(root)
        
        return final