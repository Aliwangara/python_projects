# Create a program named api_practice.py that:

# Imports requests and json.

# Asks the user to enter a GitHub username.

# Sends a GET request to this URL:

# https://api.github.com/users/<username>


# If the user exists:

# Print their name, public_repos, followers, and profile URL.

# Save all this info into a JSON file named github_user.json.

# If the username is invalid or the request fails, print a clear error message.


import requests
import json
import os



class UsernamenotfoundError(Exception):
    pass
class requestFailureError(Exception):
    pass

github_data_file = "github_user.json"





try:
    username_input = input("Enter your Github Username:  ").strip()
    
    if not username_input:
        raise UsernamenotfoundError("Please enter a correct username ")
    
    github_url = requests.get(f"https://api.github.com/users/{username_input}")

    if github_url.status_code == 404:
        raise UsernamenotfoundError("⚠️ User not found.")
    elif github_url.status_code != 200:
        raise requestFailureError(f"⚠️ Request failed with status code {github_url.status_code}.")

except ValueError:
    print("Value error please enter a text")
except UsernamenotfoundError as e:
    print("⚠️",e)
else:
    data = github_url.json()
    print("\n✅ GitHub User Information:")
    print("Name:", data.get("name"))
    print("Public Repositories:", data.get("public_repos"))
    print("Followers:", data.get("followers"))
    print("Profile URL:", data.get("html_url"))

    with open(github_data_file, "w", newline="") as f:
        json.dump(data,f,indent=4)
    print(f"\n💾 Data saved successfully to '{github_data_file}'.")
finally:
    print("Welcome")
    
    

