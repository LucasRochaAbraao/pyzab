# pyzab
A simple Python implementation of a Zabbix API wrapper.

## Installation

Simply install the `https://pypi.org/project/pyzab/` package:
`pip install pyzab`


## Usage
First, make sure to have a `.env` file alongside your script, with your credentials. This helps keep your url and token away from version control by adding it to .gitignore. This is optional, but strongly recommended. If you skip this step, initialize the Zabbix class with your credential strings. The optional .env file should look like this:
```python
## .env.py
zabbix_auth_token='key_from_zabbix_api'
zabbix_url='zabbix_api_url'
```
On a new python file, import the Zabbix class:
```python
## my_new_zabbix_script.py
from pyzab import Zabbix
```

Now import and load the `.env` file (otherwise, use the url and token as strings):
```python
## my_new_zabbix_script.py
from dotenv import load_dotenv # pip install python-dotenv
load_dotenv()
```

You can now initialize the Pyzab Zabbix api wrapper, and begin making api calls:
```python
## my_new_zabbix_script.py
zabbix = pyzab.Zabbix(os.getenv('zabbix_url'), os.getenv('zabbix_auth_token')) # or zabbix = pyzab.Zabbix('http://your_url/:8080/api_jsonrpc.php', 'your_zabbix_api_token')
all_hosts = zabbix.get_all_hosts() # returns a list with all hosts.
```

## Examples

### Example 1: Add a new host to Zabbix server
After you initialize the wrapper as shown above:

```python
zabbix = pyzab.Zabbix(os.getenv('zabbix_url'), os.getenv('zabbix_auth_token'))
new_host = zabbix.create_host(hostname="new_hostname", ip="10.99.99.99", group_id="5", templateid="10186") # You can get groupid and templateid from the zabbix front end with debug enabled
```
The `create_host` method returns a python Dict with the new host's 'hostid' (inside a list, we need to index it) to the `new_host` variable. 
We can then check the new host's data with another api call:
```python
new_host_data = zabbix.get_host(host_id=new_host['hostids'][0])
```
