#!/usr/bin/python3
"""
Queries the Reddit API andreturns number of subscribers for a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/{}/about.json"format(subreddit)
    headers = {"User-Agent": "User Agent"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code = 200:
        return response.json().get("data").get("subscribers")
    else:
        return 0
