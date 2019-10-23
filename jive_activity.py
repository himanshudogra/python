import requests
import argparse
import base64
import getpass
import json


def getUrl(serverbase,url,user):
    if url is None:
        return serverbase+"/api/core/v3/people/email/"+user
    else:
        return url


def getActivityUrlForJiveUser(serverbase,user,username,password):
    url = serverbase+"/api/core/v3/people/email/"+user
    usrPass = username+":"+password
    b64Val = base64.b64encode(usrPass)
    response = requests.get(url,headers={"Authorization":"Basic "+b64Val})
    activity_url = response.json()['resources']['activity']['ref']
    return activity_url


def getActivitiesForJiveUser(url,username,password):
    usrPass = username+":"+password
    b64Val = base64.b64encode(usrPass)
    response = requests.get(url,headers={"Authorization":"Basic "+b64Val})
    response_json = response.json()
    print (json.dumps(response_json,indent=2))
    if 'links' in response_json:
        getActivitiesForJiveUser(response_json['links']['next'],username,password)
    


class Password(argparse.Action):
    def __call__(self, parser, namespace, values, option_string):
        if values is None:
            values = getpass.getpass()

        setattr(namespace, self.dest, values)




parser = argparse.ArgumentParser(description='Script to fetch activities for a user ')
parser.add_argument('Server',metavar='server',type=str,help='Server  Base URL')
parser.add_argument('UserEmail',metavar='useremail',type=str,help='User Email to look for eg. upasana')
parser.add_argument('UserName',metavar='username',type=str,help='User name')
parser.add_argument('After',metavar='after',type=str,help="After time")
parser.add_argument('-p', action=Password, nargs='?', dest='password', help='Enter your password')


args = parser.parse_args()
useremail=args.UserEmail
username=args.UserName
password=args.password
server=args.Server
after=args.After

activity_url=getActivityUrlForJiveUser(server,useremail,username,password)
getActivitiesForJiveUser(activity_url+"?count=100&after="+after,username,password)
