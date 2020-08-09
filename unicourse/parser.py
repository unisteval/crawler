import requests
import re
from bs4 import BeautifulSoup

def get_sap_wd_secure_id(soup_base):
    form = soup_base.find('form', {'id': 'sap.client.SsrClient.form'})
    secure_id = form.find('input', {'id': 'sap-wd-secure-id'})
    sap_wd_secure_id = secure_id.get('value')
    return sap_wd_secure_id


def get_sap_contextid(soup_base):
    form = soup_base.find('form', {'id': 'sap.client.SsrClient.form'})
    action = form.get('action')
    return action

def get_string_search_class_component(soup_base):
    form = soup_base.find("span", text="검색")
    get_id = form.get("id")

    parser = re.compile("WD[0-9A-F]+")
    get_num = parser.search(get_id).group()[2:]
    
    get_num = int(get_num,16)
    get_num = get_num - 1
    ret = "WD" + hex(get_num).upper()[2:]

    return ret


def get_string_search_component(soup_base):
    form = soup_base.find("span", text="검색")
    get_id = form.get("id")

    parser = re.compile("WD[0-9A-F]+")
    get_num = parser.search(get_id).group()[2:]
    
    ret = get_num

    return ret


def get_year_component(soup_base):
    text_field = soup_base.find("span", text="학년도")
    
    parser = re.compile("WD[0-9A-F]+")
    text_num = parser.search(text_field.get("id")).group()

    label= soup_base.find("label", id=text_num)
    ret = label.get("f")

    return ret


def get_semester_component(soup_base):
    text_field = soup_base.find("span", text="학 기")
    
    parser = re.compile("WD[0-9A-F]+")
    text_num = parser.search(text_field.get("id")).group()

    label= soup_base.find("label", id=text_num)
    ret = label.get("f")

    return ret


def get_search_component(soup_base):
    """
    The last component of text input is typed search string.
    """
    form = soup_base.find_all("input", type="text")
    ret = form[-1].get("id")
    
    return ret


def get_search_box_component(soup_base):
    get_id = get_search_component(soup_base)

    get_num = get_id[2:]
    
    get_num = int(get_num,16)
    get_num = get_num + 1
    ret = "WD" + hex(get_num).upper()[2:]
    
    return ret


def get_search_button_component(soup_base):
    search_text_list = soup_base.find_all("span", text="검색")
    search_button = search_text_list[-1]

    parser = re.compile("WD[0-9A-F]+")
    ret = parser.search(search_button.get("id")).group()

    return ret


def get_download_component(soup_base):
    search_text = soup_base.find("span", text="다운로드")

    parser = re.compile("WD[0-9A-F]+")
    ret = parser.search(search_text.get("id")).group()

    return ret


def get_excel_url(soup_base):
    updates = soup_base.find_all('script-call')
    parser = re.compile('\"attachedFileId\":\"[A-F0-9]+\"')
    fileid = parser.search(updates[2].text).group()[18:-1]
    parser = re.compile('\"url\":\"[a-zA-Z0-9\\\\._]+\"')
    url = parser.search(updates[2].text).group()[7:-1]
    return fileid, url
