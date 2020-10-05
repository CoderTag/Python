# Refer : https://realpython.com/python-json/
# make an API request to the JSONPlaceholder service
# Can you determine which users have completed the most tasks?

import json
import requests

respone = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(respone.text)
print(todos[:5])

# Map of userId to number of complete TODOs for that user
todos_by_user = {}

# Increment complete TODOs count for each user.
for todo in todos:
    if todo["completed"]:
        try:
            # Increment the existing user's count.
            todos_by_user[todo["userId"]] += 1
        except KeyError:
            # This user has not been seen. Set their count to 1.
            todos_by_user[todo["userId"]] = 1

print(f"Before sorting: {todos_by_user}")

# Create a sorted list of (userId, num_complete) pairs.
top_users = sorted(todos_by_user.items(),
                   key=lambda x: x[1], reverse=True)

print(f"After sorting: {top_users}")

# Get the maximum number of complete TODOs.
max_complete = top_users[0][1]

# Create a list of all users who have completed the maximum number of TODOs.
users = []
for user, num_complete in top_users:
    if num_complete < max_complete:
        break
    users.append(str(user))

max_users = " and ".join(users)

s = "s" if len(users) > 1 else ""
print(f"user{s} {max_users} completed {max_complete} TODOs")

# Define a function to filter out completed TODOs of users with max completed TODOS.
def keep(todo):
    is_complete = todo["completed"]
    has_max_count = str(todo["userId"]) in users
    return is_complete and has_max_count

# Write filtered TODOs to file.
with open("filtered_data_file.json", "w") as data_file:
    filtered_todos = list(filter(keep, todos))
    json.dump(filtered_todos, data_file, indent=2)
