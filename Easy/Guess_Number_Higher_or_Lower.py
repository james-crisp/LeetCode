#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 19:36:38 2022

@author: jamescrisp
"""

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        
        #Binary search
        
        low = 1
        upp = 2**31-2
        k = guess(n)
        
        while k!=0:
            mid = int((low+upp)/2)
            k = guess(mid)
            if k == -1:
                upp = mid
            elif k == 1:
                low = mid
            else:
                return mid
        
        return n