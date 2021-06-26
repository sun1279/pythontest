import os
import datetime
import json
import sqlite3


class Bookeeper(object):
    def __init__(self, year):
        self.__year__ = ''
        self.__mon__ = ''
        self.__date__ = ''
        self.__cost__ = ''
        self.__type__ = ''
        self.__subtype__ = ''
        self.__note__ = ''
        self.__conn__ = sqlite3.connect('test.sqlite', check_same_thread=False)
        self.__cur__ = self.__conn__.cursor()
        
        try:
            self.__cur__.execute("SELECT * FROM mybk")
        except:
            self.__cur__.execute("CREATE TABLE mybk(year varchar(4), mon varch(2), cost varchar(10), type varchar(20), subtype varchar(20), note varchar(50), date varchar(10))")

    def getmon(self, year, month):
        CMD_GET_SORTED_MON = 'SELECT * FROM mybk where mon={} ORDER BY date ASC'.format(month)
        self.__cur__.execute(CMD_GET_SORTED_MON)
        row = self.__cur__.fetchall()
        mon_info = list() 
        d = dict() 
        for r in row:
            d['date'] = r[6]
            d['price'] = r[2]
            d['"sel1"'] = r[3]
            d['"sel2"'] = r[4]
            d['"note"'] = r[5]
            mon_info.append(d);
        return mon_info

    def add(self, year, month, input_dict):
        CMD_INSERT='INSERT INTO mybk (year , mon, cost, type, subtype,note, date) VALUES(?,?,?,?,?,?,?)'
        print(input_dict)
        self.__cur__.execute(CMD_INSERT,(year,month,input_dict['price'], input_dict['sel_1st'], input_dict['sel_2nd'], input_dict['note'], input_dict['date']))
        self.__conn__.commit()
        CMD_GET_SORTED_MON = 'SELECT * FROM mybk where mon={} ORDER BY date ASC'.format(month)
        self.__cur__.execute(CMD_GET_SORTED_MON)
        row = self.__cur__.fetchall()
        mon_info = list() 
        d = dict() 
        for r in row:
            d['date'] = r[6]
            d['price'] = r[2]
            d['"sel1"'] = r[3]
            d['"sel2"'] = r[4]
            d['"note"'] = r[5]
            mon_info.append(d);
        return mon_info

    def dele(self, year, month, index):

        CMD_GET_SORTED_MON = 'SELECT * FROM mybk where mon={} AND year= {} ORDER BY date ASC'.format(month, year)
        self.__cur__.execute(CMD_GET_SORTED_MON)
        row = self.__cur__.fetchall()
        CMD_DELETE="DELETE FROM mybk WHERE date='{}' AND cost='{}' AND type='{}' AND subtype='{}' AND note='{}'".format(row[index][6], row[index][2],row[index][3], row[index][4], row[index][5])
        self.__cur__.execute(CMD_DELETE)
        self.__conn__.commit()
        CMD_GET_SORTED_MON = 'SELECT * FROM mybk where mon={} ORDER BY date ASC'.format(month)
        self.__cur__.execute(CMD_GET_SORTED_MON)
        row = self.__cur__.fetchall()
        mon_info = list() 
        d = dict() 
        for r in row:
            d['date'] = r[6]
            d['price'] = r[2]
            d['"sel1"'] = r[3]
            d['"sel2"'] = r[4]
            d['"note"'] = r[5]
            mon_info.append(d);
        return mon_info


    def modify(self, index, input_dict):
        pass

if __name__ == '__main__':
    mybk = Bookeeper(2021)
    a=mybk.add(2021, "05", {'date':'2021-05-12', 'price':'10000000000', 'sel1':'A', 'sel2':'B', 'note':'fff'})
    a=mybk.add(2020, "05", {'date':'2020-05-13', 'price':'10000000000', 'sel1':'A', 'sel2':'B', 'note':'fff'})
    a=mybk.add(2029, "05", {'date':'2029-05-14', 'price':'10000000000', 'sel1':'A', 'sel2':'B', 'note':'fff'})
    a=mybk.add(2010, "05", {'date':'2010-05-15', 'price':'10000000000', 'sel1':'A', 'sel2':'B', 'note':'fff'})
    a=mybk.add(2022, "05", {'date':'2022-05-16', 'price':'10000000000', 'sel1':'A', 'sel2':'B', 'note':'fff'})
    a=mybk.add(2020, "05", {'date':'2020-05-17', 'price':'10000000000', 'sel1':'A', 'sel2':'B', 'note':'fff'})
    a=mybk.add(2020, "05", {'date':'2020-05-18', 'price':'10000000000', 'sel1':'A', 'sel2':'B', 'note':'fff'})
    a=mybk.add(2020, "05", {'date':'2020-05-19', 'price':'10000000000', 'sel1':'A', 'sel2':'B', 'note':'fff'})
    a=mybk.add(2021, "05", {'date':'2021-05-11', 'price':'10000000000', 'sel1':'A', 'sel2':'B', 'note':'fff'})
    a=mybk.getmon(2021,'05')
    print(a)
    a=mybk.dele(2021,'05', 0)
    print(a)

