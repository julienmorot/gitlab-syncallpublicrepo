#!/usr/bin/env python3

# apt-get install python3-git (ou pip)
import requests
import json
import os
from git import Repo
import git

API_URL = 'https://gitlab.com/api/v4'
USER = 'julienmorot'
PROJECTS_PATH = '/data/gitlab/projects'

r = requests.get(API_URL + '/users/'+USER+'/projects?simple=true&owned=true')
json=r.json()

for repo in json:
    repo_url = repo['http_url_to_repo']
    repo_path = repo['path']
    local_path = PROJECTS_PATH + '/' + repo_path
    print(local_path)

    try:
        if os.path.isdir(local_path):
            repo = git.Repo(local_path)
            repo.remotes.origin.pull()
        else:
            repo = Repo.clone_from(repo_url, local_path)
    except git.exc.InvalidGitRepositoryError:
        repo = Repo.clone_from(repo_url, local_path)
