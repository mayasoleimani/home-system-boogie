from netmiko import ConnectHandler

routers = [
    {
        'device_type': 'cisco_ios',
        'host': '10.10.10.200',
        'username': 'maya',
        'password': 'cisco',
        'global_cmd_verify': False,
    },
    {
        'device_type': 'cisco_ios',
        'host': '10.10.11.201',
        'username': 'elliot',
        'password': 'cisco',
        'global_cmd_verify': False,
    },
    {
        'device_type': 'cisco_ios',
        'host': '10.10.13.201',
        'username': 'malliot',
        'password': 'cisco',
        'global_cmd_verify': False,
    },
]

for router in routers:
    print(f"\nConnecting to {router['host']}...")
    connection = ConnectHandler(**router)
    
    print("--- Device Inventory ---")
    output = connection.send_command('show version')
    print(output)
    
    print("--- Interface Summary ---")
    output = connection.send_command('show ip interface brief')
    print(output)
    
    connection.disconnect()
    print(f"Disconnected from {router['host']}")