from netmiko import ConnectHandler

routers = [
    {
        'device_type': 'cisco_ios',
        'host': '10.10.10.200',
        'username': 'maya',
        'password': 'cisco',
        'secret': 'cisco',
        'global_cmd_verify': False,
    },
    {
        'device_type': 'cisco_ios',
        'host': '10.10.11.201',
        'username': 'elliot',
        'password': 'cisco',
        'secret': 'cisco',
        'global_cmd_verify': False,
    },
    {
        'device_type': 'cisco_ios',
        'host': '10.10.13.201',
        'username': 'malliot',
        'password': 'cisco',
        'secret': 'cisco',
        'global_cmd_verify': False,
    },
]

for router in routers:
    print(f"\nConfiguring {router['host']}...")
    connection = ConnectHandler(**router)

    commands = [
        'interface loopback 0',
        'ip address 1.1.1.1 255.255.255.255',
        'description configured by netmiko python script',
        'no shutdown',
    ]
    connection.enable()
    output = connection.send_config_set(commands)
    print(output)

    connection.send_command_timing('write memory')
    print(f"Config saved on {router['host']}")
    connection.disconnect()