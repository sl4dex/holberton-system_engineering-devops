#!/usr/bin/python3
"""todos module"""
import requests
from sys import argv


if __name__ == "__main__":
    total = done = 0
    uid = argv[1]
    tasks = []

    ruser = requests.get('https://jsonplaceholder.typicode.com/users').json()
    for u in ruser:
        if u.get("id") == int(uid):
            name = u.get("name")
            username = u.get("username")
            break

    rtodo = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    for elem in rtodo:
        if elem.get("userId") == int(uid):
            with open(uid + '.csv', 'a') as f:
                f.write('"{}","{}","{}","{}"'.format(
                        elem.get("userId"),
                        username,
                        elem.get("completed"),
                        elem.get("title")))
                f.write("\n")
