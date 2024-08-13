#!/usr/bin/python3
"""Function that queries the Reddit API and return no of subscriber"""
import requests


def number_of_subscribers(subreddit):
    """this return the total numbers of subscribers"""
    url = requests.get(
      "https://www.reddit.com/r/{}/about.json".format(subreddit),
      headers={"User-Agent": "Custom"},
    )

    if url.status_code == 200:
        return url.json().get("data").get("subscribers")
    else:
        return 0
