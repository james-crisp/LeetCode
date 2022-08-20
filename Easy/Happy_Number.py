#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 11:13:51 2022

@author: jamescrisp
"""

class Solution:
    def isHappy(self, n: int) -> bool:
        
        first = str(n)
        
        def tester(number):
            number_string = str(number)
            
            total = 0
            for x in range(len(number_string)):
                total = total + int(number_string[x])**2
            print(total)
            
            if total == 1:
                return True
            else:
                tester(total)
                
        boolean = bool(tester(n))
        print(boolean)
        
        return tester(n)
                