#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 21:07:51 2022

@author: jamescrisp
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        answer = True
        
        def checktree(nodea,nodeb):
            nonlocal answer
            
            if nodea is None and nodeb is None:
                return
            elif nodea is None or nodeb is None:
                print("check")
                answer = False
                return
            
            if nodea.val != nodeb.val:
                answer = False
                return
            
            checktree(nodea.left,nodeb.left)
            checktree(nodea.right,nodeb.right)
        
            return
        
        checktree(p,q)
        return answer