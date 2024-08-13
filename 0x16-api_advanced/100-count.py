#!/usr/bin/python3
"""
A recursive function that queries API Reddit
"""

import requests


def count_words(subreddit, word_list, after=None, w_count={}):
    """
    The function that quesries API Reddit
    """
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'my_reddit_app'}
    params = {'after': after, 'limit': 100}
    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)
    if response.status_code != 200:
        return

    data = response.json().get('data', {})
    children = data.get('children', [])
    if not children:
        if not w_count:
            return
        sorted_words = sorted(w_count.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_words:
            print(f"{word}: {count}")
        return
    for child in children:
        title = child.get('data', {}).get('title', '').lower()
        for word in word_list:
            word_lower = word.lower()
            w_count[word_lower] = w_count.get(word_lower, 0) +\
                title.split().count(word_lower)
    after = data.get('after')
    if after:
        count_words(subreddit, word_list, after, w_count)
    else:
        sorted_words = sorted(w_count.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_words:
            print(f"{word}: {count}")
