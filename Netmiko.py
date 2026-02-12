from netmiko import ConnectHandler
net_connect=ConnectHandler(
    device_type='linux',
    host='10.0.4.253',
    username='vcti',
    password='XXXXXXX'
)
output=net_connect.send_command(
    'cd Dev72 && touch de.txt && ls'
)
print(output)
