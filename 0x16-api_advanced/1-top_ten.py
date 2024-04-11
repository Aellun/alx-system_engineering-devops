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

    user_agent = {'User-agent': 'MyBot/1.0'}
    params = {'limit': 10}
    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)

    try:
        response = get(url, headers=user_agent, params=params)
        response.raise_for_status()  # Raise an exception for any HTTP errors
        results = response.json()
        my_data = results.get('data').get('children')

        for post in my_data:
            print(post.get('data').get('title'))

    except Exception as e:
        print("Error:", e)
