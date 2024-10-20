import requests
from faker import Faker

fake = Faker(['en_US'])

def contains_profanity(text):
    """
    Checks if the given text contains profanity using an external API.

    :param text: The text to check for profanity.
    :return: True if profanity is found, False otherwise.
    """
    url = f"https://www.purgomalum.com/service/containsprofanity?text={text}"
    try:
        response = requests.get(url)
        response.raise_for_status()  
        return response.text == "true"  
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return False

def is_username_taken(name):
    """
    Checks if the given username is already taken using the Roblox API.

    :param name: The username to check.
    :return: True if the username is taken, False if it is available.
    """
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

def genNicknames(amount: int = 1, prefix: str = '', suffix: str = '', min_length: int = 8, max_length: int = 15):
    """
    Generates a list of available nicknames with optional customization.

    :param amount: The number of nicknames to generate. Default is 1.
    :param prefix: Optional prefix to add to each nickname. Default is an empty string.
    :param suffix: Optional suffix to add to each nickname. Default is an empty string.
    :param min_length: Minimum length of the nickname. Default is 3.
    :param max_length: Maximum length of the nickname. Default is 15.
    :return: A list of valid nicknames.
    """
    generated_nicks = []
    
    while len(generated_nicks) < amount:
        nick = fake.user_name()

       
        if prefix:
            nick = prefix + nick
        if suffix:
            nick = nick + suffix
        
        
        if len(nick) < min_length or len(nick) > max_length:
            continue
        
    
        if not contains_profanity(nick) and not is_username_taken(nick):
            generated_nicks.append(nick)
    
    return generated_nicks
