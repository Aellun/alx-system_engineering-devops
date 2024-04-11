#!/usr/bin/python3
"""function that queries the Reddit API and returns a list containing
the titles of all hot articles for a given subreddit.
If no results are found for the given subreddit,
the function should return None."""
import requests


def recurse(subreddit, hot_list=[]):
    """
    Recursively fetches all hot articles for a given subreddit
    and returns a list of their titles.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'MyBot/1.0'}
    # Maximum limit per request
    params = {'limit': 100}

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']

        if not posts:
            # No more posts to fetch, return the hot_list
            return hot_list

        # Extract titles and append to hot_list
        hot_list.extend([post['data']['title'] for post in posts])

        # Recursive call to fetch next page
        last_post_id = posts[-1]['data']['id']
        return recurse(subreddit, hot_list)

    else:
        # Invalid subreddit or other error
        return None
