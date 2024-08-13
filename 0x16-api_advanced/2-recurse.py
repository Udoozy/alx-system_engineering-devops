#!/usr/bin/python3
"""
Recursive Function that Queries Reddit API
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """This Function is to query Reddit API"""
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'my-reddit_app'}
    params = {'after': after, 'limit': 100}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return None

    datas = response.json().get('data', {})
    children = datas.get('children', [])

    if not children:
        return hot_list if hot_list else None

    hot_list.extend([child.get('data', {}).get('title') for child in children])
    if after is None:
        return hot_list

    return recurse(subreddit, hot_list, after)
