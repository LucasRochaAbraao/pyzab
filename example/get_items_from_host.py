#!/usr/bin/env python3
# coding=utf-8

"""
    Nesse exemplo, printamos os items de um host.
"""
import os
import pyzab # pip install pyzab
from dotenv import load_dotenv # pip install python-dotenv
load_dotenv()

# query a specific host for all its items
zabbix = pyzab.Zabbix(os.getenv('zabbix_url'), os.getenv('zabbix_auth_token'))
host_items = zabbix.get_items(host_id="10084")

print(host_items)
