import requests
import json

def GetRepos(id):
    result=""
    repos = requests.get("https://api.github.com/users/"+id+"/repos").json()
    for x in repos:
        commits = requests.get("https://api.github.com/repos/"+id+"/"+x["name"]+"/commits").json()
        result+="Repo: "+x["name"]+" Number of commits: "+str(len(commits))+"\n"
    return result