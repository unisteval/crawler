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

def get_excel_url(soup_base):
    updates = soup_base.find_all('script-call')
    parser = re.compile('\"attachedFileId\":\"[A-F0-9]+\"')
    fileid = parser.search(updates[2].text).group()[18:-1]
    parser = re.compile('\"url\":\"[a-zA-Z0-9\\\\._]+\"')
    url = parser.search(updates[2].text).group()[7:-1]
    return fileid, url
