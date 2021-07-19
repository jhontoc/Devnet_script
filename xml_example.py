import xmltodict

with open("xml_example.xml","r") as data:
    xml_data=data.read()

#obejective: to parse the xml data to dictionary
xml_dict=xmltodict.parse(xml_data)
print(xml_dict)
xml_dict["nf:rpc-reply"]["nf:data"]["show"]["inventory"]["__readonly__"]["TABLE_inv"]
#objective to unparse from dictionary >> xml
print(xmltodict.unparse(xml_dict,pretty=True))

with open("xml_example.xml","w") as data:
    data.write(xmltodict.unparse(xml_dict,pretty=True))
