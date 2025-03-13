#!/usr/bin/python3
"""Query Subreddit"""


import requests


def top_ten(subreddit):
    """Query Reddit and print titles of the first 10hot posts"""

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    # Set a custom User-Agent to avoid too many request error
    headers = {'User-Agent': 'My user Agent 1.0'}

    # Send a  GET request to the Reddit API
    response = requests.get(url, headers=headers, allow_redirects=False)

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            children = response.json().get('data').get('children')
            for i in range(10):
                print(children[i].get('data').get('title'))
        else:
            print("None")
    except Exception:
        print("None")
