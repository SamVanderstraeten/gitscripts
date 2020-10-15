import config
import os, sys
import requests, json

from config import REPOS, USERS

GH_BASE_URL = "https://api.github.com"
MY_USERNAME = "SamVanderstraeten"

def get_user_id(username):
    r = requests.get("{}/users/{}".format(GH_BASE_URL, username))
    data = json.loads(r.text)
    return data['id']

def addUserToRepo(my_id, my_pass, userid, repo):
    os.popen("curl -i -u '{}:{}' -X PUT -d '' 'https://api.github.com/repos/{}/{}/collaborators/{}'".format(MY_USERNAME, my_pass, my_id, repo, userid)).read()

if __name__ == "__main__":
    my_id = get_user_id(MY_USERNAME)
    my_pass = sys.argv[0]
    for user in USERS:
        userid = get_user_id(user)
        for repo in REPOS:
            print("Adding " + user + " to " + repo)
            addUserToRepo(my_id, my_pass, userid, repo)
        print("-------------")