#!/usr/bin/python3
'''extended python script that  exports data into a JSON file.
'''
import json
import requests


API_URL = 'https://jsonplaceholder.typicode.com'
"""
URLs for fetching employee's tasks and name based on the ID
"""


if __name__ == '__main__':
    # API call to get users data
    users_res = requests.get('{}/users'.format(API_URL)).json()
    # API call to get todos data
    todos_res = requests.get('{}/todos'.format(API_URL)).json()
    users_data = {}

    for user in users_res:
        id = user.get('id')
        user_name = user.get('username')
        # Filter todos associated with the user
        todos = list(filter(lambda x: x.get('userId') == id, todos_res))
        user_data = list(map(
            lambda x: {
                'username': user_name,
                'task': x.get('title'),
                'completed': x.get('completed')
            },
            todos
        ))
        # Store user's data in the dict
        users_data['{}'.format(id)] = user_data

    # Writes the JSON data to a file
    with open('todo_all_employees.json', 'w') as file:
        json.dump(users_data, file)
