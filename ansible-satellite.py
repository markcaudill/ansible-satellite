#!/usr/bin/env python

import argparse
import ConfigParser
import json
import os
import xmlrpclib


def main():
    parser = argparse.ArgumentParser(
            description='Dynamic inventory from Satellite')
    parser.add_argument('--config', help='configuration file',
                        default='%s/.ansible-satellite' % os.path.expanduser('~'))
    parser.add_argument('--list', action='store_true')
    parser.add_argument('--host', action='store_true')
    args = parser.parse_args()

    # No support for --host yet
    if args.host is True:
        print '{}'
        return

    # Parse the config file
    config = ConfigParser.ConfigParser()
    config.read(args.config)
    
    # Setup the client and obtain a key
    client = xmlrpclib.Server(config.get('satellite', 'url'))
    key = client.auth.login(config.get('credentials', 'username'),
                            config.get('credentials', 'password'))
    
    # Get the data
    groups = {}
    for group in client.systemgroup.listAllGroups(key):
        group_safe_name = group['name'].lower().replace(' ', '_')
        groups[group_safe_name] = []
        for system in client.systemgroup.listSystems(key, group['name']):
            groups[group_safe_name].append(system['hostname'])

    # Format the data
    if args.list is True:
        print json.dumps(groups, indent=2)
    else:
        for group in groups:
            print '[%s]' % group
            print '\n'.join(groups[group])
            print    

if __name__ == '__main__':
    main()
