import os
import datetime
import json


class Bookeeper(object):
    def __init__(self, year):
        self.__json_name__ = "bk_"+str(year)+'.json'
        self.__year__ = dict()
        self.__year_str__ = str(year)
        self.__mon_str__ = ''
        if os.path.exists(self.__json_name__):
            with open(self.__json_name__) as fd:
                self.__year__ = json.load(fd)
        else:#no file exists, what to do
            self.__mon_str__ = str(datetime.date.today())[5:7:]
            self.__mon_list__ = list()
            self.__tmp__ = dict()
            self.__mon_list__.append(self.__tmp__)
            self.__year__[self.__mon_str__] = self.__mon_list__
            with open(self.__json_name__,'w') as fd:
                json.dump(self.__year__, fd)

    def getmon(self, year, month):
        year = str(year)
        self.__mon_str__ = str(month)
        if year == self.__year_str__:
            self.__mon_info__ = list()
            try:
                self.__mon_info__ = self.__year__[str(month)]
            except:
                pass
        else:
            self.__year_str__ = year
            self.__json_name__ = "bk_"+str(year)+'.json'
            with open(self.__json_name__,'r') as fd:
                self.__year__ = json.load(fd)
            self.__mon_info__ = self.__year__[self.__mon_str__]

        return self.__mon_info__

    def add(self, year, month, input_dict):
        self.__mon_info__ = list()
        self.__mon_str__ = input_dict['date'][5:7:]
        year = str(year)
        self.__mon_str__ = str(month)
        if len(input_dict['date']) != 10:
            return

        if year == self.__year_str__:
            pass
        else:
            self.__year_str__ = year
            self.__json_name__ = "bk_"+str(year)+'.json'
            if os.path.exists(self.__json_name__):
                with open(self.__json_name__,'r') as fd:
                    self.__year__ = json.load(fd)
            else:
                self.__mon_str__ = str(datetime.date.today())[5:7:]
                self.__mon_list__ = list()
                self.__tmp__ = dict()
                self.__mon_list__.append(self.__tmp__)
                self.__year__[self.__mon_str__] = self.__mon_list__
                with open(self.__json_name__,'w') as fd:
                    json.dump(self.__year__, fd)

        if self.__mon_str__ in self.__year__.keys():
            self.__mon_info__ = self.__year__[self.__mon_str__]
        else:
            self.__year__[self.__mon_str__]=self.__mon_info__

        self.__mon_info__.append(input_dict)
        while {} in self.__mon_info__:
           self.__mon_info__.remove({})
        self.__mon_info__ = sorted(self.__mon_info__, key=lambda x:x['date'])
        self.__year__[self.__mon_str__] = self.__mon_info__
        with open(self.__json_name__,'w') as fd:
            json.dump(self.__year__, fd)
        return self.__mon_info__

    def dele(self, year, month, index):

        year = str(year)
        self.__mon_str__ = str(month)
        if year == self.__year_str__:
            pass
        else:
            self.__year_str__ = year
            self.__json_name__ = "bk_"+str(year)+'.json'
            with open(self.__json_name__,'r') as fd:
                self.__year__ = json.load(fd)

        self.__mon_info__ = self.__year__[str(month)]
        try:
            self.__mon_info__.pop(int(index))
        except:
            return {'status':'Failed'}
        self.__year__[str(month)] = self.__mon_info__
        with open(self.__json_name__,'w') as fd:
            json.dump(self.__year__, fd)

        return self.__mon_info__

    def modify(self, index, input_dict):
        pass

if __name__ == '__main__':
    mybk = Bookeeper(2021)
    #a=mybk.add(2021, "05", {'date':'2021-05-12', 'price':'10000000000', 'sel1':'A', 'sel2':'B'})
    #a=mybk.add(2020, "05", {'date':'2020-05-13', 'price':'10000000000', 'sel1':'A', 'sel2':'B'})
    #a=mybk.add(2029, "05", {'date':'2029-05-14', 'price':'10000000000', 'sel1':'A', 'sel2':'B'})
    #a=mybk.add(2010, "05", {'date':'2010-05-15', 'price':'10000000000', 'sel1':'A', 'sel2':'B'})
    #a=mybk.add(2022, "05", {'date':'2022-05-16', 'price':'10000000000', 'sel1':'A', 'sel2':'B'})
    #a=mybk.add(2020, "05", {'date':'2020-05-17', 'price':'10000000000', 'sel1':'A', 'sel2':'B'})
    #a=mybk.add(2020, "05", {'date':'2020-05-18', 'price':'10000000000', 'sel1':'A', 'sel2':'B'})
    #a=mybk.add(2020, "05", {'date':'2020-05-19', 'price':'10000000000', 'sel1':'A', 'sel2':'B'})
    #a=mybk.add(2021, "05", {'date':'2021-05-11', 'price':'10000000000', 'sel1':'A', 'sel2':'B'})
    a=mybk.getmon(2021,'05')
    print(a)
    a=mybk.dele(2021,'05', 0)
    print(a)

