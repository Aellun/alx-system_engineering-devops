#!/usr/bin/python3
"""unction that queries the Reddit API, parses the title of
all hot articles, and prints a sorted count of given keywords
(case-insensitive, delimited by spaces. """
import requests


def count_words(subreddit, word_list, counts=None):
    """
    Recursively counts the occurrences of keywords in the titles
    of hot articles for a given subreddit and prints the counts
    sorted in descending order by count
    and alphabetically for keywords with the same count.
    """
    if counts is None:
        counts = {}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'MyBot/1.0'}
    # Maximum limit per request
    params = {'limit': 100}

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']

        if not posts:
            sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_counts:
                print(f"{word}: {count}")
            return

        # Count occurrences of words in titles
        for post in posts:
            title = post['data']['title'].lower()
            for word in word_list:
                if title.count(word.lower()) > 0:
                    counts[word.lower()] = counts.get(word.lower(), 0) + title.count(word.lower())

        # Recursive call to fetch next page
        last_post_id = posts[-1]['data']['id']
        return count_words(subreddit, word_list, counts)

    # Invalid subreddit or other error
    else:
        return None
