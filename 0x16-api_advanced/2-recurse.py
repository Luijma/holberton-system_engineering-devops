#!/usr/bin/python3
"""A recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit"""
import requests
import sys


def recurse(subreddit, hot_list=[], after=""):
    """returns the number of all hot articles of a given subreddit"""
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {"User-Agent": "User Agent"}
    params = {"after": after}
    response = requests.get(url, headers=headers, params=params)

    if after is None:
        return hot_list
    if response.status_code == 200:
        response = response.json()
        after = response.get('data').get('after')
        hot = response.get('data').get('children')
        for child in hot:
            hot_list.append(child.get('data').get('title'))
        return recurse(subreddit, hot_list, after)
    else:
        return (None)
