#!/usr/bin/python3
"""
2-recurse
"""

import requests

def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API and returns a list containing title

    Args:
        subreddit (str): The subreddit name.
        hot_list (list): A list to store the titles of hot articles
        after (str): A parameter used for pagination (default is None).

    Returns:
        list: A list containing the titles of hot articles, or None if no result
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100&after={after}"
    headers = {'User-Agent': 'MyBot/1.0'}
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            hot_list.append(post['data']['title'])
        
        after = data['data']['after']
        
        if after is not None:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        return None

if __name__ == '__main__':
    import sys
    
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        result = recurse(sys.argv[1])
        if result is not None:
            print(len(result))
        else:
            print("None")
