# vlanET.py

def validar_vlan(vlan_id):
    if 1 <= vlan_id <= 1005:
        return "VLAN en corresponde a rango normal"
    elif 1006 <= vlan_id <= 4094:
        return "VLAN en rango extendido, favor revisar"
    else:
        return "Número de VLAN fuera de rango, favor gestionar VLAN correcta"

if __name__ == "__main__":
    vlan_id = int(input("Introduce el número de VLANs: "))
    resultado = validar_vlan(vlan_id)
    print(resultado)
