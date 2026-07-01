#router configuration script using netmiko to connect to routers and configure loopback interfaces
from netmiko import ConnectHandler
from phase1_gns3.devices import routers


for router in routers:
    print(f"\nConfiguring {router['host']}...")
    connection = ConnectHandler(**router)
    commands = [
        'interface loopback 0',
        'ip address 1.1.1.1 255.255.255.255',
        'description configured by netmiko python script',
        'no shutdown',
    ]
    #configure loopback interface
    connection.enable()
    output = connection.send_config_set(commands)
    print(output)

    connection.send_command_timing('write memory')
    print(f"Config saved on {router['host']}")
    connection.disconnect()