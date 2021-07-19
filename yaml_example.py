import yaml

with open("CISCO-IOS-HSRP-STATECHANGE.yaml","r") as data:
    yaml_data=data.read()
yaml_dict=yaml.load(yaml_data,Loader=yaml.FullLoader)

print(yaml_dict["vars"]["measurement"]["value"])

yaml_dict["vars"]["measurement"]["value"]="jtocaspa_informationl"
print(yaml.dump(yaml_dict,default_flow_style=False))