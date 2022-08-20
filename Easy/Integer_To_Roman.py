#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 10:13:32 2022

@author: jamescrisp
"""

class Solution:
    import math
    def intToRoman(self, num: int) -> str:
        
        #Utilize a hash table
        #Convert integer to roman numerals
        
        answer = []
        
        numstr = [int(x) for x in str(num)] #Convert number to list of integers
        
        roman = {1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M'}
        
        if len(numstr) > 3:
            for j in range(numstr[0]):
                answer.append(roman[1000])
            if numstr[1] == 4 or numstr[1] == 9:
                if numstr[1] == 4:
                    answer.append(roman[100])
                    answer.append(roman[500])
                if numstr[1] == 9:
                    answer.append(roman[100])
                    answer.append(roman[1000])
            elif numstr[1] > 4:
                answer.append(roman[500])
                for k in range(numstr[1]-5):
                    answer.append(roman[100])
            
        
        return answer