#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 11:13:51 2022

@author: jamescrisp
"""

class Solution:
    def isHappy(self, n: int) -> bool:
        
        k = 0
        current_number = list(str(n))
        
        while k < 100:
            total = 0
            for sub_number in current_number:
                total+=(int(sub_number)**2)
            if total == 1:
                return True
            else:
                current_number = list(str(total))
            k+=1
        
        return False
                