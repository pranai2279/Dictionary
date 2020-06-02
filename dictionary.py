# -*- coding: utf-8 -*-
"""
Created on Tue May 26 13:29:28 2020

@author: pranai
"""

import json
df = json.load(open(r'C:\Users\pranai\Desktop\ML\Udemy courses\Python bootcamp 15 projects\original.json'))
c='y'
print('----------------------------------')
while(c=='y'):
    s = input('Enter the word to search : ').lower()
    print(df[s])
    c = input('\nEnter y to search again(any key to end) : ').lower()
    print('----------------------------------')

