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
        
        for j in range(len(strs)):
            word = strs[j]
            if len(temp) > 0:
                if sorted(word) == sorted(temp[0]):
                    temp.append(word)
                else:
                    test = False
                    for i in range(len(anagrams)):
                        if sorted(word) == sorted(anagrams[i][0]):
                            anagrams[i].append(word)
                            test = True
                    print(word)
                    print(test)
                    if test == False:
                        if j == len(strs)-1:
                            anagrams.append([word])
                        anagrams.append(temp.copy())
                        temp.clear()
                        temp.append(word)
            else:
                temp.append(word)
        
        
            
            
            
        return anagrams