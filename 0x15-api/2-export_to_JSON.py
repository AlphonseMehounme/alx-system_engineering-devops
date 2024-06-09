#!/usr/bin/python3
"""
This module list employee details
"""
import json
import requests
import sys


if __name__ == "__main__":
    theid = sys.argv[1]
    empurl = "https://jsonplaceholder.typicode.com/users/" + theid
    todosurl = "https://jsonplaceholder.typicode.com/todos/"
    emp = requests.get(empurl).json()
    EMPLOYEE_NAME = emp['name']
    USERNAME = emp['username']
    params = {'userId': theid}
    todos = requests.get(todosurl, params=params).json()
    # TOTAL_NUMBER_OF_TASKS = len(todos)
    # params = {'userId': theid, 'completed': 'true'}
    # oktodos = requests.get(todosurl, params=params).json()
    # NUMBER_OF_DONE_TASKS = len(oktodos)
    # print(f"Employee {EMPLOYEE_NAME} is done with " +
    #       f"tasks({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):")
    data = {}
    dat = []
    for todo in todos:
        dat.append({"task": todo['title'], "completed": todo['completed'],
                    "username": USERNAME})
    data.update({theid: dat})
    # print(data)
    filename = theid + ".json"
    with open(filename, 'w') as file:
        json.dump(data, file)
