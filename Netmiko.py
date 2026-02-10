from netmiko import ConnectHandler
net_connect=ConnectHandler(
    device_type='linux',
    host='',
    username='vcti',
    password='inD@18us'
)
output=net_connect.send_command(
    'cd Dev72 && touch de.txt && ls'
)
print(output)
