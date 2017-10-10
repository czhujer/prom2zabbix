#!/usr/bin/python3

import requests
import json

def getDiscovery(url,debug=0):
    discovery_list = {}
    discovery_list['data'] = []

    results = requests.get(url).text

#    if debug:
#        print("DEBUG: results: " + results)

    results_parsed = json.loads(results)
    results_data = results_parsed['data']

    if debug:
        print("DEBUG: results_data: " + json.dumps(results_data))

    service_loop_id=0
    zbx_items_final = ""
    zbx_items = ""

    for item in results_data['result']:
        job = item['metric']['job']
        name = item['metric']['__name__']

        zbx_item1 = '"{#ITEMNAME}": ' + '"' + job + '"'
        zbx_item2 = '"{#ITEMSTATUS}": ' + '"' + name + '"'

        if service_loop_id == 0:
            zbx_items = ''
        else:
            zbx_items = ',\n'

        zbx_items += '\t{\n\t\t' + zbx_item1 + ',\n\t\t' + zbx_item2 + '\n\t}'

        zbx_items_final += zbx_items
        service_loop_id+=1

    zbx_items_final  = '{\n\t"data": [\n' + zbx_items_final + '\n\n\t]\n}\n'
    print(zbx_items_final)

def getDiscovery2(url,debug=0):
    results = requests.get(url).text
    results_parsed = json.loads(results)
    results_data = results_parsed['data']

    if debug:
        print("DEBUG: results_data: " + json.dumps(results_data))

    service_loop_id=0
    zbx_items_final = ""
    zbx_items = ""

    for item in results_data['result']:

        zbx_item1 = '"{#ITEMNAME}": ' + '"' + item['metric']['host'] + '"'

        if service_loop_id == 0:
            zbx_items = ''
        else:
            zbx_items = ',\n'

        zbx_items += '\t{\n\t\t' + zbx_item1 + '\n\t}'

        zbx_items_final += zbx_items
        service_loop_id+=1

    zbx_items_final  = '{\n\t"data": [\n' + zbx_items_final + '\n\n\t]\n}\n'
    print(zbx_items_final)

def getValue(url,debug,item_name):

    results = requests.get(url).text
    item_value = ""

    if debug:
        print("DEBUG: get url: " + url)

    if debug:
        print("DEBUG: results json: " + results)

    results_parsed = json.loads(results)
    results_data = results_parsed['data']['result']

    if debug:
        print("DEBUG: results_data: " + json.dumps(results_data))

    for value in results_data:
        item_value = value['value'][1]

    if item_value == "":
        print("0")
    else:
        print(item_value)
