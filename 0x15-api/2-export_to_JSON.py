#!/usr/bin/python3
"""Export tasks owned by a specific employee to JSON"""
import json
import requests
from sys import argv

if __name__ == "__main__":
    employee_id = argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    tasks_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        employee_id)

    # Get user information
    user_response = requests.get(user_url)
    user_data = user_response.json()
    username = user_data.get("username")

    # Get tasks for the user
    tasks_response = requests.get(tasks_url)
    tasks_data = tasks_response.json()

    # Create a dictionary to store tasks for the user
    user_tasks = {employee_id: []}

    # Populate the dictionary with task details
    for task in tasks_data:
        task_details = {
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        }
        user_tasks[employee_id].append(task_details)

    # Save the tasks to a JSON file named with the employee's ID
    filename = "{}.json".format(employee_id)
    with open(filename, "w") as json_file:
        json.dump(user_tasks, json_file)
