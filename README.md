# Repo for automatic switch configuration via netmiko

Source for netmiko, tutorials and examples:
https://github.com/ktbyers/netmiko

Prerequisites:
```
pip install netmiko
```

## Howto show_on_devices_by_list

```
cd show_on_devices_by_list
vim devices.txt
python netmiko_show.py
```

The script will
1. set the local username as login for the switches
2. ask for the password of your user
3. ask you for the show command to be issued
4. run over all the switches defined in devices.txt and show you the output of the command

## Howto conf_on_devices_by_list

```
cd conf_on_devices_by_list
vim devices.txt
vim commands.txt
python netmiko_conf.py
```
Theres no need to enter configure terminal or write the configuration, the script will do that.

The script will
1. set the local username as login for the switches
2. ask for the password of your user
3. run over all the switches defined in devices.txt and issue the commands in configuration terminal
4. Write the configuration