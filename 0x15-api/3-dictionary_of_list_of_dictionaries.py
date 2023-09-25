#!/usr/bin/python3
import json
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    task_url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"

    user_response = requests.get(user_url)
    task_response = requests.get(task_url)

    user_data = user_response.json()
    task_data = task_response.json()

    username = user_data.get("username")

    user_tasks = {user_id: []}

    for task in task_data:
        task_dict = {
            "username": username,
            "task": task.get("title"),
            "completed": task.get("completed")
        }
        user_tasks[user_id].append(task_dict)

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(user_tasks, json_file)
