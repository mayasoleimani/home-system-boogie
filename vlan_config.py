from netmiko import ConnectHandler
from devices import switch

print("Connecting to SW1...")
connection = ConnectHandler(**switch)
connection.enable()

# Configure VLANs
vlans = [
    {'id': 10, 'name': 'MANAGEMENT'},
    {'id': 20, 'name': 'SERVERS'},
    {'id': 30, 'name': 'USERS'},
]

vlan_commands = []
for vlan in vlans:
    vlan_commands.append(f"vlan {vlan['id']}")
    vlan_commands.append(f" name {vlan['name']}")

output = connection.send_config_set(vlan_commands)
print("VLANs configured:")
print(output)

# Verify
output = connection.send_command_timing('show vlan brief')
print("\nVLAN verification:")
print(output)

connection.send_command_timing('write memory')
print("Config saved!")
connection.disconnect()