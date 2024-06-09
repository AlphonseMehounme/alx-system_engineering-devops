#!/usr/bin/python3
"""
This module list all tasks from each employee
"""
import json
import requests
import sys


if __name__ == "__main__":
    # theid = sys.argv[1]
    empsurl = "https://jsonplaceholder.typicode.com/users/"
    todosurl = "https://jsonplaceholder.typicode.com/todos/"
    emps = requests.get(empsurl).json()
    # USER_ID = emp['userId']
    # EMPLOYEE_NAME = emp['name']
    # USERNAME = emp['username']
    # params = {'userId': USER_ID}
    # todos = requests.get(todosurl, params=params).json()
    # TOTAL_NUMBER_OF_TASKS = len(todos)
    # params = {'userId': theid, 'completed': 'true'}
    # oktodos = requests.get(todosurl, params=params).json()
    # NUMBER_OF_DONE_TASKS = len(oktodos)
    # print(f"Employee {EMPLOYEE_NAME} is done with " +
    #       f"tasks({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):")
    data = {}
    for emp in emps:
        USER_ID = emp['id']
        EMPLOYEE_NAME = emp['name']
        USERNAME = emp['username']
        params = {'userId': USER_ID}
        todos = requests.get(todosurl, params=params).json()
        dat = []
        for todo in todos:
            dat.append({"username": USERNAME, "task": todo['title'],
                        "completed": todo['completed']})
        data.update({USER_ID: dat})
    # print(data)
    filename = "todo_all_employees.json"
    with open(filename, 'w') as file:
        json.dump(data, file)
