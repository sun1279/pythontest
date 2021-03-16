import re
import requests

class Youdao(object):
    def __init__(self, word):
        word = word.strip()
        if ' ' in word:
            word = word.replace(' ', '+')
        self.__word__ = word
        URL='http://dict.youdao.com/jsonapi?jsonversion=2&q={word}&keyfrom=deskdict.main&dogVersion=1.0&dogui=json&client=deskdict&id=9b19d285dd7f26ce5&vendor=webdict_default&in=YoudaoDict_webdict_default&appVer=8.9.6.0&appZengqiang=0&abTest=&model=SANGFOR&screen=1920*1080&le=auto&dicts=%7B%22count%22%3A21%2C%22dicts%22%3A%5B%5B%22oxfordAdvance%22%2C%22oxford%22%2C%22splongman%22%2C%22longman%22%2C%22webster%22%2C%22collins%22%2C%22collins_part%22%2C%22ec21%22%2C%22ce_new%22%2C%22hh%22%2C%22newhh%22%2C%22newcenturyjc%22%5D%2C%5B%22web_search%22%5D%2C%5B%22web_trans%22%5D%2C%5B%22special%22%5D%2C%5B%22ee%22%5D%2C%5B%22phrs%22%5D%2C%5B%22syno%22%5D%2C%5B%22rel_word%22%5D%2C%5B%22etym%22%5D%2C%5B%22typos%22%5D%2C%5B%22blng_sents_part%22%2C%22media_sents_part%22%2C%22auth_sents_part%22%5D%2C%5B%22fanyi%22%5D%5D%7D&LTH=47'.format(word=self.__word__)
        r=requests.get(URL)
        self.__wb__=r.json()
        print(self.__wb__)
    #chinese meaning,   list of dict
    def getch(self):
        if 'web_trans' in self.__wb__.keys():
            web_trans=self.__wb__['web_trans']
            wb_t1=web_trans['web-translation']
            ch=list()
            for i in wb_t1[0]['trans']:
                ch.append(i['value'])
            return ch
        else:
            pass

    #list
    def geten(self):
        if 'ee' in self.__wb__.keys():
            ee=self.__wb__['ee']
            ee_src=ee['source']
            ee_word=ee['word']
            ee_word_trs=ee_word['trs']
            en=list()
            for i in ee_word_trs:
                for j in i['tr']:
                    en.append(j['l']['i'])
            return en

    #list of dict
    def getbilng(self):
        bilng = list()
        if 'blng_sents_part' in self.__wb__.keys():
            blng_sents_part=self.__wb__['blng_sents_part']
            for i in blng_sents_part['sentence-pair']:
                d = dict()
                d['en'] = i['sentence']
                d['cn'] = i['sentence-translation']
                bilng.append(d)
            return bilng

    #list of dict
    def getrels(self):
        if 'rel_word' in self.__wb__.keys():
            rel_word=self.__wb__['rel_word']
            rels=list()
            for i in rel_word['rels']:
                d=dict()
                d['pos'] = i['rel']['pos']
                for j in i['rel']['words']:
                    d['en'] = j['word']
                    d['ch'] = j['tran']
                rels.append(d)
            return rels

    #dict
    def getsentence(self):
        if 'auth_sents_part' in self.__wb__.keys():
            auth_sents_part=self.__wb__['auth_sents_part']
            se=list()
            for i in auth_sents_part['sent']:
                s = i['speech'].replace('+',' ')
                s = s.replace("%2C", '')
                se.append(s)
            return se


    #dict
    def getphone(self):
        if 'simple' in self.__wb__.keys():
            simple=self.__wb__['simple']
            phone=dict()
            phone['us']=simple['word'][0]['usphone']
            phone['uk']=simple['word'][0]['ukphone']
            return phone


    #list of dict
    def getphrase(self):
        if 'phrs' in self.__wb__.keys():
            phrs=self.__wb__['phrs']
            phrase=list()
            for i in phrs['phrs']:
                d=dict()
                d['en']=i['phr']['headword']['l']['i']
                d['cn']=i['phr']['trs'][0]['tr']['l']['i']
                phrase.append(d)
            return  phrase

    #list of dict
    def getsyno(self):
        if 'syno' in self.__wb__.keys():
            syno=self.__wb__['syno']
            s= list()
            for i in syno['synos']:
                d=dict()
                l=list()
                d['pos'] = i['syno']['pos']
                for j in (i['syno']['ws']):
                    l.append(j['w'])
                d['syno'] = l
                d['tran'] = i['syno']['tran']
                s.append(d)
            return s

    #list of dict
    def getmedia(self):
        if 'media_sents_part' in self.__wb__.keys():
            media_sents_part=self.__wb__['media_sents_part']
            media = list()
            for m in  media_sents_part['sent']:
                d = dict()
                d['type'] = m['@mediatype']
                d['sent'] = re.sub('<.*?>',' ', m['eng'])
                d['url'] = m['snippets']['snippet'][0]['streamUrl']
                d['name'] = m['snippets']['snippet'][0]['name']
                d['source'] = m['snippets']['snippet'][0]['source']
                media.append(d)
            return media




y=Youdao('ijfasd;')

I=y.getphone()
s='发音：  美音:{}  英音:{}'.format(I['us'], I['uk'])
print(s)


print("中文翻译：")
s=""
I = y.getsyno()
s=''
for i in I:
    s+=i['pos']
    s+=i['tran']
    for j in i['syno']:
        s+=j
    s+='\n'

print(s)



print("双语例句：")
s=''
I=y.getbilng()
for i in I:
    K = i.keys()
    for k in K:
        s+=i[k]
        s+='    '
    s+='\n'
print(s)

print("权威例句：")
s=""
I = y.getsentence()
for  i in I:
    s+=i
    s+='\n'
print(s)
print("同根词：")
s=""
I = y.getrels()
for i in I:
    K = i.keys()
    for k in K:
        s+=i[k]
    s+='\n'
print(s)



print("短语：")
s=""
I = y.getphrase()
l = len(I)
if l > 10:
    l = 10
for i in range(l):
    s+=I[i]['en']
    s+=' '
    s+=I[i]['cn']
    s+='\n'
print(s)

#print("同义词：")
#s=""
#I = y.getsyno()
#s=''
#for i in I:
#    K = i.keys()
#    for k in K:
#        if type(i[k]) is str:
#            s+=i[k]
#            s+=' '
#        if type(i[k]) is list:
#            tmp = i[k]
#            for t in tmp:
#                s+=t
#                s+=' '
#
#print(s)
#print("英文释义：")
#s=""
#I = y.geten()
#for  i in I:
#    s+=i
#    s+='\n'
#print(s)




#print(y.getsyno())
#print(y.getmedia())
