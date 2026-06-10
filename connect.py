from netmiko import ConnectHandler
from datetime import datetime

routers = [
    {
        'device_type': 'cisco_ios', #R2
        'host': '10.10.10.200',
        'username': 'maya',
        'password': 'cisco',
        'global_cmd_verify': False,
    },
    {
        'device_type': 'cisco_ios', #R1
        'host': '10.10.11.201',
        'username': 'elliot',
        'password': 'cisco',
        'global_cmd_verify': False,
    },
    {
        'device_type': 'cisco_ios', #R3
        'host': '10.10.13.201',
        'username': 'malliot',
        'password': 'cisco',
        'global_cmd_verify': False,
    },
]

timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
filename = f'network_inventory_{timestamp}.txt'

with open(filename, 'w') as f:
    for router in routers:
        print(f"\n{'='*50}")
        print(f"Connecting to {router['host']}...")
        connection = ConnectHandler(**router)
        
        f.write(f"\n{'='*50}\n")
        f.write(f"Router: {router['host']}\n")
        f.write(f"Timestamp: {timestamp}\n")
        
        output = connection.send_command_timing('show ip interface brief')
        f.write(f"\n--- Interface Summary ---\n{output}\n")
        print(output)
        
        output = connection.send_command_timing('show version | include IOS Software|uptime is|processor')
        f.write(f"\n--- Device Inventory ---\n{output}\n")
        
        connection.disconnect()
        print(f"Disconnected from {router['host']}")

print(f"\nOutput saved to {filename}")