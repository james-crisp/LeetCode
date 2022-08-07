#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 09:21:28 2022

@author: jamescrisp
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        lister = []
        
        for x in s:
            if x.isalpha(): #check is it's a letter
                lister.append(x.lower()) #add lowercase letter to list
            elif isinstance(int(x),int):
                lister.append(x)
        
        if (len(lister) % 2) == 0: #even amount
            for x in range(int(len(lister)/2)):
                if lister[x] != lister[-1-x]:
                    return False
            return True
        else: #odd amount
            for x in range(int((len(lister)-1)/2)):
                if lister[x] != lister[-1-x]:
                    return False
            return True
        
        return