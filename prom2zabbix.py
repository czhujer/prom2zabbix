#!/usr/bin/python3

import argparse

from prom2zabbix_lib import getDiscovery
from prom2zabbix_lib import getDiscovery2
from prom2zabbix_lib import getValue

#import sys

import string
#import json
#import requests
#import socket
#import md5

# check a import parameters
parser = argparse.ArgumentParser(description='prom2zabbix bridge')

parser.add_argument('--action', metavar='action', required=True,
                   help='action to process: discovery | get')
parser.add_argument('--service', metavar='service', required=True,
                   help='service to process: up | nginx_server_requests')
parser.add_argument('--itemname', metavar='itemname',
                   help='item name to get value')
parser.add_argument('--debug', metavar='debug', type=int,
                   help='debug mode enable (1)')

args = parser.parse_args()

action = args.action.lower()
service = args.service.lower()
debug = args.debug

if args.itemname:
    item_name = args.itemname.lower()
else:
    item_name = ""

url = "http://127.0.0.1:9090/api/v1"
if debug:
    print("DEBUG: basic url: " + url)

if action == 'discovery':

    if service == "up":
      url = url + "/query?query=up"
      if debug:
          print("DEBUG: url: " + url)
      getDiscovery(url,debug)
    elif service == "nginx_server_requests":
      url = url + "/query?query=" + service + "{code=\"2xx\"}"
      if debug:
          print("DEBUG: url: " + url)
      getDiscovery2(url,debug)
    else:
      print("ERROR: Wrong service name!");
      parser.print_help()
      exit(2)

elif action == 'get':

    if item_name == "":
      print("ERROR: Wrong item name!");
      parser.print_help()
      exit(2)

    if service == "up":
      url = url + "/query?query=up{job=\"" + item_name + "\"}"
      getValue(url,debug,item_name)
    elif service == "nginx_server_requests":
      params = item_name.split('--')
      url = url + "/query?query=" + service + "{host=\"" + params[0] + "\",code=\"" + params[1] +"\"}"
      getValue(url,debug,item_name)
    else:
      print("ERROR: Wrong service name!");
      parser.print_help()
      exit(2)

else:
    parser.print_help()
    exit(1)
