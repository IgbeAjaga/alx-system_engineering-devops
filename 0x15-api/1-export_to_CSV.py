#!/usr/bin/python3
"""
This script fetches data from a REST API and exports it in CSV format.
"""

import requests
import csv
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: {} <employee_id>".format(sys.argv[0]))

    employee_id = sys.argv[1]

    # Fetch user data
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(
            employee_id)
    response_user = requests.get(user_url)
    user_data = response_user.json()
    user_id = user_data.get('id')
    user_name = user_data.get('username')

    # Fetch data
    todo_url = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
            employee_id)
    response_todo = requests.get(todo_url)
    todo_list = response_todo.json()

    # Create and write to the CSV file
    filename = '{}.csv'.format(user_id)
    with open(filename, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in todo_list:
            task_id = task.get('id')
            task_title = task.get('title')
            task_completed = task.get('completed')
            csv_writer.writerow(
                    [user_id, user_name, task_completed, task_title])

    print("Data exported to {} successfully.".format(filename))
