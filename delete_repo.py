import sys
from github import Github
import os
import requests
import json
token = os.getenv('GH_TOKEN')
g = Github(token)
user = g.get_user()
new_repo = "test-oic3"
repo = user.get_repo("test-oic3")
repo.delete()
