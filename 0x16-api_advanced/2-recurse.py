#!/usr/bin/python3
"""
Recursive function that queries the Reddit API and returns a list
    containing the titles of all hot articles for a given subreddit.
    If no results are found, returns None.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """returning top post titles recursively"""
    user_agent = {'User-Agent': 'api_advanced-project'}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    parameters = {'after': after} if after else {}

    results = requests.get(url, params=parameters, headers=user_agent, allow_redirects=False)

    if results.status_code == 200:
        after_data = results.json().get("data").get("after")
        if after_data is not None:
            hot_list = recurse(subreddit, hot_list, after=after_data)
        all_titles = results.json().get("data").get("children")
        for title_ in all_titles:
            hot_list.append(title_.get("data").get("title"))
        return hot_list
    else:
        return None
