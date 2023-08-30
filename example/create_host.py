#!/usr/bin/env python3

"""
    In this example, we will create a regular host with a tag,  visible hostname, ip, community and template.
"""
import os
import pyzab # pip install pyzab
from dotenv import load_dotenv # pip install python-dotenv
load_dotenv()

zabbix = pyzab.Zabbix(os.getenv('zabbix_url'), os.getenv('zabbix_auth_token'))

host_result = zabbix.create_host(
        hostname="cloudflare_dns",
        visible_hostname="Cloudflare DNS",
        group_id=2,
        template_id=10582,
        ip="1.1.1.1",
        tags=[{"tag": "mytag", "value": "1"}],
        macros=[{"macro": "{$LOCATION}", "value": "0:0:0", "description": "lat,lon,alt"}],
        interface_type="SNMP",
        snmp_community="COMMUNITY"
    )

print(host_result)

"""
{
  'type': 2,
  'details': {
     'version': 'SNMPv2c',
     'community':'COMMUNITY',
     'bulk': 1
     },
  'main': 1,
  'useip': 1,
  'ip': '1.1.1.1',
  'dns': '',
  'port': '10050'
}
"""