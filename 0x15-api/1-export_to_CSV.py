#!/usr/bin/python3
"""
Python script to export data in the CSV format
"""

import csv
import json
import requests
from sys import argv


if __name__ == "__main__":
    # create new session for http requests
    sessionReq = requests.Session()
    # Define URLs for fetching employee's tasks and name
    idEmp = argv[1]
    idURL = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(idEmp)
    nameURL = 'https://jsonplaceholder.typicode.com/users/{}'.format(idEmp)

    employee = sessionReq.get(idURL)
    employeeName = sessionReq.get(nameURL)

    json_req = employee.json()
    usr = employeeName.json()['username']

    totalTasks = 0

    for done_tasks in json_req:
        if done_tasks['completed']:
            totalTasks += 1
    # Create a CSV file name based on the employee ID
    fileCSV = idEmp + '.csv'

    with open(fileCSV, "w", newline='') as csvfile:
        write = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)
        # Write data for each task to the CSV
        for i in json_req:
            write.writerow([idEmp, usr, i.get('completed'), i.get('title')])
