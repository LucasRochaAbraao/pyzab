#!/usr/bin/env python3

"""
    In this example, we will create a web scenario with one step into an
    existing template.
"""
import os
import pyzab # pip install pyzab
from dotenv import load_dotenv # pip install python-dotenv
load_dotenv()

zabbix = pyzab.Zabbix(os.getenv('zabbix_url'), os.getenv('zabbix_auth_token'))

webscenario_response = zabbix.create_webscenario(
    webscenario_name="Homepage",
    template_id="10582",
    steps={
        "name": "Homepage",
        "url": "http://example.com",
        "status_code": "200",
        "step_number": 1
    }
)

print(webscenario_response)
