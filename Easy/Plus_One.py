#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 11:54:02 2022

@author: jamescrisp
"""

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        ans = [str(x) for x in digits]
        ans1 = "".join(ans)
        ans2 = int(ans1)
        ans2 += 1
        
        digits1 = []
        
        for x in str(ans2):
            digits1.append(x)
            
        return digits1