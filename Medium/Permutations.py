#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 20:32:45 2022

@author: jamescrisp
"""

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def permutations(lst):
            if len(lst) == 0:
                return []
            if len(lst) == 1:
                return [lst]
            
            l = []
            for i in range(len(lst)):
                m = lst[i]
                remLst = lst[:i] + lst[i+1:]
                
                for p in permutations(remLst):
                    l.append([m] + p)
                
            return l

        answer = permutations([x for x in nums])
        

        return answer