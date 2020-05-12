#!/usr/bin/env python
from netmiko import Netmiko
from getpass import getpass
from getpass import getuser

cfg_file = "commands.txt"

print("Setting local username as switch login user")
user=getuser()

print(f"Username: {user}")
pwd=getpass()

print("Issuing config commands from commands.txt on all switches from devices.txt")

with open('devices.txt', 'r') as f:
        read = f.readlines()

for device in (read):
    device = {
            "host": device,
            "username": user,
            "password": pwd,
            "device_type": "cisco_ios",
            }
    net_connect = Netmiko(**device)
    print()
    print(net_connect.find_prompt())
    output = net_connect.send_config_from_file(cfg_file)
    print(output)
    print()

    net_connect.save_config()
    print("Saved Config. Disconnecting...")
    net_connect.disconnect()
