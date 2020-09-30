import requests
import json

def GetRepos(id):
    repos = requests.get("https://api.github.com/users/"+id+"/repos").json()
    for x in repos:
        commits = requests.get("https://api.github.com/repos/"+id+"/"+x["name"]+"/commits").json()
        print("Repo: "+x["name"]+" Number of commits: "+str(len(commits)))

GetRepos("Eric-Fernandes-529")