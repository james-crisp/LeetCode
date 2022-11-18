#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 22:34:23 2022

@author: jamescrisp
"""

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def para(p, left, right, parens=[]):
            if left:
                para(p + '(', left-1, right)
            if right > left:
                para(p + ')', left, right-1)
            if not right:
                parens += p,
            return parens
        return para('',n,n)