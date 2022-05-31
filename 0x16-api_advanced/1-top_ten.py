#!/usr/bin/python3
"""
Queries Reddit API for titles of top 10 hot posts of a subreddit
"""
import json
import requests


def top_ten(subreddit):
    """ prints top 10 hot posts """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "User-Agent"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        for i in response.json().get("data").get("children"):
            print(i.get("data").get("title"))
    else:
        print("None")
