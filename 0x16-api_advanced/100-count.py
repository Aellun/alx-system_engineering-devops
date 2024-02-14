import requests

def count_words(subreddit, word_list, after=None, counts=None):
    """queries the Reddit API, parses the title of all hot articles,
    and prints a sorted count of given keywords
    (case-insensitive, delimited by spaces. Javascript should count
    as javascript, but java should not)."""
    
    if after is None:
        counts = {}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {'after': after} if after else {}

    try:
        response = requests.get(url, params=params, allow_redirects=False, headers={'user-agent': 'bhalut'})
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)

        if response.status_code == 200:
            data = response.json()['data']
            after = data.get('after')
            
            for topic in data.get('children', []):
                for word in topic['data']['title'].split():
                    for i, target_word in enumerate(word_list):
                        if target_word.lower() == word.lower():
                            counts[target_word] = counts.get(target_word, 0) + 1

            if after is None:
                sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0].lower()))
                for word, count in sorted_counts:
                    print(f"{word.lower()}: {count}")

            else:
                count_words(subreddit, word_list, after, counts)

        elif response.status_code == 404:
            print(f"Subreddit '{subreddit}' not found.")
            return

        else:
            print(f"Error {response.status_code}: Unable to fetch posts for subreddit '{subreddit}'.")
            return

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return
