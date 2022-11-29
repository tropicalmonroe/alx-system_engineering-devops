#!/usr/bin/python3
""" func that query reddit API """
import requests


def top_ten(subreddit):
    """ prints redit trending 10 topics listed for a given subreddit
    Args:
    account to search
    """
    if subreddit is None or type(subreddit) is not str:
        return 0
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    User_Agent = 'AgentMEGO'
    header = {'User-Agent': User_Agent}
    with requests.Session() as res:
        data = res.get(url, headers=header)
        if data.status_code != 200:
            print(None)
            return
        data = data.json().get('data').get('children')
        for i in data[0:10]:
            print(i.get('data').get('title'))
