import json
ICAO={'AQG': 'ZSAQ', 'JUH': 'ZSJH', 'FUG': 'ZSFY', 'HFE': 'ZSOF', 'TXN': 'ZSTX', 'PEK': 'ZBAA', 'NAY': 'ZBNY', 'CKG': 'ZUCK', 'JIQ': 'ZUQJ', 'WXN': 'ZUWX', 'FOC': 'ZSFZ', 'LCX': 'ZSLD', 'JJN': 'ZSQZ', 'SQJ': 'ZSSM', 'WUS': 'ZSWY', 'XMN': 'ZSAM', 'DNH': 'ZLDH', 'JGN': 'ZLJQ', 'JIC': 'ZLJC', 'LHW': 'ZLLL', 'LNL': 'ZLLN', 'IQN': 'ZLQY', 'THQ': 'ZLTS', 'GXH': 'ZLXH', 'YZY': 'ZLZY', 'FUO': 'ZGFS', 'CAN': 'ZGGG', 'HUZ': 'ZGHZ', 'MXZ': 'ZGMX', 'SWA': 'ZGOW', 'SZX': 'ZGSZ', 'ZHA': 'ZGZJ', 'ZUH': 'ZGSD', 'AEB': 'ZGBS', 'BHY': 'ZGBH', 'KWL': 'ZGKL', 'HCJ': 'ZGHC', 'LZH': 'ZGZH', 'NNG': 'ZGNN', 'WUZ': 'ZGWZ', 'AVA': 'ZUAS', 'BFJ': 'ZUBJ', 'KWE': 'ZUGY', 'KJH': 'ZUKJ', 'LLB': 'ZULB', 'HZH': 'ZUNP', 'LPF': 'ZUPS', 'TEN': 'ZUTR', 'ACX': 'ZUYI', 'ZYI': 'ZUZY', 'WMT': 'ZUMT', 'HAK': 'ZJHK', 'BAR': 'ZJQH', 'SYX': 'ZJSY', 'XYI': 'ZJYX', 'CDE': 'ZBCD', 'HDG': 'ZBHD', 'BPE': 'ZBDH', 'SJW': 'ZBSJ', 'TVS': 'ZBTS', 'ZQZ': 'ZBZJ', 'DQA': 'ZYDQ', 'FYJ': 'ZYFY', 'HRB': 'ZYHB', 'HEK': 'ZYHE', 'JGD': 'ZYJD', 'JMU': 'ZYJM', 'JSJ': 'ZYJS', 'JXA': 'ZYJX', 'OHE': 'ZYMH', 'MDG': 'ZYMD', 'NDG': 'ZYQQ', 'DTU': 'ZYDU', 'LDS': 'ZYLD', 'LYA': 'ZHLY', 'NNY': 'ZHNY', 'XAI': 'ZHXY', 'CGO': 'ZHCC', 'HKG': 'VHHH', 'ENH': 'ZHES', 'HPG': 'ZHSN', 'WDS': 'ZHSY', 'WUH': 'ZHHH', 'XFN': 'ZHXF', 'YIH': 'ZHYC', 'CGD': 'ZGCD', 'CSX': 'ZGHA', 'HNY': 'ZGHY', 'HJJ': 'ZGCJ', 'WGN': 'ZGSY', 'LLF': 'ZGLG', 'YYA': 'ZGYY', 'DYG': 'ZGDY', 'AXF': 'ZBAL', 'RHT': 'ZBAR', 'YIE': 'ZBES', 'BAV': 'ZBOW', 'RLK': 'ZBYZ', 'CIF': 'ZBCF', 'EJN': 'ZBEN', 'ERL': 'ZBER', 'HLD': 'ZBLA', 'HET': 'ZBHH', 'HUO': 'ZBHZ', 'NZH': 'ZBMZ', 'DSN': 'ZBDS', 'TGO': 'ZBTL', 'HLH': 'ZBUL', 'UCB': 'ZBUC', 'WUA': 'ZBUH', 'XIL': 'ZBXH', 'NZL': 'ZBZL', 'CZX': 'ZSCG', 'HIA': 'ZSSH', 'LYG': 'ZSLG', 'NKG': 'ZSNJ', 'NTG': 'ZSNT', 'WUX': 'ZSWX', 'XUZ': 'ZSXZ', 'YNZ': 'ZSYN', 'YTY': 'ZSYA', 'KOW': 'ZSGZ', 'JGS': 'ZSJA', 'JDZ': 'ZSJD', 'KHN': 'ZSCN', 'SQD': 'ZSSR', 'YIC': 'ZSYC', 'DBC': 'ZYBA', 'NBS': 'ZYBS', 'CGQ': 'ZYCC', 'YSQ': 'ZYSQ', 'TNH': 'ZYTN', 'YNJ': 'ZYYJ', 'AOG': 'ZYAS', 'CNI': 'ZYCH', 'CHG': 'ZYCY', 'DLC': 'ZYTL', 'DDG': 'ZYDD', 'JNZ': 'ZYJZ', 'SHE': 'ZYTX', 'YKH': 'ZYYK', 'MFM': 'VMMC', 'GYU': 'ZLGY', 'INC': 'ZLIC', 'ZHY': 'ZLZW', 'HXD': 'ZLDL', 'GOQ': 'ZLGM', 'GMQ': 'ZLGL', 'HTT': 'ZLHX', 'XNN': 'ZLXN', 'YUS': 'ZLYS', 'AKA': 'ZLAK', 'HZG': 'ZLHZ', 'XIY': 'ZLXY', 'ENY': 'ZLYA', 'UYN': 'ZLYL', 'DOY': 'ZSDY', 'TNA': 'ZSJN', 'JNG': 'ZLJN', 'LYI': 'ZSLY', 'TAO': 'ZSQD', 'RIZ': 'ZSRZ', 'WEF': 'ZSWF', 'WEH': 'ZSWH', 'YNT': 'ZSYT', 'SHA': 'ZSSS', 'PVG': 'ZSPD', 'CIH': 'ZBCZ', 'DAT': 'ZBDT', 'LFQ': 'ZBLF', 'LLV': 'ZBLL', 'TYN': 'ZBYN', 'WUT': 'ZBXZ', 'YCU': 'ZBYC', 'BZX': 'ZUBZ', 'CTU': 'ZUUU', 'DCY': 'ZUDC', 'DAX': 'ZUDX', 'GYS': 'ZUGU', 'AHJ': 'ZUHY', 'JZH': 'ZUJZ', 'KGT': 'ZUKD', 'LZO': 'ZULZ', 'MIG': 'ZUMY', 'NAO': 'ZUNC', 'PZI': 'ZUZH', 'XIC': 'ZUXC', 'YBP': 'ZUYB', 'TSN': 'ZBTJ', 'LXA': 'ZULS', 'LZY': 'ZUNZ', 'BPX': 'ZUBD', 'RKZ': 'ZURK', 'NGQ': 'ZUAL', 'AKU': 'ZWAK', 'AAT': 'ZWAT', 'BPL': 'ZWBL', 'KJI': 'ZWKN', 'FYN': 'ZWFY', 'HMI': 'ZWHM', 'HTN': 'ZWTN', 'KRL': 'ZWKL', 'KCA': 'ZWKC', 'KRY': 'ZWKM', 'KHG': 'ZWSH', 'IQM': 'ZWCM', 'RQA': 'ZWRQ', 'SHF': 'ZWHZ', 'TCG': 'ZWTC', 'TLQ': 'ZWTP', 'URC': 'ZWWW', 'NLT': 'ZWNL', 'QSZ': 'ZWSC', 'YIN': 'ZWYN', 'BSD': 'ZPBS', 'CWJ': 'ZPCW', 'DLU': 'ZPDL', 'JHG': 'ZPJH', 'KMG': 'ZPPP', 'JMJ': 'ZPJM', 'LJG': 'ZPLJ', 'LNJ': 'ZPLC', 'LUM': 'ZPLX', 'NLH': 'ZPNL', 'SYM': 'ZPSM', 'DIG': 'ZPDQ', 'TCZ': 'ZPTC', 'WNH': 'ZPWS', 'ZAT': 'ZPZT', 'HGH': 'ZSHC', 'NGB': 'ZSNB', 'JUZ': 'ZSJU', 'HYN': 'ZSLQ', 'WNZ': 'ZSWZ', 'YIW': 'ZSYW', 'HSN': 'ZSZS', 'JIU': 'ZSJJ', 'SHP': 'ZBSH'}

cities=[{"airport":"首都","city":"北京","enAirport":"","match":"北京 首都|beijingshoudu|PEK","pinyin":"beijingshoudu","tcode":"PEK"},{"airport":"虹桥","city":"上海","enAirport":"","match":"上海 虹桥|shanghaihongqiao|SHA","pinyin":"shanghaihongqiao","tcode":"SHA"},{"airport":"浦东","city":"上海","enAirport":"","match":"上海 浦东|shanghaipudong|PVG","pinyin":"shanghaipudong","tcode":"PVG"},{"airport":"白云","city":"广州","enAirport":"","match":"广州 白云|guangzhoubaiyun|CAN","pinyin":"guangzhoubaiyun","tcode":"CAN"},{"airport":"宝安","city":"深圳","enAirport":"","match":"深圳 宝安|shenzhenbaoan|SZX","pinyin":"shenzhenbaoan","tcode":"SZX"},{"airport":"双流","city":"成都","enAirport":"","match":"成都 双流|chengdushuangliu|CTU","pinyin":"chengdushuangliu","tcode":"CTU"},{"airport":"长水","city":"昆明","enAirport":"","match":"昆明 长水|kunmingchangshui|KMG","pinyin":"kunmingchangshui","tcode":"KMG"},{"airport":"咸阳","city":"西安","enAirport":"","match":"西安 咸阳|xianxianyang|XIY","pinyin":"xianxianyang","tcode":"XIY"},{"airport":"萧山","city":"杭州","enAirport":"","match":"杭州 萧山|hangzhouxiaoshan|HGH","pinyin":"hangzhouxiaoshan","tcode":"HGH"},{"airport":"江北","city":"重庆","enAirport":"","match":"重庆 江北|chongqingjiangbei|CKG","pinyin":"chongqingjiangbei","tcode":"CKG"},{"airport":"南苑","city":"北京","enAirport":"","match":"北京 南苑|beijingnanyuan|NAY","pinyin":"beijingnanyuan","tcode":"NAY"},{"airport":"曲阜","city":"济宁","enAirport":"","match":"济宁 曲阜|jiningqufu|JNG","pinyin":"jiningqufu","tcode":"JNG"},{"airport":"衢州","city":"衢州","enAirport":"","match":"衢州 衢州|quzhou|JUZ","pinyin":"quzhou","tcode":"JUZ"},{"airport":"库车","city":"库车","enAirport":"","match":"库车 库车|kuche|KCA","pinyin":"kuche","tcode":"KCA"},{"airport":"龙洞堡","city":"贵阳","enAirport":"","match":"贵阳 龙洞堡|guiyanglongdongbao|KWE","pinyin":"guiyanglongdongbao","tcode":"KWE"},{"airport":"中川","city":"兰州","enAirport":"","match":"兰州 中川|lanzhouzhongchuan|LHW","pinyin":"lanzhouzhongchuan","tcode":"LHW"},{"airport":"三义","city":"丽江","enAirport":"","match":"丽江 三义|lijiangsanyi|LJG","pinyin":"lijiangsanyi","tcode":"LJG"},{"airport":"贡嘎","city":"拉萨","enAirport":"","match":"拉萨 贡嘎|lasagongga|LXA","pinyin":"lasagongga","tcode":"LXA"},{"airport":"北郊","city":"洛阳","enAirport":"","match":"洛阳 北郊|luoyangbeijiao|LYA","pinyin":"luoyangbeijiao","tcode":"LYA"},{"airport":"沭埠岭","city":"临沂","enAirport":"","match":"临沂 沭埠岭|linyishubuling|LYI","pinyin":"linyishubuling","tcode":"LYI"},{"airport":"白莲","city":"柳州","enAirport":"","match":"柳州 白莲|liuzhoubailian|LZH","pinyin":"liuzhoubailian","tcode":"LZH"},{"airport":"禄口","city":"南京","enAirport":"","match":"南京 禄口|nanjinglukou|NKG","pinyin":"nanjinglukou","tcode":"NKG"},{"airport":"兴东","city":"南通","enAirport":"","match":"南通 兴东|nantongxingdong|NTG","pinyin":"nantongxingdong","tcode":"NTG"},{"airport":"萨尔图","city":"大庆","enAirport":"","match":"大庆 萨尔图|daqingsaertu|DQA","pinyin":"daqingsaertu","tcode":"DQA"},{"airport":"田阳","city":"百色","enAirport":"","match":"百色 田阳|baisetianyang|AEB","pinyin":"baisetianyang","tcode":"AEB"},{"airport":"阿拉山口","city":"博乐","enAirport":"","match":"博乐 阿拉山口|bolealashankou|BPL","pinyin":"bolealashankou","tcode":"BPL"},{"airport":"赛乌苏","city":"二连浩特","enAirport":"","match":"二连浩特 赛乌苏|erlianhaote|ERL","pinyin":"erlianhaote","tcode":"ERL"},{"airport":"盘龙","city":"广元","enAirport":"","match":"广元 盘龙|guangyuanpanlong|GYS","pinyin":"guangyuanpanlong","tcode":"GYS"},{"airport":"六盘山","city":"固原","enAirport":"","match":"固原 六盘山|guyuanliupanshan|GYU","pinyin":"guyuanliupanshan","tcode":"GYU"},{"airport":"黎平","city":"黎平","enAirport":"","match":"黎平 黎平|liping|HZH","pinyin":"liping","tcode":"HZH"},{"airport":"舟白","city":"黔江","enAirport":"","match":"黔江 舟白|qianjiangzhoubai|JIQ","pinyin":"qianjiangzhoubai","tcode":"JIQ"},{"airport":"康定","city":"甘孜","enAirport":"","match":"甘孜 康定|ganzikangding|KGT","pinyin":"ganzikangding","tcode":"KGT"},{"airport":"喀纳斯","city":"布尔津","enAirport":"","match":"布尔津 喀纳斯|buerjinkanasi|KJI","pinyin":"buerjinkanasi","tcode":"KJI"},{"airport":"林都","city":"伊春","enAirport":"","match":"伊春 林都|yichunlindu|LDS","pinyin":"yichunlindu","tcode":"LDS"},{"airport":"荔波","city":"黔南州","enAirport":"","match":"黔南州 荔波|qiannanzhoulipo|LLB","pinyin":"qiannanzhoulipo","tcode":"LLB"},{"airport":"长白山","city":"白山","enAirport":"","match":"白山 长白山|baishanchangbaishan|NBS","pinyin":"baishanchangbaishan","tcode":"NBS"},{"airport":"昆莎","city":"阿里","enAirport":"","match":"阿里 昆莎|alikunsha|NGQ","pinyin":"alikunsha","tcode":"NGQ"},{"airport":"许家坪","city":"恩施","enAirport":"","match":"恩施 许家坪|enshixujiaping|ENH","pinyin":"enshixujiaping","tcode":"ENH"},{"airport":"鄂尔多斯","city":"鄂尔多斯","enAirport":"","match":"鄂尔多斯 鄂尔多斯|eerduosi|DSN","pinyin":"eerduosi","tcode":"DSN"},{"airport":"普陀山","city":"舟山","enAirport":"","match":"舟山 普陀山|zhoushanputuoshan|HSN","pinyin":"zhoushanputuoshan","tcode":"HSN"},{"airport":"关公","city":"运城","enAirport":"","match":"运城 关公|yunchengzhangxiao|YCU","pinyin":"yunchengzhangxiao","tcode":"YCU"},{"airport":"地窝堡","city":"乌鲁木齐","enAirport":"","match":"乌鲁木齐 地窝堡|wulumuqidiwobao|URC","pinyin":"wulumuqidiwobao","tcode":"URC"},{"airport":"黄花","city":"长沙","enAirport":"","match":"长沙 黄花|changshahuanghuo|CSX","pinyin":"changshahuanghuo","tcode":"CSX"},{"airport":"金川","city":"金昌","enAirport":"","match":"金昌 金川|jinzhou|JIC","pinyin":"jinzhou","tcode":"JIC"},{"airport":"西郊","city":"满洲里","enAirport":"","match":"满洲里 西郊|manzhoulixijiao|NZH","pinyin":"manzhoulixijiao","tcode":"NZH"},{"airport":"驼峰","city":"腾冲","enAirport":"","match":"腾冲 驼峰|tengchongtuofeng|TCZ","pinyin":"tengchongtuofeng","tcode":"TCZ"},{"airport":"邯郸","city":"邯郸","enAirport":"","match":"邯郸 邯郸|handan|HDG","pinyin":"handan","tcode":"HDG"},{"airport":"白塔","city":"呼和浩特","enAirport":"","match":"呼和浩特 白塔|huhehaote|HET","pinyin":"huhehaote","tcode":"HET"},{"airport":"新桥","city":"合肥","enAirport":"","match":"合肥 新桥|hefeiluogang|HFE","pinyin":"hefeiluogang","tcode":"HFE"},{"airport":"东山","city":"海拉尔","enAirport":"","match":"海拉尔 东山|hailaerdongshang|HLD","pinyin":"hailaerdongshang","tcode":"HLD"},{"airport":"哈密","city":"哈密","enAirport":"","match":"哈密 哈密|hami|HMI","pinyin":"hami","tcode":"HMI"},{"airport":"霍坦","city":"和田","enAirport":"","match":"和田 霍坦|hetianhuodan|HTN","pinyin":"hetianhuodan","tcode":"HTN"},{"airport":"路桥","city":"台州","enAirport":"","match":"台州 路桥|taizhouluqiao|HYN","pinyin":"taizhouluqiao","tcode":"HYN"},{"airport":"且末","city":"且末","enAirport":"","match":"且末 且末|qiemo|IQM","pinyin":"qiemo","tcode":"IQM"},{"airport":"庆阳","city":"庆阳","enAirport":"","match":"庆阳 庆阳|qingyang|IQN","pinyin":"qingyang","tcode":"IQN"},{"airport":"罗家","city":"景德镇","enAirport":"","match":"景德镇 罗家|jingdezhenluojia|JDZ","pinyin":"jingdezhenluojia","tcode":"JDZ"},{"airport":"西双版纳","city":"景洪","enAirport":"","match":"景洪 西双版纳|jinghong|JHG","pinyin":"jinghong","tcode":"JHG"},{"airport":"晋江","city":"泉州","enAirport":"","match":"泉州 晋江|quanzhoujinjiang|JJN","pinyin":"quanzhoujinjiang","tcode":"JJN"},{"airport":"小岭子","city":"锦州","enAirport":"","match":"锦州 小岭子|jinzhouxiaolingzi|JNZ","pinyin":"jinzhouxiaolingzi","tcode":"JNZ"},{"airport":"昌北","city":"南昌","enAirport":"","match":"南昌 昌北|nanchangchangbei|KHN","pinyin":"nanchangchangbei","tcode":"KHN"},{"airport":"克拉玛依","city":"克拉玛依","enAirport":"","match":"克拉玛依 克拉玛依|kalamayi|KRY","pinyin":"kalamayi","tcode":"KRY"},{"airport":"两江","city":"桂林","enAirport":"","match":"桂林 两江|guilinliangjiang|KWL","pinyin":"guilinliangjiang","tcode":"KWL"},{"airport":"芒市","city":"德宏","enAirport":"","match":"德宏 芒市|dehongmangshi|LUM","pinyin":"dehongmangshi","tcode":"LUM"},{"airport":"蓝田","city":"泸州","enAirport":"","match":"泸州 蓝田|luzhouliantian|LZO","pinyin":"luzhouliantian","tcode":"LZO"},{"airport":"海浪 ","city":"牡丹江","enAirport":"","match":"牡丹江 海浪 |mudanjianghailang|MDG","pinyin":"mudanjianghailang","tcode":"MDG"},{"airport":"长岗岌","city":"梅县","enAirport":"","match":"梅县 长岗岌|meixianchanggangji|MXZ","pinyin":"meixianchanggangji","tcode":"MXZ"},{"airport":"三家子","city":"齐齐哈尔","enAirport":"","match":"齐齐哈尔 三家子|qiqihaersanjiazi|NDG","pinyin":"qiqihaersanjiazi","tcode":"NDG"},{"airport":"古莲 ","city":"漠河","enAirport":"","match":"漠河 古莲 |mohegulian|OHE","pinyin":"mohegulian","tcode":"OHE"},{"airport":"正定","city":"石家庄","enAirport":"","match":"石家庄 正定|shijiazhuangzhengding|SJW","pinyin":"shijiazhuangzhengding","tcode":"SJW"},{"airport":"思茅","city":"普洱","enAirport":"","match":"普洱 思茅|puersimao|SYM","pinyin":"puersimao","tcode":"SYM"},{"airport":"通辽","city":"通辽","enAirport":"","match":"通辽 通辽|tongliao|TGO","pinyin":"tongliao","tcode":"TGO"},{"airport":"大水泊","city":"威海","enAirport":"","match":"威海 大水泊|weihaidashuipo|WEH","pinyin":"weihaidashuipo","tcode":"WEH"},{"airport":"苏南硕放","city":"无锡","enAirport":"","match":"无锡 苏南硕放|wuxisunanshuofang|WUX","pinyin":"wuxisunanshuofang","tcode":"WUX"},{"airport":"襄阳","city":"襄阳","enAirport":"","match":"襄阳 襄阳|xiangyangjichang|XFN","pinyin":"xiangyangjichang","tcode":"XFN"},{"airport":"观音","city":"徐州","enAirport":"","match":"徐州 观音|xuzhouguanyin|XUZ","pinyin":"xuzhouguanyin","tcode":"XUZ"},{"airport":"朝阳川","city":"延吉","enAirport":"","match":"延吉 朝阳川|yanjichaoyangchuan|YNJ","pinyin":"yanjichaoyangchuan","tcode":"YNJ"},{"airport":"湛江","city":"湛江","enAirport":"","match":"湛江 湛江|zhanjiang|ZHA","pinyin":"zhanjiang","tcode":"ZHA"},{"airport":"新舟","city":"遵义","enAirport":"","match":"遵义 新舟|zunyixinzhou|ZYI","pinyin":"zunyixinzhou","tcode":"ZYI"},{"airport":"三峡","city":"宜昌","enAirport":"","match":"宜昌 三峡|yichangsanxia|YIH","pinyin":"yichangsanxia","tcode":"YIH"},{"airport":"莱山","city":"烟台","enAirport":"","match":"烟台 莱山|yantailaishan|YNT","pinyin":"yantailaishan","tcode":"YNT"},{"airport":"王村","city":"长治","enAirport":"","match":"长治 王村|changzhiwangcun|CIH","pinyin":"changzhiwangcun","tcode":"CIH"},{"airport":"河市","city":"达州","enAirport":"","match":"达州 河市|dazhouheshi|DAX","pinyin":"dazhouheshi","tcode":"DAX"},{"airport":"美兰","city":"海口","enAirport":"","match":"海口 美兰|haikoumeilan|HAK","pinyin":"haikoumeilan","tcode":"HAK"},{"airport":"黄龙","city":"九寨沟","enAirport":"","match":"九寨沟 黄龙|jiuzhaihuanglong|JZH","pinyin":"jiuzhaihuanglong","tcode":"JZH"},{"airport":"南郊","city":"绵阳","enAirport":"","match":"绵阳 南郊|mianyangnanjiao|MIG","pinyin":"mianyangnanjiao","tcode":"MIG"},{"airport":"龙嘉","city":"长春","enAirport":"","match":"长春 龙嘉|changchunlongjia|CGQ","pinyin":"changchunlongjia","tcode":"CGQ"},{"airport":"玉龙","city":"赤峰","enAirport":"","match":"赤峰 玉龙|chifengyulong|CIF","pinyin":"chifengyulong","tcode":"CIF"},{"airport":"大长山岛","city":"长海","enAirport":"","match":"长海 大长山岛|changhaidachangdao|CNI","pinyin":"changhaidachangdao","tcode":"CNI"},{"airport":"奔牛","city":"常州","enAirport":"","match":"常州 奔牛|changzhoubenniu|CZX","pinyin":"changzhoubenniu","tcode":"CZX"},{"airport":"倍加皂","city":"大同","enAirport":"","match":"大同 倍加皂|datongbeijiazao|DAT","pinyin":"datongbeijiazao","tcode":"DAT"},{"airport":"浪头","city":"丹东","enAirport":"","match":"丹东 浪头|dandonglangtou|DDG","pinyin":"dandonglangtou","tcode":"DDG"},{"airport":"香格里拉","city":"迪庆","enAirport":"","match":"迪庆 香格里拉|diqingxianggelila|DIG","pinyin":"diqingxianggelila","tcode":"DIG"},{"airport":"周水子","city":"大连","enAirport":"","match":"大连 周水子|dalianzhoushuizi|DLC","pinyin":"dalianzhoushuizi","tcode":"DLC"},{"airport":"敦煌","city":"敦煌","enAirport":"","match":"敦煌 敦煌|dunhuang|DNH","pinyin":"dunhuang","tcode":"DNH"},{"airport":"东营","city":"东营","enAirport":"","match":"东营 东营|dongying|DOY","pinyin":"dongying","tcode":"DOY"},{"airport":"荷花","city":"张家界","enAirport":"","match":"张家界 荷花|zhangjiajiehehua|DYG","pinyin":"zhangjiajiehehua","tcode":"DYG"},{"airport":"二十里堡","city":"延安","enAirport":"","match":"延安 二十里堡|yananershilibao|ENY","pinyin":"yananershilibao","tcode":"ENY"},{"airport":"佛山","city":"佛山","enAirport":"","match":"佛山 佛山|foshan|FUO","pinyin":"foshan","tcode":"FUO"},{"airport":"加格达奇","city":"加格达奇","enAirport":"","match":"加格达奇 加格达奇|jiagedaqi|JGD","pinyin":"jiagedaqi","tcode":"JGD"},{"airport":"和平","city":"日喀则","enAirport":"","match":"日喀则 和平|rikezeheping|RKZ","pinyin":"rikezeheping","tcode":"RKZ"},{"airport":"天吉泰","city":"巴彦淖尔","enAirport":"","match":"巴彦淖尔 天吉泰|bayannaoertianjitai|RLK","pinyin":"bayannaoertianjitai","tcode":"RLK"},{"airport":"伊尔施","city":"阿尔山","enAirport":"","match":"阿尔山 伊尔施|aershanyiershi|YIE","pinyin":"aershanyiershi","tcode":"YIE"},{"airport":"张掖","city":"张掖","enAirport":"","match":"张掖 张掖|zhangye|YZY","pinyin":"zhangye","tcode":"YZY"},{"airport":"曹家堡","city":"西宁","enAirport":"","match":"西宁 曹家堡|xiningcaojiabao|XNN","pinyin":"xiningcaojiabao","tcode":"XNN"},{"airport":"菜坝","city":"宜宾","enAirport":"","match":"宜宾 菜坝|yibincaiba|YBP","pinyin":"yibincaiba","tcode":"YBP"},{"airport":"保山云端","city":"保山","enAirport":"","match":"保山 保山云端|baoshanyunduan|BSD","pinyin":"baoshanyunduan","tcode":"BSD"},{"airport":"河东","city":"银川","enAirport":"","match":"银川 河东|yinchuan|INC","pinyin":"yinchuan","tcode":"INC"},{"airport":"桃仙","city":"沈阳","enAirport":"","match":"沈阳 桃仙|shenyangtaoxian|SHE","pinyin":"shenyangtaoxian","tcode":"SHE"},{"airport":"西关","city":"阜阳","enAirport":"","match":"阜阳 西关|fuyangxiguan|FUG","pinyin":"fuyangxiguan","tcode":"FUG"},{"airport":"涟水","city":"淮安","enAirport":"","match":"淮安 涟水|huaianlianshui|HIA","pinyin":"huaianlianshui","tcode":"HIA"},{"airport":"兴凯湖","city":"鸡西","enAirport":"","match":"鸡西 兴凯湖|jixixingkaihu|JXA","pinyin":"jixixingkaihu","tcode":"JXA"},{"airport":"冠豸山","city":"连城","enAirport":"","match":"连城 冠豸山|lianchengguanzhishan|LCX","pinyin":"lianchengguanzhishan","tcode":"LCX"},{"airport":"米林","city":"林芝","enAirport":"","match":"林芝 米林|linzhimilin|LZY","pinyin":"linzhimilin","tcode":"LZY"},{"airport":"那拉提","city":"那拉提","enAirport":"","match":"那拉提 那拉提|nalati|NLT","pinyin":"nalati","tcode":"NLT"},{"airport":"榆阳","city":"榆林","enAirport":"","match":"榆林 榆阳|yulinyuyang|UYN","pinyin":"yulinyuyang","tcode":"UYN"},{"airport":"滨海","city":"天津","enAirport":"","match":"天津 滨海|tianjinbinhai|TSN","pinyin":"tianjinbinhai","tcode":"TSN"},{"airport":"泰州","city":"扬州","enAirport":"","match":"扬州 泰州|yangzhoutaizhou|YTY","pinyin":"yangzhoutaizhou","tcode":"YTY"},{"airport":"喀什","city":"喀什","enAirport":"","match":"喀什 喀什|keshi|KHG","pinyin":"keshi","tcode":"KHG"},{"airport":"高坪","city":"南充","enAirport":"","match":"南充 高坪|naochonggaoping|NAO","pinyin":"naochonggaoping","tcode":"NAO"},{"airport":"流亭","city":"青岛","enAirport":"","match":"青岛 流亭|qingdaoliuting|TAO","pinyin":"qingdaoliuting","tcode":"TAO"},{"airport":"龙湾","city":"温州","enAirport":"","match":"温州 龙湾|wenzhouyongqiang|WNZ","pinyin":"wenzhouyongqiang","tcode":"WNZ"},{"airport":"昭通","city":"昭通","enAirport":"","match":"昭通 昭通|zhaotong|ZAT","pinyin":"zhaotong","tcode":"ZAT"},{"airport":"阿勒泰","city":"阿勒泰","enAirport":"","match":"阿勒泰 阿勒泰|aletai|AAT","pinyin":"aletai","tcode":"AAT"},{"airport":"临沧","city":"临沧","enAirport":"","match":"临沧 临沧|lincang|LNJ","pinyin":"lincang","tcode":"LNJ"},{"airport":"桃花源","city":"常德","enAirport":"","match":"常德 桃花源|changdetaohuayuan|CGD","pinyin":"changdetaohuayuan","tcode":"CGD"},{"airport":"吴圩 ","city":"南宁","enAirport":"","match":"南宁 吴圩 |nanningwuxu|NNG","pinyin":"nanningwuxu","tcode":"NNG"},{"airport":"库尔勒","city":"库尔勒","enAirport":"","match":"库尔勒 库尔勒|kuerle|KRL","pinyin":"kuerle","tcode":"KRL"},{"airport":"安庆","city":"安庆","enAirport":"","match":"安庆 安庆|anqing|AQG","pinyin":"anqing","tcode":"AQG"},{"airport":"塔城","city":"塔城","enAirport":"","match":"塔城 塔城|tacheng|TCG","pinyin":"tacheng","tcode":"TCG"},{"airport":"天河","city":"武汉","enAirport":"","match":"武汉 天河|wuhantianhe|WUH","pinyin":"wuhantianhe","tcode":"WUH"},{"airport":"青山","city":"西昌","enAirport":"","match":"西昌 青山|xichangqingshan|XIC","pinyin":"xichangqingshan","tcode":"XIC"},{"airport":"南洋","city":"盐城","enAirport":"","match":"盐城 南洋|yanchengnanyang|YNZ","pinyin":"yanchengnanyang","tcode":"YNZ"},{"airport":"长乐","city":"福州","enAirport":"","match":"福州 长乐|fuzhouchangle|FOC","pinyin":"fuzhouchangle","tcode":"FOC"},{"airport":"格尔木","city":"格尔木","enAirport":"","match":"格尔木 格尔木|geermu|GOQ","pinyin":"geermu","tcode":"GOQ"},{"airport":"黑河","city":"黑河","enAirport":"","match":"黑河 黑河|heihe|HEK","pinyin":"heihe","tcode":"HEK"},{"airport":"芷江","city":"怀化","enAirport":"","match":"怀化 芷江|huahuazhijiang|HJJ","pinyin":"huahuazhijiang","tcode":"HJJ"},{"airport":"乌兰浩特","city":"乌兰浩特","enAirport":"","match":"乌兰浩特 乌兰浩特|wulanhaote|HLH","pinyin":"wulanhaote","tcode":"HLH"},{"airport":"太平","city":"哈尔滨","enAirport":"","match":"哈尔滨 太平|haerbintaiping|HRB","pinyin":"haerbintaiping","tcode":"HRB"},{"airport":"西关","city":"汉中","enAirport":"","match":"汉中 西关|hanzhongxiguan|HZG","pinyin":"hanzhongxiguan","tcode":"HZG"},{"airport":"井冈山","city":"井冈山","enAirport":"","match":"井冈山 井冈山|jinggangshan|JGS","pinyin":"jinggangshan","tcode":"JGS"},{"airport":"庐山","city":"九江","enAirport":"","match":"九江 庐山|jiujianglushan|JIU","pinyin":"jiujianglushan","tcode":"JIU"},{"airport":"麦积山","city":"天水","enAirport":"","match":"天水 麦积山|tianshuimaijishan|THQ","pinyin":"tianshuimaijishan","tcode":"THQ"},{"airport":"交河","city":"吐鲁番","enAirport":"","match":"吐鲁番 交河|tulufanjiaohe|TLQ","pinyin":"tulufanjiaohe","tcode":"TLQ"},{"airport":"三女河","city":"唐山","enAirport":"","match":"唐山 三女河|tangshansannvhe|TVS","pinyin":"tangshansannvhe","tcode":"TVS"},{"airport":"巴塘","city":"玉树","enAirport":"","match":"玉树 巴塘|yushubatang|YUS","pinyin":"yushubatang","tcode":"YUS"},{"airport":"香山","city":"中卫","enAirport":"","match":"中卫 香山|zhongweixiangshan|ZHY","pinyin":"zhongweixiangshan","tcode":"ZHY"},{"airport":"普者黑","city":"文山","enAirport":"","match":"文山 普者黑|wenshanpuzhehei|WNH","pinyin":"wenshanpuzhehei","tcode":"WNH"},{"airport":"宝安营","city":"攀枝花","enAirport":"","match":"攀枝花 宝安营|panzhihuobaoanying|PZI","pinyin":"panzhihuobaoanying","tcode":"PZI"},{"airport":"山海关","city":"秦皇岛","enAirport":"","match":"秦皇岛 山海关|qinhuangdaohaiguan|SHP","pinyin":"qinhuangdaohaiguan","tcode":"SHP"},{"airport":"凤凰","city":"三亚","enAirport":"","match":"三亚 凤凰|sanyafenghuang|SYX","pinyin":"sanyafenghuang","tcode":"SYX"},{"airport":"凤凰","city":"铜仁","enAirport":"","match":"铜仁 凤凰|tongrenfenghuang|TEN","pinyin":"tongrenfenghuang","tcode":"TEN"},{"airport":"遥墙","city":"济南","enAirport":"","match":"济南 遥墙|jinanyaoqiang|TNA","pinyin":"jinanyaoqiang","tcode":"TNA"},{"airport":"屯溪","city":"黄山","enAirport":"","match":"黄山 屯溪|huangshantunxi|TXN","pinyin":"huangshantunxi","tcode":"TXN"},{"airport":"乌海","city":"乌海","enAirport":"","match":"乌海 乌海|wuhai|WUA","pinyin":"wuhai","tcode":"WUA"},{"airport":"武夷山","city":"武夷山","enAirport":"","match":"武夷山 武夷山|wuyishan|WUS","pinyin":"wuyishan","tcode":"WUS"},{"airport":"长州岛","city":"梧州","enAirport":"","match":"梧州 长州岛|wuzhouchangzhoudao|WUZ","pinyin":"wuzhouchangzhoudao","tcode":"WUZ"},{"airport":"锡林浩特","city":"锡林浩特","enAirport":"","match":"锡林浩特 锡林浩特|xilinhaote|XIL","pinyin":"xilinhaote","tcode":"XIL"},{"airport":"兴义","city":"兴义","enAirport":"","match":"兴义 兴义|xingyi|ACX","pinyin":"xingyi","tcode":"ACX"},{"airport":"安康","city":"安康","enAirport":"","match":"安康 安康|ankang|AKA","pinyin":"ankang","tcode":"AKA"},{"airport":"阿克苏","city":"阿克苏","enAirport":"","match":"阿克苏 阿克苏|akesu|AKU","pinyin":"akesu","tcode":"AKU"},{"airport":"腾鳌","city":"鞍山","enAirport":"","match":"鞍山 腾鳌|anshantengao|AOG","pinyin":"anshantengao","tcode":"AOG"},{"airport":"黄果树","city":"安顺","enAirport":"","match":"安顺 黄果树|anshunhuangguoshu|AVA","pinyin":"anshunhuangguoshu","tcode":"AVA"},{"airport":"二里半","city":"包头","enAirport":"","match":"包头 二里半|baotouerliban|BAV","pinyin":"baotouerliban","tcode":"BAV"},{"airport":"福成","city":"北海","enAirport":"","match":"北海 福成|beihaifucheng|BHY","pinyin":"beihaifucheng","tcode":"BHY"},{"airport":"昌都邦达","city":"昌都","enAirport":"","match":"昌都 昌都邦达|changdubangda|BPX","pinyin":"changdubangda","tcode":"BPX"},{"airport":"东郊","city":"佳木斯","enAirport":"","match":"佳木斯 东郊|jiamusidongjiao|JMU","pinyin":"jiamusidongjiao","tcode":"JMU"},{"airport":"黄金","city":"赣州","enAirport":"","match":"赣州 黄金|ganzhouhuangjin|KOW","pinyin":"ganzhouhuangjin","tcode":"KOW"},{"airport":"零陵","city":"永州","enAirport":"","match":"永州 零陵|yongzhoulingling|LLF","pinyin":"yongzhoulingling","tcode":"LLF"},{"airport":"白塔埠","city":"连云港","enAirport":"","match":"连云港 白塔埠|lianyungangbaita|LYG","pinyin":"lianyungangbaita","tcode":"LYG"},{"airport":"姜营","city":"南阳","enAirport":"","match":"南阳 姜营|nanyangjiangying|NNY","pinyin":"nanyangjiangying","tcode":"NNY"},{"airport":"揭阳潮汕","city":"汕头","enAirport":"","match":"汕头 揭阳潮汕|jieyangchaoshan|SWA","pinyin":"jieyangchaoshan","tcode":"SWA"},{"airport":"武宿","city":"太原","enAirport":"","match":"太原 武宿|taiyuanwusu|TYN","pinyin":"taiyuanwusu","tcode":"TYN"},{"airport":"潍坊","city":"潍坊","enAirport":"","match":"潍坊 潍坊|weifang|WEF","pinyin":"weifang","tcode":"WEF"},{"airport":"五桥","city":"万州","enAirport":"","match":"万州 五桥|wanxianwuqiao|WXN","pinyin":"wanxianwuqiao","tcode":"WXN"},{"airport":"高崎","city":"厦门","enAirport":"","match":"厦门 高崎|xiamengaoqi|XMN","pinyin":"xiamengaoqi","tcode":"XMN"},{"airport":"伊宁","city":"伊宁","enAirport":"","match":"伊宁 伊宁|yining|YIN","pinyin":"yining","tcode":"YIN"},{"airport":"金湾","city":"珠海","enAirport":"","match":"珠海 金湾|zhuhaijinwan|ZUH","pinyin":"zhuhaijinwan","tcode":"ZUH"},{"airport":"义乌","city":"义乌","enAirport":"","match":"义乌 义乌|yiwu|YIW","pinyin":"yiwu","tcode":"YIW"},{"airport":"朝阳","city":"朝阳","enAirport":"","match":"朝阳 朝阳|chaoyang|CHG","pinyin":"chaoyang","tcode":"CHG"},{"airport":"大理","city":"大理","enAirport":"","match":"大理 大理|dali|DLU","pinyin":"dali","tcode":"DLU"},{"airport":"嘉峪关","city":"嘉峪关","enAirport":"","match":"嘉峪关 嘉峪关|jiayuguan|JGN","pinyin":"jiayuguan","tcode":"JGN"},{"airport":"栎社","city":"宁波","enAirport":"","match":"宁波 栎社|ningbolishe|NGB","pinyin":"ningbolishe","tcode":"NGB"},{"airport":"新郑","city":"郑州","enAirport":"","match":"郑州 新郑|zhengzhouxinzheng|CGO","pinyin":"zhengzhouxinzheng","tcode":"CGO"},{"airport":"张家口","city":"张家口","enAirport":"","match":"张家口 张家口|zhangjiakou|ZQZ","pinyin":"zhangjiakou","tcode":"ZQZ"},{"airport":"宜春明月山","city":"宜春","enAirport":"","match":"宜春 宜春明月山|yichun|YIC","pinyin":"yichun","tcode":"YIC"},{"airport":"毕节飞雄","city":"毕节","enAirport":"","match":"毕节 毕节飞雄|bijie|BFJ","pinyin":"bijie","tcode":"BFJ"},{"airport":"九华山","city":"池州","enAirport":"","match":"池州 九华山|jiuhuashan|JUH","pinyin":"jiuhuashan","tcode":"JUH"}]
for city in cities:
    city['ICAO']=ICAO.get(city["tcode"])

#print(cities)
with open('AirportCode.json','w') as fd:
    json.dump(cities,fd)

d=dict()
with open('AirportCode.json') as fd:
    d=json.load(fd)

print(d)


