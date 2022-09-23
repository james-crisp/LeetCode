#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 21:50:48 2022

@author: jamescrisp
"""

class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        
        count = -1
        
        for i in range(int(len(s)/2)):
            
            if s[i].isalpha():
                while !s[-i+count].isalpha:
                    count -= 1
                
                temp = s[i]
                s[i] = s[-i+count]
                s[-i+count] = s[i]
                
                    