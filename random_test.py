'''
@Author: Never
@Date: 2020-06-22 11:19:36
@Description: 
@LastEditTime: 2020-06-22 11:43:58
@LastEditors: Never
'''

import random

m=0
n=0
t=0
ilist=[]
while t<10000:
    i=random.randint(1,101)
    ilist.append(i)
    if i>=40:
        m+=1
    else:
        n+=1
    t+=1
print(ilist)
print(m/(m+n))
print(n/(n+m))
    