from constants import *
from parser import *

import requests
from bs4 import BeautifulSoup

datas ={
        'sap-charset': "utf-8",
}

sess = requests.Session()
soup_jar = {'hello':'hello'}
sess.headers = SESSION_HEADERS
sess.cookies.update({'sap-usercontext': 'sap-client=700'})

res_init = sess.get(SOURCE_URL)
soup_jar['init'] = BeautifulSoup(res_init.text, 'html.parser')

form = soup_jar['init'].find('form', {'name': 'sap.client.SsrClient.form'})
action = form.get('action')
res_base = sess.post(HOST_URL + action)

soup_jar['base'] = BeautifulSoup(res_base.text, 'lxml')

sapid = get_sap_wd_secure_id(soup_jar['base'])
contextid = get_sap_contextid(soup_jar['base'])
    
datas['sap-wd-secure-id'] = sapid

targeturl = HOST_URL + contextid

sess2 = requests.Session()
sess2.headers = REQUEST_HEADERS

datas['SAPEVENTQUEUE'] = "ClientInspector_Notify~E002Id~E004WD01~E005Data~E004ClientWidth~003A682px~003BClientHeight~003A359px~003BScreenWidth~003A1368px~003BScreenHeight~003A912px~003BScreenOrientation~003Alandscape~003BThemedTableRowHeight~003A21px~003BThemedFormLayoutRowHeight~003A25px~003BDeviceType~003ADESKTOP~E003~E002ResponseData~E004delta~E005EnqueueCardinality~E004single~E003~E002~E003~E001Custom_ClientInfos~E002Id~E004WD01~E005WindowOpenerExists~E004false~E005ClientURL~E004http~003A~002F~002Fuspap1.unist.ac.kr~003A8000~002Fsap~002Fbc~002Fwebdynpro~002Fsap~002Fzcmw5223~0023~E005ClientWidth~E004682~E005ClientHeight~E004359~E005DocumentDomain~E004unist.ac.kr~E005IsTopWindow~E004true~E005ParentAccessible~E004true~E003~E002ClientAction~E004enqueue~E005ResponseData~E004delta~E003~E002~E003~E001LoadingPlaceHolder_Load~E002Id~E004_loadingPlaceholder_~E003~E002ResponseData~E004delta~E005ClientAction~E004submit~E003~E002~E003"
req = sess2.post(targeturl, data=datas)

datas['_stateful_'] = "X"
datas['SAPEVENTQUEUE'] = "TabStrip_TabSelect~E002Id~E004WD53~E005ItemId~E004WD54~E005ItemIndex~E0040~E005FirstVisibleItemIndex~E004-1~E003~E002ResponseData~E004delta~E005ClientAction~E004submit~E003~E002~E003"
req = sess2.post(targeturl,data=datas)


datas['SAPEVENTQUEUE'] = "ComboBox_ListAccess~E002Id~E004WDF7~E005ItemListBoxId~E004WDF8~E005FilterValue~E004CSE~E003~E002ResponseData~E004delta~E005ClientAction~E004submitAsync~E003~E002~E003"
req = sess2.post(targeturl, data=datas)

datas['SAPEVENTQUEUE'] = "ComboBox_Change~E002Id~E004WDF7~E005Value~E004CSE~E003~E002ResponseData~E004delta~E005EnqueueCardinality~E004single~E005Delay~E004full~E003~E002~E003~E001Button_Press~E002Id~E004WDFA~E003~E002ResponseData~E004delta~E005ClientAction~E004submit~E003~E002~E003"
req = sess2.post(targeturl,data=datas)

print(req.text)
