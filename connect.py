from netmiko import ConnectHandler

router = {
    'device_type': 'cisco_ios',
    'host': '10.10.10.200',
    'username': 'maya',
    'password': 'cisco',
    'global_cmd_verify': False,
    'conn_timeout': 10,
}

connection = ConnectHandler(**router)
print("Connected successfully!")
output = connection.send_command('show ip interface brief')
print(output)
connection.disconnect()