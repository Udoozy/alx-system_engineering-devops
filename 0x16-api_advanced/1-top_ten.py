#!/usr/bin/python3
"""
Function That querries the Reddit API and prints 1st 10 h pst
"""
import requests


def top_ten(subreddit):
    """
    This function prinits the 10 hottest post on subreddit
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
      "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    parameters = {
      "limit": 10
    }
    response = requests.get(url, headers=headers, params=parameters,
                           allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return
    results = response.json().get("data")
    [print(c.get("data").get("title")) for c in results.get("children")]
