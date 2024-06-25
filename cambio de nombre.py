from ncclient import manager

# COMUNICACION CON ROUTER
router = {
    'host': '192.168.7.58',  
    'port': 830,
    'username': 'cisco',
    'password': 'cisco123!',
    'hostkey_verify': False
}

# NUEVO NOMBRE DEL ROUTER
new_hostname = "Apellido1Apellido2"  # Cambia esto por el nombre deseado

# CONFIGURACIÓN PARA CAMBIAR EL NOMBRE DEL ROUTER
config_hostname = f"""
<config>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <hostname>{new_hostname}</hostname>
    </native>
</config>
"""

# ENVIO DE CONFIGURACIÓN
with manager.connect(**router) as m:
    netconf_reply = m.edit_config(target='running', config=config_hostname)
    print(netconf_reply)
