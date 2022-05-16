#!/usr/bin/python3
"""todos module"""
from sys import argv
import requests

if __name__ == "__main__":
    total = done = 0
    uid = argv[1]
    tasks = []

    ruser = requests.get('https://jsonplaceholder.typicode.com/users').json()
    for u in ruser:
        if u.get("id") == int(uid):
            name = u.get("name")

    rtodo = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    for elem in rtodo:
        if elem.get("userId") == int(uid):
            if elem.get("completed") is True:
                # completed
                done = done + 1
                tasks.append(elem.get("title"))
            # total
            total = total + 1

    print("Employee {} is done with tasks({}/{}):".format(name, done, total))
    for t in tasks:
        print("     {}".format(t))
