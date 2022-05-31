#!/usr/bin/python3
"""how many subs module"""
import requests


def number_of_subscribers(subreddit):
    """how many subs function"""
    subs = requests.get(f"https://www.reddit.com/r/{subreddit}/about.json",
                        headers={'User-Agent': 'me'})
    if subs.status_code == 404:
        return 0
    else:
        subs = subs.json()
    return subs['data']['subscribers']
