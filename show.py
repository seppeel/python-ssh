#!/usr/bin/env python
from netmiko import Netmiko
from getpass import getpass
from getpass import getuser

print("Setting local username as switch login user")
user=getuser()
print(f"Username: {user}")
pwd=getpass()

print("Enter Switch")
device=input()

print("Enter command")
command=input()

device = {
        "host": device,
        "username": user,
        "password": pwd,
        "device_type": "cisco_ios",
        }

net_connect = Netmiko(**device)
print()
print(net_connect.find_prompt())
output = net_connect.send_command(command)
net_connect.disconnect()
print(output)
print()
