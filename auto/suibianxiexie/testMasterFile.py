# -*- coding: utf-8 -*-
'''
@File  : testMasterFile.py
@Author: 汪先锦
@Date  : 2020/5/21 10:26
@Desc  : 
'''
import requests
import time

url = "http://sit.kibana.baozun.work/elasticsearch/_msearch?rest_total_hits_as_int=true&ignore_throttled=true"
headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "content-type": "application/.",
    "kbn-version": "6.6.2",
    "kbn-xpack-sig": "55ad01edfc90ee6ebea06fc2ec9ce894"
}

str1 = []
file_1 = open("ysld_sku.txt", "r", encoding="utf-8")
for line in file_1.readlines():
    str1.append(line.replace("\n", ""))
    file_1.close()

for i in str1:
    url = "http://sit.kibana.baozun.work/elasticsearch/_msearch?rest_total_hits_as_int=true&ignore_throttled=true"
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "content-type": "application/.",
        "kbn-version": "6.6.2",
        "kbn-xpack-sig": "55ad01edfc90ee6ebea06fc2ec9ce894"
    }
    playlod = """{"index":"hub3*","ignore_unavailable":true,"preference":1590027088683}
    {"version":true,"size":2000,"sort":[{"@timestamp":{"order":"desc","unmapped_type":"boolean"}}],"_source":{"excludes":[]},"aggs":{"2":{"date_histogram":{"field":"@timestamp","interval":"1h","time_zone":"Asia/Shanghai","min_doc_count":1}}},"stored_fields":["*"],"script_fields":{},"docvalue_fields":[{"field":"@timestamp","format":"date_time"}],"query":{"bool":{"must":[{"query_string":{"query":"%s","analyze_wildcard":true,"default_field":"*"}},{"range":{"@timestamp":{"gte":1589422443134,"lte":1590027243134,"format":"epoch_millis"}}}],"filter":[],"should":[],"must_not":[]}},"highlight":{"pre_tags":["@kibana-highlighted-field@"],"post_tags":["@/kibana-highlighted-field@"],"fields":{"*":{}},"fragment_size":2147483647}}
""" % i

    res = requests.post(url=url, data=playlod, verify=False, headers=headers)

    response = res.json()
    re = (response['responses'][0]['hits']['hits'])
    if re != []:
        filename = '报文.txt'
        with open(filename, 'a+') as file_object:
            file_object.write('SKU:{}\n报文{}\n'.format(i, response))
        time.sleep(1)

print('-------------------测试结束---------------------------------')
