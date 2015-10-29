# Ansible Satellite #

## Description ##
An Ansible [dynamic inventory][1] script.

[1]: https://docs.ansible.com/ansible/intro_dynamic_inventory.html

## Usage ##

    ansible all -i <path/to/ansible-satellite.py> --list-hosts

If you run `ansible-satellite.py` by itself it will output in an Ansible
inventory-style format. When called by Ansible, it outputs JSON.

## Configuration ##
The configuration is looked for in `~/.ansible-satellite` by default.

Example:

```ini
[satellite]
url = http://satellite-server.exampl.com/rpc/api

[credentials]
username = coolsysadmin
password = SecretStuff
```
