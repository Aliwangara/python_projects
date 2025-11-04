import requests



def github_data(username):
    response = requests.get(f"https://api.github.com/users/{username}")
    if response.status_code == 200:
        data = response.json()
        return {
            "github_name": data["name"],
            "public_repos": data["public_repos"],
            "followers": data["followers"],
            "profile_url": data["html_url"]
        }
    else:
        return None
    