#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 20:32:45 2022

@author: jamescrisp
"""

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def permutations(sets,n):
            if n == 0:
                return [[]]
            
            l = []
            for i in range(0, len(sets)):
                m = sets[i]
                remLst = sets[i+1:]
                
                remainlst_combo = permutations(remLst,n-1)
                for p in remainlst_combo:
                    l.append([m, *p])
            
            return l
            
        
        return permutations(nums,3)