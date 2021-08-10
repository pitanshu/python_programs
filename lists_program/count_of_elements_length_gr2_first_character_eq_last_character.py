# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 11:41:16 2020

@author: pitan
"""

list=['abc','aba','121','1234']
cntr=0

for i in list:
    if((len(i)>=2)and(i[0]==i[-1])):
        cntr=cntr+1

print(cntr)