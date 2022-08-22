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
        
        counter = 0
        temp = 0
        
        if root is None:
            return 0
        
        def traverseTree(node):
            nonlocal counter
            nonlocal temp
            
            temp += 1
            
            if node is None:
                if temp > counter:
                    counter = temp
                temp = 0
                return 0
            
            
            
            return traverseTree(node.left) + node.val + traverseTree(node.right)
        
        total = traverseTree(root)
        
        return counter
        
        