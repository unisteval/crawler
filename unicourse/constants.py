year_component = "WD31" 
semester_component = "WD4B"
stringSearch_component = "WD53"
stringSearchClass_component = "WD54"
search_component = "WDFA"
searchBox_component = "WDFB"
searchButton_component = "WDFD"
download_component = "WD9B"

SOURCE_URL = 'http://uspap1.unist.ac.kr:8000/sap/bc/webdynpro/sap/zcmw5223'
HOST_URL = 'http://uspap1.unist.ac.kr:8000'

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

EXCEL_HEADERS = {
'Host': 'uspap1.unist.ac.kr:8000',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Language': 'ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3',
'Accept-Encoding': 'gzip, deflate',
'Prefer': 'safe',
'DNT': '1',
'Connection': 'keep-alive',
'Referer': 'http://uspap1.unist.ac.kr:8000/sap/bc/webdynpro/sap/zcmw5223',
'Cookie': 'sap-usercontext=sap-client=700',
'Upgrade-Insecure-Requests': '1'
}

INIT_EVENTQUEUE = "ClientInspector_Notify~E002Id~E004WD01~E005Data~E004ClientWidth~003A150px~003BClientHeight~003A759px~003BScreenWidth~003A1368px~003BScreenHeight~003A912px~003BScreenOrientation~003Alandscape~003BThemedTableRowHeight~003A21px~003BThemedFormLayoutRowHeight~003A25px~003BDeviceType~003ADESKTOP~E003~E002ResponseData~E004delta~E005EnqueueCardinality~E004single~E003~E002~E003~E001Custom_ClientInfos~E002Id~E004WD01~E005WindowOpenerExists~E004false~E005ClientURL~E004http~003A~002F~002Fuspap1.unist.ac.kr~003A8000~002Fsap~002Fbc~002Fwebdynpro~002Fsap~002Fzcmw5223~0023~E005ClientWidth~E004150~E005ClientHeight~E004759~E005DocumentDomain~E004unist.ac.kr~E005IsTopWindow~E004true~E005ParentAccessible~E004true~E003~E002ClientAction~E004enqueue~E005ResponseData~E004delta~E003~E002~E003~E001LoadingPlaceHolder_Load~E002Id~E004_loadingPlaceholder_~E003~E002ResponseData~E004delta~E005ClientAction~E004submit~E003~E002~E003"

SEARCH_EVENTQUEUE = ""

def search_eventqueue():
    global SEARCH_EVENTQUEUE
    SEARCH_EVENTQUEUE = "TabStrip_TabSelect~E002Id~E004" + \
        stringSearch_component + "~E005ItemId~E004" + \
        stringSearchClass_component +"~E005ItemIndex~E0040~E005FirstVisibleItemIndex~E004-1~E003~E002ResponseData~E004delta~E005ClientAction~E004submit~E003~E002~E003"
    return SEARCH_EVENTQUEUE
