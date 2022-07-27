#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 10:54:10 2022

@author: jamescrisp
"""

class Solution:
    import math
    def intToRoman(self, num: int) -> str:
        
        #Utilize a hash table
        #Convert integer to roman numerals
        
        answer = []
        
        roman = {1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M'}
        
        if (num/1000) > 0:
            temp = math.floor(num/1000)
            for i in range(temp):
                answer.append(roman[1000])
        if (num/100) >= 9:
            answer.append(roman[100])
            answer.append(roman[1000])
        
        print(math.floor(8675/1000))
        
        print(roman[1])
        
        return answer
        