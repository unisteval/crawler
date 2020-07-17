import requests
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
