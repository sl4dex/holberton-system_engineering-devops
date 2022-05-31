#!/usr/bin/python3
"""hot posts module"""
import requests


def top_ten(subreddit):
    """hot posts function"""
    hot = requests.get(
        f"https://www.reddit.com/r/{subreddit}/hot/.json?limit=10",
        headers={'User-Agent': 'me'})
    if hot.status_code == 404:
        return 0
    else:
        hot = hot.json()
        for child in hot['data']['children']:
            print(child['data']['title'])
