#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 21:50:48 2022

@author: jamescrisp
"""

class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        
        queue = []
        final = list(s)
        
        for char in s:
            if char.isalpha():
                queue.append(char)
        
        for i in range(len(final)):
            if final[i].isalpha():
                final[i] = queue.pop(-1)
                
        s = ''.join(final)
        
        return s
        
        
        
            
                
                    
        
        
        
            
                
                    
                
                    