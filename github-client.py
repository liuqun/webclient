#!/usr/bin/env python3
# encoding: utf-8
from github import Github


def register_new_access_token(token_note: str) -> str:
    """通过交互式脚本远程注册一个新的 github 个人访问令牌

    :param token_note:
    """
    username = 'liuqun'
    import getpass
    password = getpass.getpass()
    url = 'https://api.github.com/authorizations'
    my_note = token_note
    post_data = {'scopes': ['repo'], 'note': my_note}
    import json
    import requests
    response = requests.post(
        url,
        auth=(username, password),
        data=json.dumps(post_data),
    )
    # print('API response:', response.text)
    token = response.json()['token']
    # print('Your OAuth token is', token)
    return token


if '__main__' == __name__:
    import datetime
    now = datetime.datetime.now()
    token_note = now.strftime("My API token %Y-%m-%d %H:%M:%S.%f")
    access_token = None
    if not access_token:
        access_token = register_new_access_token(token_note)

    repo_owner = 'liuqun'
    repo_name = 'njit8021xclient'

    try:
        client = Github(access_token, per_page=100)
        user = client.get_user(repo_owner)
        repo = user.get_repo(repo_name)
        stargazers = [s for s in repo.get_stargazers()]
        print('Repo', repo_name, 'have', len(stargazers), 'stargazers:')
        for persion in stargazers:
            print(persion.login)
    except Exception as e:
        print(e)
