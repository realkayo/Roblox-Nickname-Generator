import requests

def is_username_taken(name):
    url = "https://users.roblox.com/v1/usernames/users"
    payload = {
        "usernames": [name],
        "excludeBannedUsers": False
    }

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        data = response.json().get("data", [])
        

        return bool(data)
    except requests.exceptions.RequestException as err:
        print(f"Error: {err}")
        return False 
