#!/usr/bin/python3
"""
Uses RESPT API for a given employee ID, returns information about
their todolist
"""


import requests
from sys import argv


if __name__ == '__main__':
    argc = len(argv)
    if (argc == 2 and argv[1].isdigit()):

        # Set Api link and info
        REST = 'https://jsonplaceholder.typicode.com/'
        emp_id = argv[1]

        # Request for employee information
        emp_response = requests.get(REST + 'users/' + emp_id)

        # Extract employee info from response
        emp_name = emp_response.json().get("username")

        # Request for todo-list information and make dictionary
        todo_response = requests.get(REST + 'todos?userId=' + emp_id)
        tasks = todo_response.json()

        # variables for counting tasks
        tasks_done = 0
        task_count = 0
        task_string = ""

        with open(emp_id + '.csv', 'w', encoding='utf-8') as csv_file:
            for task in tasks:
                csv_file.write('"{}","{}","{}","{}"\n'.
                               format(emp_id, emp_name,
                                      task.get("completed"),
                                      task.get("title")))
