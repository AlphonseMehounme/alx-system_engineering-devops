#!/usr/bin/python3
"""
This module function returns the number of subs of a subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """
    Return number of subs
    """
    url = "https://www.reddit.com/r/" + subreddit + "/about.json"
    headers = {
        'User-Agent': 'subs/0.0.1'
    }
    res = requests.get(url)
    if res.status_code == 200:
        res = res.json()
        return res['data']['subscribers']
    return 0
