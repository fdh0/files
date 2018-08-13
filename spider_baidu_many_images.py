#!/usr/bin/python  
# -*- coding: utf-8 -*-
import urllib,json,socket  
import random,os  
import sys
import re
import argparse


##############################################
# 需要您填写和修改的部分,其他部分无需修改
##############################################
#1. 存放图像的文件夹名
folder_name = "baidu_pictures_cat"

#2. 爬虫搜索关键词
keyword = "cat"

#3. 想爬取多少张图片

images_num = 110

################################################

#图片存放目录
DIR_LOC="/home/feng/images_baidu"
#DIR_LOC = "/var/www/html/share/"
dir = DIR_LOC+folder_name+'/'

valid_type = ['.png', '.jpg', '.PNG', '.JPG', '.gif', '.GIF', '.jpeg', '.JPEG']

download_page = 30

socket.setdefaulttimeout(10)

tmpurl = 'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word='+keyword+'&pn='


try:
    if not os.path.isdir(dir):
	os.mkdir(dir)
except OSError:
	print 'can not make dir!'
	sys.exit()

i = 0
    
for dp in xrange(download_page):
    url = tmpurl+str(dp*60)
    pattern = re.compile(r'setData\(\'imgData\', (\{[\s\S]*?\})\);')
    try:
        ipdata = urllib.urlopen(url).read()
    except IOError:
        print 'can not open this url!'
        sys.exit() 
    ipdata = pattern.search(ipdata)
    ipdata = ipdata.group(1)
    _regex = re.compile(r'\\(?![/u"])')  
    ipdata = _regex.sub(r"\\\\", ipdata) 
    imgData = json.loads(ipdata, strict=False)

    if imgData['data']:
        for obj in imgData['data']:
            if obj and obj['objURL']:
                try:
                    data_img = urllib.urlopen(obj['objURL']).read()
                except IOError:
                    print 'img is damaged.'
                else:
                    fPostfix = os.path.splitext(obj['objURL'])[1]
                    if fPostfix in valid_type:
                        filename = dir + os.path.basename(obj['objURL'])
                    else:
                        filename = dir + os.path.basename(obj['objURL']) + '.jpg'
                    try:
                        file_obj = open(filename, 'w')
                        file_obj.write(data_img)
                        file_obj.close()
                    except socket.timeout, e:
                        print 'socket time out!'
                    else:
                        i += 1
                        print 'img '+ str(i) + ' is downloaded!'
                        if(i>=images_num):                           
                            sys.exit()
                    finally:
                        pass
print 'all images have been downloaded!'
sys.exit()
