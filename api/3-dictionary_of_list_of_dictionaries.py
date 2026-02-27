#!/usr/bin/python3
"""
Script that exports all employees' TODO list data to JSON format.
"""

import json
import requests


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch all users
    users_response = requests.get(f"{base_url}/users")
    users = users_response.json()

    # Fetch all todos
    todos_response = requests.get(f"{base_url}/todos")
    todos = todos_response.json()

    # Build dictionary
    final_data = {}

    for user in users:
        user_id = str(user.get("id"))
        username = user.get("username")

        # Initialize list for this user
        final_data[user_id] = []

        for task in todos:
            if task.get("userId") == user.get("id"):
                final_data[user_id].append({
                    "username": username,
                    "task": task.get("title"),
                    "completed": task.get("completed")
                })

    # Write JSON file
    with open("todo_all_employees.json", "w") as json_file:
        json.dump(final_data, json_file)
