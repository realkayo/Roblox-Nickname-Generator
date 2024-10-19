import requests

def contains_profanity(text):
    url = f"https://www.purgomalum.com/service/containsprofanity?text={text}"
    try:
        response = requests.get(url)
        response.raise_for_status()  
        return response.text == "true"  
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return False
