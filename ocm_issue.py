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
