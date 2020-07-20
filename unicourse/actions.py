from constants import *
from parser import *
import requests
from bs4 import BeautifulSoup


class Search:
    def __init__(self, sapid, contextid):
        self.sess = requests.Session()
        self.data = {'sap-charset': 'utf-8'}
        self.url = HOST_URL
        
        self.sess.headers = REQUEST_HEADERS
        self.data['sap-wd-secure-id'] = sapid
        self.url = self.url + contextid
        
        self.data['SAPEVENTQUEUE'] = INIT_EVENTQUEUE
        self.res = self.sess.post(self.url, data=self.data)

        #This part select search mode
        self.data['_stateful_'] = "X"
        self.data['SAPEVENTQUEUE'] = SEARCH_EVENTQUEUE
        self.res = self.sess.post(self.url, data=self.data)


    def set_period(self, year,semester):
        """
        semester 1: 90
        semester summer: 91
        semester 2: 92
        semester winter: 93
        """
        self.data['SAPEVENTQUEUE'] = "ComboBox_Select~E002Id~E004WD31~E005Key~E004"
        self.data['SAPEVENTQUEUE'] = self.data['SAPEVENTQUEUE'] + str(year)
        self.data['SAPEVENTQUEUE'] = self.data['SAPEVENTQUEUE'] + "~E005ByEnter~E004false~E003~E002ResponseData~E004delta~E005ClientAction~E004submit~E003~E002~E003"
        self.res = self.sess.post(self.url, data=self.data)

        self.data['SAPEVENTQUEUE'] = "ComboBox_Select~E002Id~E004WD4B~E005Key~E0040"
        self.data['SAPEVENTQUEUE'] = self.data['SAPEVENTQUEUE'] + str(semester)
        self.data['SAPEVENTQUEUE'] = self.data['SAPEVENTQUEUE'] + "~E005ByEnter~E004false~E003~E002ResponseData~E004delta~E005ClientAction~E004submit~E003~E002~E003"
        self.res = self.sess.post(self.url, data=self.data)


    def search_string(self, string): 
        self.data['SAPEVENTQUEUE'] = "ComboBox_ListAccess~E002Id~E004WDF7~E005ItemListBoxId~E004WDF8~E005FilterValue~E004"
        self.data['SAPEVENTQUEUE'] = self.data['SAPEVENTQUEUE'] + str(string)
        self.data['SAPEVENTQUEUE'] = self.data['SAPEVENTQUEUE'] + "~E003~E002ResponseData~E004delta~E005ClientAction~E004submitAsync~E003~E002~E003"
        self.res = self.sess.post(self.url, data=self.data)

        self.data['SAPEVENTQUEUE'] = "ComboBox_Change~E002Id~E004WDF7~E005Value~E004"
        self.data['SAPEVENTQUEUE'] = self.data['SAPEVENTQUEUE'] + str(string)
        self.data['SAPEVENTQUEUE'] = self.data['SAPEVENTQUEUE'] + "~E003~E002ResponseData~E004delta~E005EnqueueCardinality~E004single~E005Delay~E004full~E003~E002~E003~E001Button_Press~E002Id~E004WDFA~E003~E002ResponseData~E004delta~E005ClientAction~E004submit~E003~E002~E003"
        self.res = self.sess.post(self.url, data=self.data)

    def get_text(self):
        return self.res.text


def initaction():
    """
    get sap-wd-secure-id, session contextid
    """
    sess = requests.Session()
    soup_jar = {'hello':'hello'}
    sess.headers = SESSION_HEADERS
    sess.cookies.update({'sap-usercontext': 'sap-client=700'})

    res_init = sess.get(SOURCE_URL)
    soup_jar['init'] = BeautifulSoup(res_init.text, 'html.parser')

    form = soup_jar['init'].find('form', 
            {'name': 'sap.client.SsrClient.form'})
    action = form.get('action')
    res_base = sess.post(HOST_URL + action)

    soup_jar['base'] = BeautifulSoup(res_base.text, 'lxml')

    sapid = get_sap_wd_secure_id(soup_jar['base'])
    contextid = get_sap_contextid(soup_jar['base'])
    
    return sapid, contextid

