#!/usr/bin/python3

from requests import get
"""function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit."""


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts listed for a given subreddit.
    """

    if subreddit is None or not isinstance(subreddit, str):
        print("None")
        return

    user_agent = {'User-agent': 'Google Chrome Version 24.0.6367.37'}
    params = {'limit': 10}
    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)

    response = get(url, headers=user_agent, params=params)
    results = response.json()

    try:
        my_data = results.get('data').get('children')

        for i in my_data:
            print(i.get('data').get('title'))

    except Exception:
        print("None")
