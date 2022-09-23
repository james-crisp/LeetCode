#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 21:50:48 2022

@author: jamescrisp
"""

class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        
        count = -1
        list1 = list(s)
        
        for i in range(int(len(s)/2)):
            
            if s[i].isalpha():
                
                while not s[count].isalpha():
                    print('a')
                    count -= 1
                
                temp = s[i]
                list1[i] = s[count]
                list1[count] = s[i]
        
        s = ''.join(list1)
        
        return s
        
        
        
            
                
                    
                
                    