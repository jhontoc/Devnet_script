import json

with open("json_example.json","r") as data:
    json_data=data.read()

json_dict=json.loads(json_data)
devices=json_dict["TABLE_inv"]["ROW_inv"]
serialnumber=[]
productid=[]
for item in range(0,len(devices)):
 productid.append(json_dict["TABLE_inv"]["ROW_inv"][item]["productid"])
 serialnumber.append(json_dict["TABLE_inv"]["ROW_inv"][item]["serialnum"])

with open("json_example.json","w") as data:
    json.dump(devices,data,indent=4)


