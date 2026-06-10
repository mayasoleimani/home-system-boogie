from netmiko import ConnectHandler
from devices import routers


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