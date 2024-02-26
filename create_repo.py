import sys
from github import Github
import os
import requests
import json
token = os.getenv('GH_TOKEN')
#g = Github(token)
g = Github(base_url="https://api.github.com/repos/mybhadre/test-oic", login_or_token='token')
# Creating a new repository
new_repo = "mybhadre/demo-oic"
user = g.get_user()
print(user)

repo = user.create_repo(new_repo)
#print(f"Repository '{new_repo}' created successfully!")
reponame = "mybhadre/test-oic"
#token = "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"
#GITHUB_API_URL = "https://api.github.com/repos/mybhadre/test-oic"
#headers = {"Authorization": "token {}".format(token)}
#data = {"name": "{}".format(reponame)}
#print(headers)
#print(data)

#r = requests.post(GITHUB_API_URL +"mybhadre" + "", data=json.dumps(data), headers=headers)
#print(r)
