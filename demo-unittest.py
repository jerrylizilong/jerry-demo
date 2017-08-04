import httplib2
import unittest

#发送http 请求，传入拼装好的完整http 报文
def sendRequest(url):
    http = httplib2.Http(timeout=30)
    headers = {'Content-type': 'application/json;charset=utf8'}
    try :
        response, content = http.request(url, 'GET')
        content = content.decode('utf-8')
    except httplib2.ServerNotFoundError as e:
        response = "Error"
        content = e
    except Exception as e:
        response = "Error"
        content = e
    return response, content

# 通过 yahoo finance 接口查询不同币种之间的汇率
def search(fromCurrency, toCurrency):
    url = 'http://finance.yahoo.com/d/quotes.csv?e=.csv&f=sl1d1t1&s='
    print(toCurrency.strip())
    url1 = url + toCurrency.strip() + fromCurrency + '=x'
    print(url1)
    response, content = sendRequest(url1)
    list = content.split(',')
    print(list[1])
    result = list[1]
    if result!='N/A':
        result= float(result)
    return result


class demoUnittest(unittest.TestCase):
    def setUp(self):
        print('start searching:')

    def tearDown(self):
        print('end')

    def test1(self):
        fromCurrency = 'CNY'
        toCurrency = 'USD'
        self.assertEqual(round(search(fromCurrency, toCurrency)*search( toCurrency,fromCurrency),2),1, msg='the currency rate is wrong')


    def test2(self):
        fromCurrency = 'CAD'
        toCurrency = 'USD'
        self.assertEqual(round(search(fromCurrency, toCurrency)*search( toCurrency,fromCurrency),2),1, msg='the currency rate is wrong')

    def test3(self):
        fromCurrency = 'JPY'
        toCurrency = 'USD'
        self.assertEqual(round(search(fromCurrency, toCurrency)*search( toCurrency,fromCurrency),2),1, msg='the currency rate is wrong')


    def test4(self):
        fromCurrency = 'HKD'
        toCurrency = 'USD'
        self.assertEqual(round(search(fromCurrency, toCurrency)*search( toCurrency,fromCurrency),2),1, msg='the currency rate is wrong')

    def test5(self):
        fromCurrency = 'GBP'
        toCurrency = 'USD'
        self.assertEqual(round(search(fromCurrency, toCurrency)*search( toCurrency,fromCurrency),2),1, msg='the currency rate is wrong')

