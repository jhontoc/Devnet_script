from env_lab import dnac
import json
import requests
import urllib3
from requests.auth import HTTPBasicAuth
from prettytable import PrettyTable

dnac_devices = PrettyTable(['Hostname','platform_id','Software Type','Software Version','Up Time','MGMT IP'])
dnac_devices.padding_width=1

#silence the insecure warnig due to SSL Certicate
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

headers = {
    'content-type':'application/json',
    'x-auth-token':''
}

def dnac_login(host,username,password):
    url = f'https://{host}/api/system/v1/auth/token'
    response=requests.request("POST",url,auth=HTTPBasicAuth(username,password), headers=headers, verify=False)
    return response.json()['Token']

def network_device_list(dnac,token):
    url=f'https://{dnac["host"]}/api/v1/network-device'
    headers['x-auth-token']=token
    response=requests.request("GET",url,headers=headers,verify=False)
    data=response.json()

    if requests.codes.ok == 200:
        for item in data['response']:
            dnac_devices.add_row([item['hostname'],item['platformId'],item["softwareType"],item['softwareVersion'],item['lastUpdated'],item['managementIpAddress']])

login=dnac_login(dnac['host'],dnac['username'],dnac['password'])
network_device_list(dnac,login)
#print(json.dumps(output,indent=4))
print(dnac_devices)

dict={"1":"item1",
      "2":"item2",
      'mylist':[10,20],
      'nested_dict':{"1":'item1',
                     '2':'item2'
                     }
      }
