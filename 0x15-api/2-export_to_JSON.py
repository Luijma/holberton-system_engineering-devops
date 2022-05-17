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
        i = 0
        final = len(tasks) - 1

        with open(emp_id + '.json', 'w', encoding='utf-8') as json:
            json.write("{" + '"{}": ['.format(emp_id))

            for task in tasks:
                if task['completed']:
                    task_state = "true"
                else:
                    task_state = "false"

                json.write('{' + '"task: {}", '.format(task.get('title')))
                json.write('"completed": {}, '.format(task_state))
                json.write('"username": "{}"'.format(emp_name))

                if i < final:
                    json.write('}, ')
                    i += 1

            json.write('}]}')
