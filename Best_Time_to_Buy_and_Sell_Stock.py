#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 10:17:26 2022

@author: jamescrisp
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        minn = prices[0]
        diff = 0
        
        for i in range(1,len(prices)):
            if prices[i] < minn:
                minn = prices[i]
            elif prices[i] - minn > diff:
                diff = prices[i] - minn
        
        return diff
        