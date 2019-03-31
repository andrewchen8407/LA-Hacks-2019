#!/usr/bin/env python

import json
import ssl
import urllib.parse
import urllib.request
from human import Human
import random
global nessie
nessie = None
account_dict = None

def get_json() -> list:
    response = None

    try:
        url = "http://api.reimaginebanking.com/customers?key=d82c21942a5a727b975804aa4e8d7155"
        context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
        response = urllib.request.urlopen(url, context=context)
        json_array = response.read()
        global nessie
        global account_dict
        nessie = json.loads(json_array)
        names_and_ids = list(zip(get_ids(),get_names()))
        account_dict = {k:(v,0, Human(k,v,1000,100,100,100,100)) for k,v in names_and_ids}
        for k in account_dict:
            account_dict[k][2].set_health(random.randint(50,100))
            account_dict[k][2].set_luxury(random.randint(5, 25))
            account_dict[k][2].set_entertainment(random.randint(30, 50))
            account_dict[k][2].set_food(random.randint(30, 80))

        # url = "http://api.reimaginebanking.com/customers?key=d82c21942a5a727b975804aa4e8d7155"
        # json_array = response.read()
        # nessie = json.loads(json_array)
        #
        # url = "http://api.reimaginebanking.com/customers?key=d82c21942a5a727b975804aa4e8d7155"
        # json_array = response.read()
        # nessie = json.loads(json_array)

    except Exception as E:
        print(E)

    finally:
        if response is not None:
            response.close()


def get_names():
    names = []
    for d in nessie:
        names.append(d['first_name'] + ' ' + d['last_name'])
    return names

def get_ids():
    ids = []
    for d in nessie:
        ids.append(d['_id'])
    return ids


def set_balance(pin, amount):
    if pin in account_dict:
        account_dict[pin] = (account_dict[pin][0], amount)
    else:
        print("Wrong ID")


# def get_dates(list_of_dicts: ['dict']) -> list:
#     """Receives parsed JSON response and returns a list of dates, each of which is associated with available stock info
#     from that date, within the specified time period.
#
#     param list_of_dicts: The list returned from the get_json method; the list is filled with JSON objects converted into
#     Python dictionaries."""
#     dates = []
#
#     for d in list_of_dicts:
#         dates.append(d['date'])
#
#     return dates
#
#
# def get_opening_prices(list_of_dicts: ['dict']) -> list:
#     """Receives parsed JSON response and returns a list of opening prices, one opening price per date.
#
#     param list_of_dicts: The list returned from the get_json method; the list is filled with JSON objects converted into
#     Python dictionaries."""
#     opening_prices = []
#
#     for d in list_of_dicts:
#         opening_prices.append(d['open'])
#
#     return opening_prices
#
#
# def get_closing_prices(list_of_dicts: ['dict']) -> list:
#     """Receives parsed JSON response and returns a list of closing prices, one closing price per date.
#
#     param list_of_dicts: The list returned from the get_json method; the list is filled with JSON objects converted into
#     Python dictionaries."""
#     closing_prices = []
#
#     for d in list_of_dicts:
#         closing_prices.append(d['close'])
#
#     return closing_prices
#
#
# def get_high_prices(list_of_dicts: ['dict']) -> list:
#     """Receives parsed JSON response and returns a list of high prices, one high price per date.
#
#     param list_of_dicts: The list returned from the get_json method; the list is filled with JSON objects converted into
#     Python dictionaries."""
#     high_prices = []
#
#     for d in list_of_dicts:
#         high_prices.append(d['high'])
#
#     return high_prices
#
#
# def get_low_prices(list_of_dicts: ['dict']) -> list:
#     """Receives parsed JSON response and returns a list of low prices, one low price per date.
#
#     param list_of_dicts: The list returned from the get_json method; the list is filled with JSON objects converted into
#     Python dictionaries."""
#     low_prices = []
#
#     for d in list_of_dicts:
#         low_prices.append(d['low'])
#
#     return low_prices
#
#
# def get_volumes(list_of_dicts: ['dict']) -> list:
#     """Receives parsed JSON response and returns a list of volumes, one volume per date.
#
#     param list_of_dicts: The list returned from the get_json method; the list is filled with JSON objects converted into
#     Python dictionaries."""
#     volumes = []
#
#     for d in list_of_dicts:
#         volumes.append(d['volume'])
#
#     return volumes
#
#
# class InvalidTimePeriodError(Exception):
#     pass
