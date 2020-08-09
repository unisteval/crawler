from .constants import *
from .parser import *
import requests
from bs4 import BeautifulSoup
from datetime import datetime

class Search:
    def __init__(self, sapid, contextid):
        global SEARCH_EVENTQUEUE
        self.sess = requests.Session()
        self.data = {'sap-charset': 'utf-8'}
        self.url = HOST_URL
        
        self.sess.headers = REQUEST_HEADERS
        self.data['sap-wd-secure-id'] = sapid
        self.contextid = contextid
        self.url = self.url + contextid
        
        #Initial session loading
        self.data['SAPEVENTQUEUE'] = INIT_EVENTQUEUE
        self.res = self.sess.post(self.url, data=self.data)

        #This part select search mode
        self.data['_stateful_'] = "X"
        self.data['SAPEVENTQUEUE'] = search_eventqueue()
        self.res = self.sess.post(self.url, data=self.data)


    def set_period(self, year, semester):
        """
        semester 1: 90
        semester summer: 91
        semester 2: 92
        semester winter: 93
        semester 3: 94

        Setting year and semester on session
        
        """
        self.data['SAPEVENTQUEUE'] = "ComboBox_Select~E002Id~E004" + \
            year_component + "~E005Key~E004"
        self.data['SAPEVENTQUEUE'] = self.data['SAPEVENTQUEUE'] + str(year)
        self.data['SAPEVENTQUEUE'] = self.data['SAPEVENTQUEUE'] + "~E005ByEnter~E004false~E003~E002ResponseData~E004delta~E005ClientAction~E004submit~E003~E002~E003"
        self.res = self.sess.post(self.url, data=self.data)

        self.data['SAPEVENTQUEUE'] = "ComboBox_Select~E002Id~E004" + \
            semester_component + "~E005Key~E0040"
        self.data['SAPEVENTQUEUE'] = self.data['SAPEVENTQUEUE'] + str(semester)
        self.data['SAPEVENTQUEUE'] = self.data['SAPEVENTQUEUE'] + "~E005ByEnter~E004false~E003~E002ResponseData~E004delta~E005ClientAction~E004submit~E003~E002~E003"
        self.res = self.sess.post(self.url, data=self.data)


    def search_string(self, string):
        """
        Search string on session
        """
        global search_component
        global searchBox_component
        global searchButton_component

        search_soup = BeautifulSoup(self.res.text, 'lxml')
        
        search_component = get_search_component(search_soup)
        searchBox_component = get_search_box_component(search_soup)
        searchButton_component = get_search_button_component(search_soup)

       #This part type string on box
        self.data['SAPEVENTQUEUE'] = "ComboBox_ListAccess~E002Id~E004" + \
            search_component + "~E005ItemListBoxId~E004" + \
                searchBox_component + "~E005FilterValue~E004"
        self.data['SAPEVENTQUEUE'] = self.data['SAPEVENTQUEUE'] + str(string)
        self.data['SAPEVENTQUEUE'] = self.data['SAPEVENTQUEUE'] + "~E003~E002ResponseData~E004delta~E005ClientAction~E004submitAsync~E003~E002~E003"
        self.res = self.sess.post(self.url, data=self.data)
        
        #This part click "search" button on site
        self.data['SAPEVENTQUEUE'] = "ComboBox_Change~E002Id~E004" + \
            search_component + "~E005Value~E004"
        self.data['SAPEVENTQUEUE'] = self.data['SAPEVENTQUEUE'] + str(string)
        self.data['SAPEVENTQUEUE'] = self.data['SAPEVENTQUEUE'] + "~E003~E002ResponseData~E004delta~E005EnqueueCardinality~E004single~E005Delay~E004full~E003~E002~E003~E001Button_Press~E002Id~E004" + \
                searchButton_component + "~E003~E002ResponseData~E004delta~E005ClientAction~E004submit~E003~E002~E003"
        self.res = self.sess.post(self.url, data=self.data)


    def get_excel(self, file_name):
        """
        get excel file from session
        """
        global download_component

        download_soup = BeautifulSoup(self.res.text, 'lxml')
        download_component = get_download_component(download_soup)

        #Start excel session
        xsess = requests.Session()
        xsess.headers = EXCEL_HEADERS
        
        #prepare excel session
        self.data['SAPEVENTQUEUE'] = "Button_Press~E002Id~E004" + \
            download_component + "~E003~E002ResponseData~E004delta~E005ClientAction~E004submit~E003~E002~E003"
        self.res = self.sess.post(self.url, data=self.data)

        #parse data from prepared excel session
        fileid, action = get_excel_url(BeautifulSoup(self.res.text,'lxml-xml'))        
        
        #replace
        xurl = HOST_URL + action
        xurl = xurl.replace("\\x2f","/")
        xurl = xurl.replace("\\x7e","~")
        xurl = xurl.replace("\\x3f", "?")
        xurl = xurl.replace("\\x2d","-")
        xurl = xurl.replace("\\x3d","=")
        xurl = xurl.replace("\\x253a",":")
        xurl = xurl.replace("\\x26","&")
        xres = xsess.post(xurl)
        
        #write file
        with open(file_name,'wb') as f:
            f.write(xres.content)


    def get_text(self):
        """
        get result text, use for debug
        """
        return self.res.text


def initsession():
    """
    get sap-wd-secure-id, session contextid
    """
    global stringSearch_component
    global year_component
    global semester_component

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
    stringSearchClass_component = \
            get_string_search_class_component(soup_jar['base'])
    stringSearch_component = \
            get_string_search_component(soup_jar['base']) 
    year_component = get_year_component(soup_jar['base'])
    semester_component = get_semester_component(soup_jar['base'])

    return sapid, contextid


def get_file(year, semester, string, file_name):
    """
    capsulize get excel file step
    """
    sapid, contextid = initsession()
    semester_dict = {"1st":90,"summer":91,"2nd":92,"winter":93,"3rd":94}

    if year < 2009 or year > datetime.today().year:
        raise YearError();

    if year == 2012 or year == 2013:
        if semester == 93 or semester == "winter":
            raise SemesterError
    else:
        if semester == 94 or semester == "3rd":
            raise SemesterError

    search = Search(sapid, contextid)

    if semester in [90,91,92,93]:
        search.set_period(year,semester)
    elif semester in semester_dict:
        search.set_period(year,semester_dict[semester])

    search.search_string(string)

    search.get_excel(file_name)
