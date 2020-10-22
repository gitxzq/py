'''
@Author: Never
@Date: 2020-06-18 00:10:40
@Description: 
@LastEditTime: 2020-06-24 10:32:17
@LastEditors: Never
'''
mylist =[1, 1, 1, 2, 1, 2, 2, 2, 1, 2, 2, 2, 1, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 2, 1, 2, 2, 1, 2, 1, 2, 2, 1, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 2, 1, 2, 1, 1, 2, 1, 2, 1, 2, 1, 1, 1, 1, 2, 1, 1, 2, 2, 1, 2, 1, 2, 1, 2, 2, 2, 2, 2, 1, 1, 1, 2, 2, 2, 1, 1, 2, 2, 1, 1, 2, 1, 2, 1, 2, 2]
myset = set(mylist)
for item in myset:
    print("the %d has found %d" %(item,mylist.count(item)))
# import random
# randomlist=[]
# for i in random(1,101):
#     randomlist.append(i)

# print(randomlist)