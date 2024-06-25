from ncclient import manager
import json
import xmltodict

# COMUNICACION CON ROUTER VIRTUAL
router = {
    'host': '192.168.7.58',  
    'port': 830,
    'username': 'cisco',
    'password': 'cisco123!',
    'hostkey_verify': False
}

#SOLICITUD DE INTERFACES
filter_interfaces = """
<filter>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <interface/>
    </native>
</filter>
"""

# COMUNICACION CON ROYTER
with manager.connect(**router) as m:
    netconf_reply = m.get(filter=filter_interfaces)
    # CONVERSION DE RESPUESTA
    interface_dict = xmltodict.parse(netconf_reply.xml)

# CONVERSION DE JSON
interface_json = json.dumps(interface_dict, indent=4)
print(interface_json)
