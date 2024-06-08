#!/usr/bin/python3
"""
This module list employee details
"""
import csv
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
    TOTAL_NUMBER_OF_TASKS = len(todos)
    params = {'userId': theid, 'completed': 'true'}
    oktodos = requests.get(todosurl, params=params).json()
    NUMBER_OF_DONE_TASKS = len(oktodos)
    print(f"Employee {EMPLOYEE_NAME} is done with " +
          f"tasks({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):")
    for todo in oktodos:
        print(f"\t {todo['title']}")
    data = []
    for todo in todos:
        data.append([theid, USERNAME, todo['completed'], todo['title']])
    filename = theid + ".csv"
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for da in data:
            writer.writerow(da)
