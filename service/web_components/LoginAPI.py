from . import *
from flask import Flask, request, jsonify
from linkedin import linkedin
from linkedin.linkedin import PERMISSIONS
import json
import tweepy
from SMCGlibrary.Twitter import Twitter
from SMCGlibrary.Facebook import Facebook
from SMCGlibrary.LinkedIn import LinkedIn


class LoginAPI(Component):
    def __init__(self, env: Environment):
        super().__init__(env, '/api/v1/Login', LoginAPI, ['POST'])
        self.env = env

    def view(self):
        data = request.get_json()
        if data['platform'] == "twitter":
            self.twitterAuth(data)
        elif data['platform'] == "facebook":
            self.facebookAuth(data)
        elif data['platform'] == "linkedin":
            self.linkedinAuth(data)
        return {"status":0}

    def twitterAuth(self, data):
        access_token = data['access_token']
        access_token_secret = data['access_token_secret']
        auth_dict = {
            'access_token': access_token,
            'access_token_secret': access_token_secret,
            'consumer_key': "EzoH0w73hC3naY84U6NBHZHyz",
            'consumer_secret': "qjFQ5WPxqJD7C0JZtMiORkzbhYAXjNNfX0WyMdx5GWz1IiZxFw"
        }
        json_object = json.dumps(auth_dict, indent=4)
        with open('twitter_auth.json', 'w') as outfile:
            outfile.write(json_object)

    def facebookAuth(self, data):
        userAccessToken = data['userAccessToken']
        pageAccessToken = data['pageAccessToken']
        pageId = data['pageId']
        auth_dict = {
            'userAccessToken': userAccessToken,
            'pageAccessToken': pageAccessToken,
            'pageId': pageId
        }
        json_object = json.dumps(auth_dict, indent=4)

        with open('facebook_auth.json', 'w') as outfile:
            outfile.write(json_object)

    def linkedinAuth(self,data):
        data = request.get_json()
        code = data['code']
        APPLICATION_KEY = '78sme225fsy5by'
        APPLICATION_SECRET = 'J3xg14qRTV87viVq'
        RETURN_URL = 'http://localhost:8888'
        authentication = linkedin.LinkedInAuthentication(
            APPLICATION_KEY,
            APPLICATION_SECRET,
            RETURN_URL,
            linkedin.PERMISSIONS.enums.values()
        )
        authentication.authorization_code = code
        result = authentication.get_access_token()
        profile = authentication.get_profile(selectors=['id', 'first-name', 'last-name'])
        auth_dict = {
            "access_token": result.access_token,
            "APPLICATION_KEY": '78sme225fsy5by',
            "APPLICATION_SECRET": 'J3xg14qRTV87viVq',
            "profile": profile
        }
        json_object = json.dumps(auth_dict, indent=4)
        with open("linkedin_auth.json", 'w') as outfile:
            outfile.write(json_object)


