import tweepy  # make sure to install tweepy first
import time
from datetime import datetime, date
from random import choice


class Bot:
    def __init__(self):
        # Sign up for a Twitter Developer Account to get the CONSUMER_KEY, CONSUMER_SECRET, KEY, and SECRET
        # https://developer.twitter.com/en/apply-for-access
        self.auth = tweepy.OAuthHandler('CONSUMER_KEY', 'CONSUMER_SECRET')
        self.auth.set_access_token('KEY', 'SECRET')
        self.api = tweepy.API(self.auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
        self.user = self.api.me()
        self.search_terms = ['pythonlearning', '100DaysOfCode', 'DEVCommunity', 'python', 'python3', 'programming', 
        'coding', 'codenewbies', 'pythonhelp', 'pythonprogramming', 'developers', 'programmer', 'coder', 'code', 
        'codingskills', 'algorithm', 'pythonguides', 'pythondeveloper', 'codingisfun', 'github', 'opensource']
        self.number_of_tweets = 0

    def retweet(self):
        hashtag = choice(self.search_terms)
        for tweet in tweepy.Cursor(self.api.search, hashtag).items(3):  # maximum of 3 retweets for selected hashtag
            try:
                self.number_of_tweets += 1
                print('NUMBER OF TWEEETS:', self.number_of_tweets)
                print(f'HASHTAG: #{hashtag}')
                print(f'DATE: {date.today()}')
                print(f'TIME: {datetime.now().strftime("%H:%M:%S")}')
                print(tweet.text)
                tweet.retweet()
                time.sleep(120)
            except tweepy.TweepError as e:
                print(e.reason)
            except StopIteration:
                break


bot = Bot()
while True:
    bot.retweet()
