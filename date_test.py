'''
@Author: Never
@Date: 2020-06-18 00:10:40
@Description:
@LastEditTime: 2020-06-24 10:32:17
@LastEditors: Never
'''

class Data_test(object):
    def __init__(self,year=0,mon=0,day=0):
        self.year=year
        self.mon=mon
        self.day=day
    @classmethod
    def get_data(cls,data_as_string):
        year,mon,day=map(int,data_as_string.split('-'))
        date1=cls(year,mon,day)
        return date1

    def out_date(self):
        print('year:',self.year)
        print('month:',self.mon)
        print('day:',self.day)

t=Data_test.get_data('2021-3-11')
t.out_date()


