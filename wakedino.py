# by Carl Monk (@ForToffee)
# github.com/ForToffee/Robosapien
# cut and shut from my IoTBox code
# uses Tweepy

import tweepy
import robo
import time

# Consumer keys and access tokens, used for OAuth
consumer_key = 'YourKeyGoesHere'
consumer_secret = 'YourKeyGoesHere'
access_token = 'YourKeyGoesHere'
access_token_secret = 'YourKeyGoesHere'

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Creation of the actual interface, using authentication
api = tweepy.API(auth)

rs=robo.Robo(21)	#create Robo object for GPIO 21	
rs.send_code(0xB1)	#Reset

last_id = 0
def searchHashTag():
	global last_id
	ret = api.search(q='#wakedino',count=1, since_id=last_id)
	if len(ret) > 0:
		tweet = ret[0]
		print '===== START ====='
		print '{} (@{}) - {}\n{}'.format(tweet.author.name.encode('utf-8'), tweet.author.screen_name.encode('utf-8'), tweet.created_at, tweet.text.encode('utf-8'))
		print '====== END ======'
		last_id = tweet.id
		return True
	else:
		return False

elapsed = 0
while True:
	if searchHashTag():
		rs.send_code(0xCE)	#Roar
		elapsed = 0
	else:
		if elapsed > 120:
			rs.send_code(0xFB)	#NoOp
			elapsed = 0
		else:
			elapsed += 10

	time.sleep(10)
