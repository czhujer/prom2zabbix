#!/usr/bin/python3

import argparse

from prom2zabbix_lib import getDiscovery

#import sys

#import string
#import json
#import requests
#import socket
#import md5

# check a import parameters
parser = argparse.ArgumentParser(description='prom2zabbix bridge')

parser.add_argument('--action', metavar='action', required=True,
                   help='action to process: discovery | get')
parser.add_argument('--service', metavar='service', required=True,
                   help='service to process: prometheus')
parser.add_argument('--debug', metavar='debug', type=int,
                   help='debug mode enable (1)')

args = parser.parse_args()

action = args.action.lower()
service = args.service.lower()
debug = args.debug

url = "http://127.0.0.1:9090/api/v1"
if debug:
    print("DEBUG: basic url: " + url)

if action == 'discovery':

    if service == "prometheus":
      url = url + "/query?query=up"
      if debug:
          print("DEBUG: url: " + url)
      getDiscovery(url,debug)
    else:
      print("Wrong service name!");
      parser.print_help()

elif action == 'get':

    print("Not impemented yet!");
    exit(1);
    #getStatus(serviceName)

else:
    parser.print_help()


