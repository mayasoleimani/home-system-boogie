#switch configuration script using netmiko to connect to switch and configure VLANs
from netmiko import ConnectHandler
from phase1_gns3.devices import switch

print("Connecting to SW1...")
connection = ConnectHandler(**switch)
connection.enable()

vlans = [
    {'id': 10, 'name': 'MANAGEMENT'},
    {'id': 20, 'name': 'SERVERS'},
    {'id': 30, 'name': 'USERS'},
]

#create a list of commands to configure VLANs on the switch
vlan_commands = []
for vlan in vlans:
    vlan_commands.append(f"vlan {vlan['id']}")
    vlan_commands.append(f" name {vlan['name']}")

#use CLI to configure VLANs on the switch
output = connection.send_config_set(vlan_commands)
print("VLANs configured:")
print(output)

# verify vlans have been configured
output = connection.send_command_timing('show vlan brief')
print("\nVLAN verification:")
print(output)

connection.send_command_timing('write memory')
print("Config saved!")
connection.disconnect()