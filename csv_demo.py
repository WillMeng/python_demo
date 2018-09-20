#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import codecs
import csv

reload(sys)
sys.setdefaultencoding('utf8')

with open('./demo_read.csv', 'rb') as read_file, open('./demo_write.csv', 'wb') as write_file:
    # 中文乱码解决方案
    write_file.write(codecs.BOM_UTF8)
    reader = csv.reader(read_file)
    writer = csv.writer(write_file)
    # write csv
    writer.writerow(['计划id', '计划', '修改前', '修改后', '修改后-修改前', '修改前-修改后', '修改时间'])
    # read csv  
    for line in reader:
        if str(line[4]) == '否定关键词':
            before_data = line[7]
            after_data = line[8]
            bef_set = set(before_data.strip().split(','))
            aft_set = set(after_data.strip().split(','))
            sub_set = (aft_set - bef_set)
            sub_set1 = (bef_set - aft_set)
            campaign_id = line[1]
            campaign_txt = line[3]
            opt_time = line[9]
            writer.writerow(
                [campaign_id, campaign_txt, before_data, after_data, ','.join(sub_set), ','.join(sub_set1), opt_time])
