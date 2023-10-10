#!/usr/bin/python3
"""
100-count
"""

import requests

def count_words(subreddit, word_list, after=None, word_count={}):
    """
    Recursively queries the Reddit API, parses the titles of hot articles, and prints a sorted count of given keywords.

    Args:
        subreddit (str): The subreddit name.
        word_list (list): A list of keywords to count.
        after (str): A parameter used for pagination (default is None).
        word_count (dict): A dictionary to store word counts (default is an empty dictionary).

    Returns:
        None
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100&after={after}"
    headers = {'User-Agent': 'MyBot/1.0'}
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        
        for post in posts:
            title = post['data']['title'].lower()
            for word in word_list:
                word = word.lower()
                if word in title and f"{word}." not in title and f"{word}!" not in title and f"{word}_" not in title:
                    word_count[word] = word_count.get(word, 0) + 1
        
        after = data['data']['after']
        
        if after is not None:
            return count_words(subreddit, word_list, after, word_count)
        else:
            sorted_counts = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_counts:
                print(f"{word}: {count}")
    else:
        return None

if __name__ == '__main__':
    import sys
    
    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'".format(sys.argv[0]))
    else:
        subreddit = sys.argv[1]
        word_list = sys.argv[2].split()
        count_words(subreddit, word_list)
