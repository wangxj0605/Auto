# -*- coding: utf-8 -*-
'''
@File  : elk.py
@Author: 汪先锦
@Date  : 2020/4/14 17:21
@Desc  : 
'''
import requests
url='http://sit.kibana.baozun.work/elasticsearch/_msearch?rest_total_hits_as_int=true&ignore_throttled=true'
data='''
{"index":"hub4*","ignore_unavailable":true,"preference":1586856175616}
{"version":true,"size":2000,"sort":[{"@timestamp":{"order":"desc","unmapped_type":"boolean"}}],"_source"
:{"excludes":[]},"aggs":{"2":{"date_histogram":{"field":"@timestamp","interval":"10m","time_zone":"Asia
/Shanghai","min_doc_count":1}}},"stored_fields":["*"],"script_fields":{},"docvalue_fields":[{"field"
:"@timestamp","format":"date_time"}],"query":{"bool":{"must":[{"query_string":{"query":"4055017063629"
,"analyze_wildcard":true,"default_field":"*"}},{"range":{"@timestamp":{"gte":1586793600000,"lte":1586879999999
,"format":"epoch_millis"}}}],"filter":[],"should":[],"must_not":[]}},"highlight":{"pre_tags":["@kibana-highlighted-field
@"],"post_tags":["@/kibana-highlighted-field@"],"fields":{"*":{}},"fragment_size":2147483647}}
'''


r=requests.post(url=url,data=data,)
print(r.text)