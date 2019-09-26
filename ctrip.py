import json
import requests

URL1='https://m.ctrip.com/restapi/flight/html5/swift/getLowestPriceCalendar?'
URL2='https://m.ctrip.com/restapi/soa2/14022/flightListSearch?_fxpcqlniredt=09031046111774300258'

headers = {
    'origin': 'https://m.ctrip.com',
    'content-type': 'application/json',
#    'Referer': 'https://m.ctrip.com/html5/flight/swift/domestic/BJS/SHA/2019-04-15',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}
code_name={'阿勒泰': 'AAT', '阿克苏': 'AKU', '鞍山': 'AOG', '安庆': 'AQG', '安顺': 'AVA', '阿拉善左旗': 'AXF', '澳门': 'MFM', '阿里': 'NGQ', '阿拉善右旗': 'RHT', '阿尔山': 'YIE', '百色': 'AEB', '包头': 'BAV', '毕节': 'BFJ', '北海': 'BHY', '北京': 'BJS', '北京(南苑机场)': 'NAY', '北京(首都国际机场)': 'PEK', '博乐': 'BPL', '保山': 'BSD', '白城': 'DBC', '布尔津': 'KJI', '白山': 'NBS', '巴彦淖尔': 'RLK', '昌都': 'BPX', '承德': 'CDE', '常德': 'CGD', '长春': 'CGQ', '朝阳': 'CHG', '赤峰': 'CIF', '长治': 'CIH', '重庆': 'CKG', '长沙': 'CSX', '成都': 'CTU', '沧源': 'CWJ', '常州': 'CZX', '池州': 'JUH', '潮州': 'SWA', '潮汕': 'SWA', '大同': 'DAT', '达县': 'DAX', '达州': 'DAX', '稻城': 'DCY', '丹东': 'DDG', '迪庆': 'DIG', '大连': 'DLC', '大理': 'DLU', '敦煌': 'DNH', '东营': 'DOY', '大庆': 'DQA', '德令哈': 'HXD', '德宏': 'LUM', '鄂尔多斯': 'DSN', '额济纳旗': 'EJN', '恩施': 'ENH', '二连浩特': 'ERL', '福州': 'FOC', '阜阳': 'FUG', '抚远': 'FYJ', '富蕴': 'FYN', '广州': 'CAN', '果洛': 'GMQ', '格尔木': 'GOQ', '广元': 'GYS', '固原': 'GYU', '高雄': 'KHH', '赣州': 'KOW', '贵阳': 'KWE', '桂林': 'KWL', '红原': 'AHJ', '海口': 'HAK', '河池': 'HCJ', '邯郸': 'HDG', '黑河': 'HEK', '呼和浩特': 'HET', '合肥': 'HFE', '杭州': 'HGH', '淮安': 'HIA', '怀化': 'HJJ', '海拉尔': 'HLD', '哈密': 'HMI', '衡阳': 'HNY', '哈尔滨': 'HRB', '和田': 'HTN', '花土沟': 'HTT', '花莲': 'HUN', '霍林郭勒': 'HUO', '惠阳': 'HUZ', '惠州': 'HUZ', '汉中': 'HZG', '黄山': 'TXN', '呼伦贝尔': 'XRQ', '嘉义': 'CYI', '景德镇': 'JDZ', '加格达奇': 'JGD', '嘉峪关': 'JGN', '井冈山': 'JGS', '景洪': 'JHG', '金昌': 'JIC', '九江': 'JIU', '晋江': 'JJN', '荆门': 'JM1', '佳木斯': 'JMU', '济宁': 'JNG', '锦州': 'JNZ', '建三江': 'JSJ', '鸡西': 'JXA', '九寨沟': 'JZH', '金门': 'KNH', '揭阳': 'SWA', '济南': 'TNA', '库车': 'KCA', '康定': 'KGT', '喀什': 'KHG', '凯里': 'KJH', '昆明': 'KMG', '库尔勒': 'KRL', '克拉玛依': 'KRY', '黎平': 'HZH', '澜沧': 'JMJ', '连城': 'LCX', '龙岩': 'LCX', '临汾': 'LFQ', '兰州': 'LHW', '丽江': 'LJG', '荔波': 'LLB', '吕梁': 'LLV', '临沧': 'LNJ', '陇南': 'LNL', '六盘水': 'LPF', '拉萨': 'LXA', '洛阳': 'LYA', '连云港': 'LYG', '临沂': 'LYI', '柳州': 'LZH', '泸州': 'LZO', '林芝': 'LZY', '芒市': 'LUM', '牡丹江': 'MDG', '马祖': 'MFK', '绵阳': 'MIG', '梅县': 'MXZ', '梅州': 'MXZ', '马公': 'MZG', '满洲里': 'NZH', '漠河': 'OHE', '南昌': 'KHN', '南竿': 'LZN', '南充': 'NAO', '宁波': 'NGB', '南京': 'NKG', '宁蒗': 'NLH', '南宁': 'NNG', '南阳': 'NNY', '南通': 'NTG', '澎湖列岛': 'MZG', '攀枝花': 'PZI', '普洱': 'SYM', '琼海': 'BAR', '秦皇岛': 'BPE', '祁连': 'HBQ', '且末': 'IQM', '庆阳': 'IQN', '黔江': 'JIQ', '泉州': 'JJN', '衢州': 'JUZ', '齐齐哈尔': 'NDG', '青岛': 'TAO', '日照': 'RIZ', '日喀则': 'RKZ', '若羌': 'RQA', '神农架': 'HPG', '石狮': 'JJN', '莎车': 'QSZ', '上海': 'SHA', '上海(浦东国际机场)': 'PVG', '上海(虹桥国际机场)': 'SHA', '沈阳': 'SHE', '石河子': 'SHF', '石家庄': 'SJW', '上饶': 'SQD', '三明': 'SQJ', '汕头': 'SWA', '三亚': 'SYX', '深圳': 'SZX', '十堰': 'WDS', '邵阳': 'WGN', '松原': 'YSQ', '台州': 'HYN', '台中': 'RMQ', '塔城': 'TCG', '腾冲': 'TCZ', '铜仁': 'TEN', '通辽': 'TGO', '天水': 'THQ', '吐鲁番': 'TLQ', '通化': 'TNH', '台南': 'TNN', '台北': 'TPE', '天津': 'TSN', '台东': 'TTT', '唐山': 'TVS', '太原': 'TYN', '泰州': 'YTY', '五大连池': 'DTU', '乌兰浩特': 'HLH', '乌兰察布': 'UCB', '乌鲁木齐': 'URC', '潍坊': 'WEF', '威海': 'WEH', '文山': 'WNH', '温州': 'WNZ', '乌海': 'WUA', '武汉': 'WUH', '武夷山': 'WUS', '无锡': 'WUX', '梧州': 'WUZ', '万州': 'WXN', '乌拉特中旗': 'WZQ', '兴义': 'ACX', '香格里拉': 'DIG', '夏河': 'GXH', '香港': 'HKG', '西双版纳': 'JHG', '新源': 'NLT', '西安': 'SIA', '咸阳': 'SIA', '忻州': 'WUT', '信阳': 'XAI', '襄阳': 'XFN', '西昌': 'XIC', '锡林浩特': 'XIL', '厦门': 'XMN', '西宁': 'XNN', '徐州': 'XUZ', '延安': 'ENY', '银川': 'INC', '伊春': 'LDS', '永州': 'LLF', '榆林': 'UYN', '宜宾': 'YBP', '运城': 'YCU', '宜春': 'YIC', '宜昌': 'YIH', '伊犁': 'YIN', '伊宁': 'YIN', '义乌': 'YIW', '营口': 'YKH', '延吉': 'YNJ', '烟台': 'YNT', '盐城': 'YNZ', '扬州': 'YTY', '玉树': 'YUS', '郑州': 'CGO', '张家界': 'DYG', '芷江': 'HJJ', '舟山': 'HSN', '扎兰屯': 'NZL', '遵义茅台': 'WMT', '张掖': 'YZY', '昭通': 'ZAT', '湛江': 'ZHA', '中卫': 'ZHY', '张家口': 'ZQZ', '珠海': 'ZUH', '遵义': 'ZYI'}


class CFlight(object):
    def __init__(self, dep, arr, date=''):
        self.__dep__ = code_name.get(dep)
        self.__arr__ = code_name.get(arr)
        if not self.__dep__:
            print("Departure city error")
            exit()
        if not self.__arr__:
            print("Arriving city error")
            exit()
        self.__date__ = date

    '''Get the flight list and price a day, this return'''
    def get_day(self):
        p={"preprdid":"","trptpe":1,"flag":8,"searchitem":[{"dccode":self.__dep__,"accode":self.__arr__,"dtime":self.__date__}],"subchannel":'',"tid":"{6d549c74-62d5-42e7-a2cb-35c94d349df4}","head":{"cid":"09031046111774300258","ctok":"","cver":"1.0","lang":"01","sid":"8888","syscode":"09","auth":'',"extension":[{"name":"protocal","value":"https"}]},"contentType":"json"}
        try:
            r=requests.post(URL2, data=json.dumps(p), headers=headers, )
        except:
            print("Error post")
            exit()
        wb=r.json()
        all_flight= wb.get('fltitem')
        return all_flight

    '''Get the Lowest price of every day within three months '''
    def get_month(self):
        p={"stype":1,"dCty":self.__dep__,"aCty":self.__arr__,"flag":'',"start":"","end":"","head":{"cid":"","ctok":"","cver":"1.0","lang":"01","sid":"8888","syscode":"09","auth":'',"extension":[{"name":"aid","value":""},{"name":"sid","value":""},{"name":"protocal","value":"https"}]},"contentType":"json"}
        r=requests.post(URL1, data=json.dumps(p),headers=headers)
        wb=r.json()
        ls=wb['prices']
        return ls


if __name__ == "__main__":
    '''Print lowest price within three months'''
    def PrintPriceList(ls):
        for l in ls:
            print(l.get('airname'),end='  ')
            print(l.get('flightNo').ljust(7),end='  ')
            print(l.get('dDate'),end='   ')
            print(l.get('dweek'),end=' ')
            print(l.get('price'))
    
    
    
    '''Print flight list a day'''
    def PrintPriceByDate(ls):
        print('航班号         出发机场     到达机场        日期        起飞时间      落地时间   最低票价')
        for l in ls:
            print(l.get('mutilstn')[0].get('basinfo').get('flgno').ljust(8), end='     ')
            print(l.get('mutilstn')[0].get('dportinfo').get('cityname'),end='(')
            print(l.get('mutilstn')[0].get('dportinfo').get('aportsname'),end=')    ')
            print(l.get('mutilstn')[0].get('aportinfo').get('cityname'), end='(')
            print(l.get('mutilstn')[0].get('aportinfo').get('aportsname'), end=')    ')
            data=l.get('mutilstn')[0].get('dateinfo').get('ddate')
            print(data.split()[0],end='     ')
            print(data.split()[1],end='     ')
            data=l.get('mutilstn')[0].get('dateinfo').get('adate')
            print(data.split()[1],end='     ')
            print(l.get('policyinfo')[0].get('priceinfo')[0].get('price'))


    f = CFlight('青','上海', '2019-07-01')
    #l=f.get_day()
    l=f.get_month()
    #PrintPriceByDate(l)
    PrintPriceList(l)
