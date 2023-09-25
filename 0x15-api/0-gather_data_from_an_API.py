#!/usr/bin/python3
"""
This script fetches data from a REST API and displays
the employee's TODO list progress.
"""

import requests
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
    employee_name = user_data.get('name')

    # Fetch data
    todo_url = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
            employee_id)
    response_todo = requests.get(todo_url)
    todo_list = response_todo.json()

    # Calculate the number of completed tasks
    total_tasks = len(todo_list)
    completed_tasks = sum(1 for task in todo_list if task.get('completed'))

    # Display the result
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, completed_tasks, total_tasks))
    for task in todo_list:
        if task.get('completed'):
            print("\t {}".format(task.get('title')))
