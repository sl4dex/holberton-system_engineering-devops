#!/usr/bin/python3
"""all export json module"""
import json
import requests


if __name__ == "__main__":
    alll = {}
    tasks = []

    rtodo = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    ruser = requests.get('https://jsonplaceholder.typicode.com/users').json()
    for u in ruser:
        ide = u.get("id")
        username = u.get("username")

        for elem in rtodo:
            if elem.get("userId") == int(ide):
                tasks.append({"task": elem.get("title"),
                              "completed": elem.get("completed"),
                              "username": username})
                break
        alll[str(ide)] = tasks
    with open('todo_all_employees.json', 'a') as f:
        json.dump(alll, f)
