#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 19:55:04 2022

@author: jamescrisp
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root, depth):
            if not root: return depth
            return min(dfs(root.left,depth+1),dfs(root.right,depth+1))
            
        return dfs(root,0)
            