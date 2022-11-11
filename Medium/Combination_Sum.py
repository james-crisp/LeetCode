#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 17:32:21 2022

@author: jamescrisp
"""

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        #DFS
        
        total = 0
        num_List = []
        
        def listCheck(numbers):
            
        
        for i in range(len(candidates)):
            total = 0
            temp_List = []
            total += candidates[i]
            temp_List.append(candidates[i])
            if total < target:
                #repeat
            elif total == target:
                num_List.append(temp_List)
            else:
                #break
        
        return num_List
    
    def dfs(self,nums,target,path,ret):
        if target < 0:
            return
        if target == 0:
            ret.append([])
            return
        for i in range(len(nums)):
            return self.dfs(nums[i:],target,path,ret)
    
                
                