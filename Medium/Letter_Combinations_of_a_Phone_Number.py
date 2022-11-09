#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 21:38:24 2022

@author: jamescrisp
"""

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        #hash table
        
        number_map = { '2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz' }
            
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return number_map[0]
        
        prev = self.letterCombinations(number_map[:-1])
        
        return [c+b for c in prev for b in ]
        