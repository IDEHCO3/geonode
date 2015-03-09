from django.db import models
from geonode.people.models import Profile

# Create your models here.
import tweepy

class TweeterStream(models.Model):

    name = models.CharField(max_length=150)
    status = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)

    center_x = models.FloatField()
    center_y = models.FloatField()
    zoom = models.IntegerField()

    creation_date = models.DateTimeField()
    init_date = models.DateTimeField()
    end_date = models.DateTimeField()

    userGeonode = models.ForeignKey(Profile)

class TweeterAuth:
    def __init__(self,consumer_key, consumer_secret, access_token, access_token_secret ):
        self.auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        self.auth.set_access_token(access_token, access_token_secret)

class TweeterAPI:
    def __init__(self, auth):
        self.api = tweepy.API(auth)

    def printa(self):
        public_tweets = self.api.home_timeline()
        for tweet in public_tweets:
            print (tweet.text)
            print(tweet.coordinates)
    def search(self, queryString):
        return self.api.search(queryString)