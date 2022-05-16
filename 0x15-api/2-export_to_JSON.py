#!/usr/bin/python3
"""export json module"""
import requests
from sys import argv
import json


if __name__ == "__main__":
    total = done = 0
    uid = argv[1]
    user = {}
    tasks = []
    task = {}

    ruser = requests.get('https://jsonplaceholder.typicode.com/users').json()
    for u in ruser:
        if u.get("id") == int(uid):
            username = u.get("username")
            break

    rtodo = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    for elem in rtodo:
        if elem.get("userId") == int(uid):
            task["task"] = elem.get("title")
            task["completed"] = elem.get("completed")
            task["username"] = username
            tasks.append(task)

    user[uid] = tasks
    with open(uid + '.json', 'a') as f:
        json.dump(user, f)
