# TODO make requests to github API

import requests

def get_github_user(username):
    # dealing with multiple different errors here
    # returning a tuple if this succed or fail
    try:
        response = requests.get(f'https://api.github.com/users/{username}')
        if response.status_code == 404: # not found
            return None, f'User {username} not found'
        response.raise_for_status()  # raise error for other bad status codes
        response_json = response.json()
        user_info = extract_user_info(response_json)
        return user_info, None  # no error
    except Exception as e:
        return None, 'Error connecting to GitHub '


def extract_user_info(json_response):
    return {
        'login': json_response.get('login'),
        'name': json_response.get('name'),
        'avatar_url': json_response.get('avatar_url'),
        'home_page': json_response.get('html_url'),
        'repos': json_response.get('public_repos'),
        
    }