#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 11:04:29 2022

@author: jamescrisp
"""

class Solution:
    def isValid(self, s: str) -> bool:
        
        length = len(s)
        
        if length % 2 != 0:
            return False
        
        parenHash = {")":"(","]":"[","}":"{"}
        queue = []
        
        for x in range(length):
            
            if s[x] == '(' or s[x] == '[' or s[x] == "{":
                queue.append(s[x])
            elif s[x] == ')' or s[x] == "]" or s[x] == "}":
                if len(queue) == 0:
                    return False
                if queue.pop() != parenHash[s[x]]:
                    return False
        
        if len(queue) > 0:
            return False
        
        return True
            

            