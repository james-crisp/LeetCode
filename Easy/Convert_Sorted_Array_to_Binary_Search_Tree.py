#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 16:49:44 2022

@author: jamescrisp
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        total_numbers = len(nums)
        if not total_numbers:
            return None
        
        middle_node = total_numbers // 2
        return TreeNode(
            nums[middle_node],
            self.sortedArrayToBST(nums[:middle_node]), self.sortedArrayToBST(nums[middle_node+1 :])
        )