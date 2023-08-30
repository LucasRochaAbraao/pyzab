#!/usr/bin/env python3
# coding=utf-8

"""
    Nesse exemplo, eu print os dados de um host.
"""
import os
import pyzab # pip install pyzab
from dotenv import load_dotenv # pip install python-dotenv
load_dotenv()

zabbix = pyzab.Zabbix(os.getenv('zabbix_url'), os.getenv('zabbix_auth_token'))
host = zabbix.get_host(filter={"name": "Host para testes de API"})

print(host)