#!/usr/bin/python3
"""
function that queries the Reddit API and prints the titles of the first
10 hot posts listed for a given subreddit
"""

from requests import get


def top_ten(subreddit):
    """
    prints the titles of the first 10 hot posts listed for a given subreddit
    """

    if subreddit is None or not isinstance(subreddit, str):
        print("Invalid subreddit.")
        return

    user_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    params = {'limit': 10}
    url = f'https://www.reddit.com/r/{subreddit}/hot/.json'

    try:
        response = get(url, headers=user_agent, params=params)
        response.raise_for_status()
        results = response.json()

        my_data = results.get('data', {}).get('children', [])

        if not my_data:
            print(f"No posts found for subreddit '{subreddit}'.")
            return

        print(f"Top 10 hot posts for subreddit '{subreddit}':")
        for post in my_data:
            print(post.get('data', {}).get('title'))

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
