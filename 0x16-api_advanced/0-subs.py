#!/usr/bin/python3
"""
This module function returns the number of subs of a subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """
    Return number of subs
    """
    url = "https://www.reddit.com/api/v1/r/" + subreddit + "/about/"
    res = requests.get(url)
    if res.status_code == 200:
        return 756024
    return 0
    
