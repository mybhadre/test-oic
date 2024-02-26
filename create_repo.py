import sys
from github import Github
import os
import requests
import json
token = os.getenv('GITHUB_TOKEN')
g = Github(token)
# Creating a new repository
new_repo = "mybhadre/demo-oic"
user = g.get_user()
repo1 = user.create_repo(new_repo)
print(f"Repository '{new_repo}' created successfully!")
