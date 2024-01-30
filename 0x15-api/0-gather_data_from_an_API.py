#!/usr/bin/python3
'''
Python script that, using this REST API,
for a given employee ID, returns information about his/her TODO list progress.
'''

import re
import requests
import sys
# Define the base URL
REST_API = "https://jsonplaceholder.typicode.com"

if __name__ == '__main__':
    # Check if any command-line arguments were passed
    if len(sys.argv) > 1:
        # Check if the passed argument is a number
        if re.fullmatch(r'\d+', sys.argv[1]):
            id = int(sys.argv[1])
            req = requests.get('{}/users/{}'.format(REST_API, id)).json()
            task_req = requests.get('{}/todos'.format(REST_API)).json()
            emp_name = req.get('name')
            tasks = list(filter(lambda x: x.get('userId') == id, task_req))
            completed_tasks = list(filter(lambda x: x.get('completed'), tasks))
            print(
                'Employee {} is done with tasks({}/{}):'.format(
                    emp_name,
                    len(completed_tasks),
                    len(tasks)
                )
            )
            # prints the titles of any completed tasks
            if len(completed_tasks) > 0:
                for task in completed_tasks:
                    print('\t {}'.format(task.get('title')))
