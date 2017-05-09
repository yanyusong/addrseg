# -*- coding: utf-8 -*-

"""
劝农山镇（长春莲花山生态旅游度假区省级）    220105173000
双营子回族乡（梅花鹿产业经济开发区）（省级）    220112270000 
"""

import sys
import os

"""
这三个还真是地名
"""
names = []
names.append(u'达斡尔民族乡')
names.append(u'鄂伦春民族乡')
names.append(u'回族乡')

suffixs = u"""边境经济合作区管委会
满族蒙古族锡伯族乡
彝族仡佬族布依族乡
苗族彝族布依族乡
彝族苗族布依族乡
彝族布依族苗族乡
布依族白族苗族乡
布依族彝族苗族乡
傣族傈僳族自治乡
侗族土家族苗族乡
社区公共服务中心
鄂伦春族民族乡
苗族彝族满族乡
苗族彝族回族乡
维吾尔族回族乡
白族彝族苗族乡
畲族少数民族乡
柯尔克孜民族乡
回族街道办事处
回族维吾尔族乡
回族彝族苗族乡
傈僳族普米族乡
俄罗斯族民族乡
社区工作委员会
鄂温克民族乡
达斡尔民族乡
蒙古族满族乡
苗族布依族乡
苗族土家族乡
苗族仡佬族乡
满族锡伯族镇
满族蒙古族乡
满族朝鲜族乡
柯尔克孜族乡
朝鲜族满族乡
彝族纳西族乡
彝族布朗族乡
彝族傈僳族乡
布朗族彝族乡
布依族苗族乡
布依族彝族乡
塔吉克民族乡
土家族苗族乡
土家族自治乡
回族东乡族乡
哈萨克民族乡
傈僳族彝族乡
傈僳族傣族乡
仡佬族苗族乡
门巴民族乡
鄂温克族乡
达斡尔族镇
达斡尔族乡
街道办事处
蒙古民族乡
苗族瑶族乡
苗族彝族乡
苗族壮族乡
苗族侗族乡
白族自治乡
白族彝族乡
瑶族苗族乡
珞巴民族乡
朝鲜民族乡
彝族苗族乡
彝族白族乡
彝族傣族乡
壮族瑶族乡
塔吉克族乡
地区办事处
回族苗族乡
回族满族乡
回族民族乡
回族彝族乡
傣族自治乡
侗族苗族乡
管理委员会
社区服务站
阿昌族乡
蒙古族镇
蒙古族乡
纳西族乡
毛南族乡
拉祜族乡
布依族乡
土家族乡
哈尼族乡
傈僳族乡
仫佬族乡
东乡族乡
街道办
藏族乡
苗族乡
羌族乡
白族乡
畲族镇
畲族乡
瑶族乡
满族镇
满族乡
水族乡
民族乡
彝族乡
壮族乡
土族乡
回族镇
回族乡
傣族乡
侗族乡
佤族乡
办事处
街道
苏木
镇
乡"""

suffixs = suffixs.split(os.linesep)
suffixs = [s.strip() for s in suffixs]

bracket = u'（'

def endwith(county, suffixs, code):
    for suffix in suffixs:
        if county.endswith(suffix):
            county = county.replace(suffix, '')
            key = '%s\t%s' % (county, code)
            print key.encode('utf-8')
            return True
    return False

for line in sys.stdin:
    line = line.strip()
    print line
    line = line.decode('utf-8')
    arr = line.split()
    if len(arr) != 2:
        print 'err'
        sys.exit()
    county, code = arr
    if bracket in county:
        county = county.split(bracket, 1)[0]
        key = '%s\t%s' % (county, code)
        print key.encode('utf-8')


    if endwith(county, suffixs, code):
        continue



# 未整理的
"""
中心镇建设管理办公室    140122104000
双城市街道管委会        230182001000
城关社区建设委员会      230882002000
菊园新区管委会  310114003000
滨湖世纪社区    340111008000
南瑞社区公共服务委员会  340203098000
淮滨社区        340311001000
明珠社区        340311002000
文化路街道办事  370402004000
光明路街道办事  370402006000
四新地区管委会  420105012000
大川镇人民政府  420302100000
侨乡街道开发区  429006002000
城中办街道事处  450403003000
城北办街道事处  450403004000
鱼嘴镇人民政府  500105100000
复盛镇人民政府  500105101000
五宝镇人民政府  500105102000
允景洪街道办事  532801001000
乐家湾镇政府    630102100000
韵家口镇政府    630102101000
头屯河区乡类似乡镇单位  650106198000

"""