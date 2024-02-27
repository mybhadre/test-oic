import sys
from github import Github
import os
import requests
import json
#token = os.getenv('GH_TOKEN')
#g = Github(token)
#g = Github(base_url="https://api.github.com/api/v3", login_or_token='token')
# Creating a new repository
#new_repo = "demo-oic"

#user = g.get_user()
#print(user)
#login = user.login
#print(user) # will print 'AuthenticatedUser(login=<username_of_logged_in_user>)'
#print(login) 
#reponame = "mybhadre/test-oic"
#repo = user.create_repo(new_repo)
#print(f"Repository '{new_repo}' created successfully!")
reponame = "demo-oic2"

token = os.getenv('GH_TOKEN')
#g = Github(token)
username = 'mybhadre'


login = requests.get('https://api.github.com/search/repositories?q=github+api', auth=(username,token))
print(login)
GITHUB_API_URL = "https://api.github.com/"
headers = {"Authorization": "token {}".format(token)}
data = {"name": "{}".format(reponame)}
print(headers)
print(data)

r = requests.post(GITHUB_API_URL + 'user/repos', data=json.dumps(data), auth=(username,token))
print(r)
