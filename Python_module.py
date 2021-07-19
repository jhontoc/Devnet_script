import math
import json
import calendar as ca
from Class_concept import Router, Switch
"""
this example is to test information about modules
"""
#print(help(json.load))
#print(help(ca))
#print(ca.month(2021,5))


RTR1=Router('XR9000','1.1.1.1','6.5.1')
RTR2=Router('ISR4001','2.2.2.2','16.5.1')
SW1=Switch('Catalys9k','3.3.3.3','17.1')

print(f'Routers:\n{RTR1.getdes()}\n{RTR2.getdes()}\nSwitches:\n{SW1.getdes()}')