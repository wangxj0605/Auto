import unittest

import requests

from interfaceTest import logg


class MyTestCase(unittest.TestCase):
    def test_caipiao(self):
        try:
            # headers = {'Content-Tpye': 'application/json'}
            url = 'https://api.binstd.com/caipiao/query'
            data = {
                'caipiaoid': '13',
                'issueno': '',
                'appkey': '6aab843350e75ae0'
            }
            r1 = requests.post(url, data)
            status = r1.json()
            self.assertEqual(status['status'], 0)
        except:
            loginfo = logg.log()
            loginfo.get_logger('接口请求异常,请检查接口的参数和url是否有误!')
        finally:
            pass


if __name__ == '__main__':
    unittest.main()
