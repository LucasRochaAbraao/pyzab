#!/usr/bin/env python3
# coding=utf-8

"""
    Nesse exemplo, eu pego todos hosts que estão desabilitados no zabbix,
    e habilito cada caso estão respondendo icmp.
"""
import os
import pyzab # pip install pyzab
from icmplib import ping # pip install icmplib
from dotenv import load_dotenv # pip install python-dotenv
load_dotenv()

zabbix = pyzab.Zabbix(os.getenv('zabbix_url'), os.getenv('zabbix_auth_token'))
todos_hosts_desabilitados = zabbix.get_all_hosts(filter={"status": "1"}) # pegar todos que estão desabilitados

for host in todos_hosts_desabilitados:
    interface = zabbix.get_host_interface(host_id=host['hostid'])
    disponibilidade = ping(interface['ip'])
    if disponibilidade.is_alive: # verdadeiro se o host tá pingando
        zabbix.enable_host(host['hostid'])
