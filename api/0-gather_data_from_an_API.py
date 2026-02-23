#!/usr/bin/python3
"""
Script that, for a given employee ID, returns information
about his/her TODO list progress using a REST API.
"""

import requests
import sys


if __name__ == "__main__":
    # Check if employee ID is provided
    if len(sys.argv) != 2:
        sys.exit(1)

    employee_id = sys.argv[1]

    # Base URL of the API
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch employee information
    user_response = requests.get(f"{base_url}/users/{employee_id}")
    user_data = user_response.json()
    employee_name = user_data.get("name")

    # Fetch TODO list for the employee
    todos_response = requests.get(
        f"{base_url}/todos", params={"userId": employee_id}
    )
    todos = todos_response.json()

    # Calculate total and completed tasks
    total_tasks = len(todos)
    done_tasks = [task for task in todos if task.get("completed") is True]
    number_of_done_tasks = len(done_tasks)

    # Print required output
    print(f"Employee {employee_name} is done with tasks"
          f"({number_of_done_tasks}/{total_tasks}):")

    for task in done_tasks:
        print("\t {}".format(task.get("title")))
