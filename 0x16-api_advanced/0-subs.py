#!/usr/bin/python3
"""
function that queries the Reddit API and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit. return 0
"""

from requests import get

def number_of_subscribers(subreddit):
    """
    number of subscribers for a given subreddit
    """

    if subreddit is None or not isinstance(subreddit, str):
        return 0

    user_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)

    try:
        response = get(url, headers=user_agent)
        response.raise_for_status()
        results = response.json()
        return results.get('data').get('subscribers')

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

    return 0

