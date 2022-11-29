#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 18:16:15 2022

@author: jamescrisp
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = []
        temp = []
        
        for word in strs:
            
            if len(temp) > 0:
                if sorted(word) == sorted(temp[0]):
                    temp.append(word)
                else:
                    anagrams.append(temp)
                    temp.clear()
                    temp.append(word)
            else:
                temp.append(word)
                
            
            
            
        return anagrams