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
            #print(anagrams)
            #print(temp)
            if len(anagrams) > 0:
                test = False
                for i in range(len(anagrams)):
                    if sorted(word) == sorted(anagrams[i]):
                        anagrams[i].append(word)
                        test = True
                        break
                if test == False:
                    anagrams.append(word)
            else:
                anagrams.append(word)
                
            
            
            
        return anagrams