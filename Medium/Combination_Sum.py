#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 17:32:21 2022

@author: jamescrisp
"""

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        #DFS
        ret = []
        self.dfs(candidates,target,[],ret)
        return ret
    
    
    def dfs(self,nums,target,path,ret):
        if target < 0:
            return
        if target == 0:
            ret.append(path)
            return
        for i in range(len(nums)):
            self.dfs(nums[i:],target-nums[i],path+[nums[i]],ret)
    
                
    
                
    
                
                