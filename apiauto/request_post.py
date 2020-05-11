# -*- coding: utf-8 -*-
'''
@File  : request_post.py
@Author: 汪先锦
@Date  : 2020/5/11 11:27
@Desc  : 
'''
import requests
import json
def post():
    par={'yoyo':'hello world','pythonQQ群':'226296743'}
    response=requests.post('http://httpbin.org/post',data=par)
    print(response.text)

def post_json():
    par = {'yoyo': 'hello world', 'pythonQQ群': '226296743'}
    response = requests.post('http://httpbin.org/post', json=json.dumps(par))
    print(response.json())
    print(response.text)


# def headers():
#     url='http://passport.cnblogs.com/user/signin'
#     payloa={"input1":"xxx",
#            "input2":"xxx",
#            "remember":True}
#     header={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0",
#
#      "Accept": "application/json, text/javascript, */*; q=0.01",
#
#      "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
#
#      "Accept-Encoding": "gzip, deflate, br",
#
#      "Content-Type": "application/json; charset=utf-8",
#
#      "X-Requested-With": "XMLHttpRequest",
#      "cookie": "_ga=GA1.2.1943758666.1534139129; __gads=ID=7dc4241d7a659b07:T=1534324492:S=ALNI_MZVPsflA1iXFU4OlGdZ1E2i_akRIQ; UM_distinctid=170c219eb647b-0f8674f59491f7-c383f64-1fa400-170c219eb65e7; _gid=GA1.2.147810609.1589168540; .Cnblogs.AspNetCore.Cookies=CfDJ8B9DwO68dQFBg9xIizKsC6TPNEkMBSSnZ5k-dDwKNH3Fge857GP3GfzsqFK7XvkVGSEmZnvvURWNcu-2fP9chPTVhpgXAGetesXD1eaMZLgIqX74Af-ndT8eKMI8QUobqJEqU1EWD0bmHfeQRtVydrEna8I3yNBNcqFXsr9gz9QWGEq8Y-WWjvvPg-YHNF5sACHlGErnoXwAdqokalrS6sknyOBN4jp1Tgrug2-rSZRisPoNUsN87LwVYVIl8g-HGza3ou-bYNGUvRCjHVdGBUb28aYQAGjakkIGTCYogjkVL9C9iI9hqiRWFvuNOLu2hRxigllfQe3hzXM_sxAjHYeuR2kaczOCQ0-jTPbYBWrmHY-inrgPuD0Bvo61ENZtEc5AiwE5I8_gPhsgUq0sKFwJJtJvHkJZDa8yaN4u6oId34bYdGxYoF_yAzOLpjdnCHsI89UnMjT8ePlT9DedyT-81Z6KwTl5acgaK5HZJQDWn5UeI5SJE2JHscF-_tPCZYvLPrE1lLWtaxJUfZdC7gMQ6VTMbGFEBh7fB00qbvoJZs5YIgJgNTJdgEMZt1JocQ; .CNBlogsCookie=C0B0269EFA1E7F677792B070A50890C1178B3995FC2028A5F9CF0C155595AC6D89DBFF0B9003EA55F90067E395D36202391266EF1A0245DE7A154C57413F326CC618923F36C3BE11087B59C09B621F89FED7FB87F8825FB66B5A82CE3FAEEF787C3101AB; _gat=1",
#     "Connection": "keep-alive"
#     }
#     response=requests.post(url,json=json.dumps(payloa),header=header,verify=False)
#     print(response.json())
# #post_json()
# if __name__ == '__main__':
#     headers()