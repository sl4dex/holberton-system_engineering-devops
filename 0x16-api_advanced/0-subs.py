#!/usr/bin/python3
"""how many subs module"""
import requests


def number_of_subscribers(subreddit):
    """how many subs function"""
    subs = requests.get(f"https://www.reddit.com/r/{subreddit}/about.json",
                        headers={'User-Agent': 'me'}).json()
    return subs['data']['subscribers']
