import config
import os, sys
import requests, json
from getpass import getpass

from config import REPOS, USERS, GH_BASE_URL, MY_USERNAME, ORG_NAME

'''
    Small script to add lots of users to lots of repos automatically. 
    Saves some time! 
    Just edit the config.py file to your needs.

    PASS GitHub password as argument ()
'''

# def get_user_id(username):
#     r = requests.get("{}/users/{}".format(GH_BASE_URL, username))
#     data = json.loads(r.text)
#     print(username + "::" + str(data['id']))
#     return data['id']

def addUserToRepo(my_username, my_pass, username, repo):
    cmd = "curl -s -u '{}:{}' -H 'Accept: application/vnd.github.v3+json' -X PUT -d '' '{}/repos/{}/{}/collaborators/{}'".format(my_username, my_pass, GH_BASE_URL, ORG_NAME, repo, username)
    r = os.popen(cmd).read()

    msg = json.loads(r)["message"]
    if msg == "Bad credentials":
        print("!!!!! Bad credentials")
        sys.exit()
    elif msg == "Not found":
        print("!!!!! User {} could not be added".format(username))
    else:
        print("..... OK")

if __name__ == "__main__":
    my_pass = getpass()
    for user in USERS:
        for repo in REPOS:
            print("Adding " + user + " to " + repo)
            addUserToRepo(MY_USERNAME, my_pass, user, repo)
        print("-------------")