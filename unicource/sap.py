import requests
from bs4 import BeautifulSoup

SOURCE_URL = 'http://uspap1.unist.ac.kr:8000/sap/bc/webdynpro/sap/zcmw5223#'
ECC_URL = 'http://uspap1.unist.ac.kr:8000'

REQUEST_HEADERS = {
'Accept': '*/*',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3',
'Connection': 'keep-alive',
'Content-Type': 'application/x-www-form-urlencoded',
'DNT': '1',
'Host': 'uspap1.unist.ac.kr:8000',
'Origin': 'http://uspap1.unist.ac.kr:8000',
'Referer': 'http://uspap1.unist.ac.kr:8000/sap/bc/webdynpro/sap/zcmw5223',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0'
}

SESSION_HEADERS = {
'Accept': '*/*',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3',
'Connection': 'keep-alive',
'Cookie': 'sap-usercontext=sap-client=700',
'DNT': '1',
'Host': 'uspap1.unist.ac.kr:8000',
'Prefer': 'safe',
'Referer': 'http://uspap1.unist.ac.kr:8000/sap/bc/webdynpro/sap/zcmw5223',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0'
}

def get_sap_wd_secure_id(soup_base):
    form = soup_base.find('form', {'id': 'sap.client.SsrClient.form'})
    secure_id = form.find('input', {'id': 'sap-wd-secure-id'})
    sap_wd_secure_id = secure_id.get('value')
    return sap_wd_secure_id

sess = requests.Session()
soup_jar = {'hello':'hello'}
sess.headers = SESSION_HEADERS
sess.cookies.update({'sap-usercontext': 'sap-client=700'})

res_init = sess.get(SOURCE_URL)
soup_jar['init'] = BeautifulSoup(res_init.text, 'html.parser')

form = soup_jar['init'].find('form', {'name': 'sap.client.SsrClient.form'})
action = form.get('action')
res_base = sess.post(ECC_URL + action)

soup_jar['base'] = BeautifulSoup(res_base.text, 'lxml')

sapid = get_sap_wd_secure_id(soup_jar['base'])
print(sapid)
