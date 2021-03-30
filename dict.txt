import re
import requests
WORD='confer'
WORD=WORD.strip()
if ' ' in WORD:
    WORD=WORD.replace(' ','+')
URL='http://dict.youdao.com/jsonapi?jsonversion=2&q={word}&keyfrom=deskdict.main&dogVersion=1.0&dogui=json&client=deskdict&id=9b19d285dd7f26ce5&vendor=webdict_default&in=YoudaoDict_webdict_default&appVer=8.9.6.0&appZengqiang=0&abTest=&model=SANGFOR&screen=1920*1080&le=auto&dicts=%7B%22count%22%3A21%2C%22dicts%22%3A%5B%5B%22oxfordAdvance%22%2C%22oxford%22%2C%22splongman%22%2C%22longman%22%2C%22webster%22%2C%22collins%22%2C%22collins_part%22%2C%22ec21%22%2C%22ce_new%22%2C%22hh%22%2C%22newhh%22%2C%22newcenturyjc%22%5D%2C%5B%22web_search%22%5D%2C%5B%22web_trans%22%5D%2C%5B%22special%22%5D%2C%5B%22ee%22%5D%2C%5B%22phrs%22%5D%2C%5B%22syno%22%5D%2C%5B%22rel_word%22%5D%2C%5B%22etym%22%5D%2C%5B%22typos%22%5D%2C%5B%22blng_sents_part%22%2C%22media_sents_part%22%2C%22auth_sents_part%22%5D%2C%5B%22fanyi%22%5D%5D%7D&LTH=47'.format(word=WORD)

r=requests.get(URL)
wb=r.json()

#http://dict.youdao.com/jsonapi?jsonversion=2&q=advocate&keyfrom=deskdict.main&dogVersion=1.0&dogui=json&client=deskdict&id=9b19d285dd7f26ce5&vendor=webdict_default&in=YoudaoDict_webdict_default&appVer=8.9.6.0&appZengqiang=0&abTest=&model=SANGFOR&screen=1920*1080&le=auto&dicts=%7B%22count%22%3A21%2C%22dicts%22%3A%5B%5B%22oxfordAdvance%22%2C%22oxford%22%2C%22splongman%22%2C%22longman%22%2C%22webster%22%2C%22collins%22%2C%22collins_part%22%2C%22ec21%22%2C%22ce_new%22%2C%22hh%22%2C%22newhh%22%2C%22newcenturyjc%22%5D%2C%5B%22web_search%22%5D%2C%5B%22web_trans%22%5D%2C%5B%22special%22%5D%2C%5B%22ee%22%5D%2C%5B%22phrs%22%5D%2C%5B%22syno%22%5D%2C%5B%22rel_word%22%5D%2C%5B%22etym%22%5D%2C%5B%22typos%22%5D%2C%5B%22blng_sents_part%22%2C%22media_sents_part%22%2C%22auth_sents_part%22%5D%2C%5B%22fanyi%22%5D%5D%7D&LTH=47

web_trans_flag = 0
ee_flag = 0
blng_sents_part_flag = 0
rel_word_flag = 0
auth_sents_part_flag = 0
media_sents_part_flag = 0
simple_flag = 0
phrs_flag = 0
oxford_flag = 0
special_flag = 0
syno_flag = 0
input_flag = 0
meta_flag = 0
le_flag = 0
lang_flag = 0

if 'web_trans' in wb.keys():
    web_trans=wb['web_trans']
    web_trans_flag = 1
if 'ee' in wb.keys():
    ee=wb['ee']
    ee_flag = 1
if 'blng_sents_part' in wb.keys():
    blng_sents_part=wb['blng_sents_part']
    blng_sents_part_flag = 1
if 'rel_word' in wb.keys():
    rel_word=wb['rel_word']
    rel_word_flag = 1
if 'auth_sents_part' in wb.keys():
    auth_sents_part=wb['auth_sents_part']
    auth_sents_part_flag = 1
if 'media_sents_part' in wb.keys():
    media_sents_part=wb['media_sents_part']
    media_sents_part_flag = 1
if 'simple' in wb.keys():
    simple=wb['simple']
    simple_flag = 1
#etym=wb['etym']

if 'phrs' in wb.keys():
    phrs=wb['phrs']
    phrs_flag = 1
if 'oxford' in wb.keys():
    oxford=wb['oxford']
    oxford_flag = 1
if 'special' in wb.keys():
    special=wb['special']
    special_flag = 1
if 'syno' in wb.keys():
    syno=wb['syno']
    syno_flag = 1
if 'syno' in wb.keys():
    syno=wb['syno']
    syno_flag = 1
if 'input' in wb.keys():
    input=wb['input']
    input_flag = 1
#collins=wb['collins']
if 'meta' in wb.keys():
    meta=wb['meta']
    meta_flag = 1
if 'le' in wb.keys():
    le=wb['le']
    le_flag = 1
if 'lang' in wb.keys():
    lang=wb['lang']
    lang_flag = 1

#################################################################################
if web_trans_flag == 1:
    print("Translation:----------1")
    wb_t1=web_trans['web-translation']
    for i in wb_t1[0]['trans']:
        print(i['value'], end=' ')
    print('')
    for i in wb_t1:
        print(i['key'], i['trans'][0]['value'])

#################################################################################
if ee_flag == 1:
    print("English meaning:----------2")
    ee_src=ee['source']
    ee_word=ee['word']
    ee_word_trs=ee_word['trs']
    for i in ee_word_trs:
        for j in i['tr']:
            print(j['l']['i'])
'''
for i in ee_word_trs:
    print(i['pos'])
    print(i['tr'][0]['similar-words'])
    for j in i['tr']:
        if 'l' in j.keys():
            print(j['l'])
            print("1------------")
        if 'exam'  in j.keys():
            print(j['exam'])
            print("2------------")
'''


#ee_word_phone=ee_word['phone']
#ee_word_speech=ee_word['speech']
#ee_word_phrase=ee_word['return-phrase']

#################################################################################
if blng_sents_part_flag == 1:
    print("BLNG sentance:----------3")
    blng_sents_part['sentence-pair']
    for i in blng_sents_part['sentence-pair']:
        print(i['sentence'])
        print(i['sentence-translation'])
#################################################################################
if rel_word_flag == 1:
    print("Rels :----------4")
    for i in rel_word['rels']:
        print(i['rel']['pos'], end='   ')
        for j in i['rel']['words']:
        #print(i['rel']['words'])
            print(j['word'])
            print(j['tran'])

##########################################################
if auth_sents_part_flag == 1:
    print("Sentence :----------5")
    for i in auth_sents_part['sent']:
        print(i['speech'].replace('+',' '))
##########################################################
if media_sents_part_flag == 1:
    print("MEdia :----------6")
    for m in  media_sents_part['sent']:
        print(re.sub('<.*?>',' ', m['eng'])) #TODO TODO pattern replace
        #print(m['@mediatype'])
        #print(m['snippets']['snippet'][0]['source'], end=' ')
        #print(m['snippets']['snippet'][0]['name'])
        #print(m['snippets']['snippet'][0]['streamUrl'])

##########################################################
if simple_flag == 1:
    print("Phone :----------7")
    print(simple['word'][0]['usphone'])
    print(simple['word'][0]['ukphone'])
##########################################################
if phrs_flag == 1:
    print("Phrase:----------8")
    for i in phrs['phrs']:
        print(i['phr']['headword']['l']['i'], end=' ')
        print(i['phr']['trs'][0]['tr']['l']['i'])
##########################################################
if syno_flag == 1:
    print("Syno:----------9")
    for i in syno['synos']:
        print(i['syno']['pos'], end=' ')
        for j in (i['syno']['ws']):
            print(j['w'], end=' ')

print('')

