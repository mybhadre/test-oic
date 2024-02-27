import sys
from github import Github
import os
import requests
import json
#token = os.getenv('GH_TOKEN')
#g = Github(token)
#g = Github(base_url="https://api.github.com/api/v3", login_or_token='token')
# Creating a new repository
new_repo = "demo-oic"
#g = Github("mybhadre", "My@github24")

#user = g.get_user()
#print(user)
#login = user.login
#print(user) # will print 'AuthenticatedUser(login=<username_of_logged_in_user>)'
#print(login) 
reponame = "mybhadre/test-oic"
#repo = user.create_repo(new_repo)
#print(f"Repository '{new_repo}' created successfully!")
reponame = "mybhadre/demo-oic"
token = "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"
#token = os.getenv('GH_TOKEN')
g = Github(token)
user = "mybhadre"
print(user)
GITHUB_API_URL = "https://api.github.com/"
headers = {"Authorization": "token {}".format(token)}
data = {"name": "{}".format(reponame)}
print(headers)
print(data)

r = requests.post(GITHUB_API_URL + 'user/repos', data=json.dumps(data), auth=(user,token))
print(r)
