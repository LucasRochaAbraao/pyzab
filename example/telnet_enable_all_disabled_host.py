#!/usr/bin/env python3
# coding=utf-8

"""
    Nesse exemplo, eu pego todos hosts que estão desabilitados no zabbix,
    e habilito cada caso estão aceitando conexão via telnet. Esse script
    é bem parecido com o outro aqui dos exemplos, para casos de hosts
    com bloqueio de ping.
"""
import os
import pyzab # pip install pyzab
from telnetlib import Telnet
from dotenv import load_dotenv # pip install python-dotenv
load_dotenv()

zabbix = pyzab.Zabbix(os.getenv('zabbix_url'), os.getenv('zabbix_auth_token'))
todos_hosts_desabilitados = zabbix.get_all_hosts(filter={"status": "1"}) # pegar todos que estão desabilitados

for host in todos_hosts_desabilitados:
    interface = zabbix.get_host_interface(host_id=host['hostid'])
    disponibilidade = None
    try:
        disponibilidade = Telnet(interface['ip'], "10050", 2)
    except TimeoutError:
        pass # não ligo de ter dado timeout, quero o que aceitou a conexão
    
    if disponibilidade: # verdadeiro se o host tá acessível via telnet
        print("habilitando!")
        zabbix.enable_host(host['hostid'])
