#!/usr/bin/python3
"""
1-top_ten
"""

import requests

def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first

    Args:
        subreddit (str): The subreddit name.

    Returns:
        None
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'MyBot/1.0'}
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            print(post['data']['title'])
    else:
        print(None)

if __name__ == '__main__':
    import sys
    
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])
