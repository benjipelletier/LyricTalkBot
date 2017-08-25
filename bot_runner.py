import urllib
import requests
import json
import praw
import config

def bot_login():
	return praw.Reddit(username = config.username,
					   passsword = config.password,
					   client_id = config.client_id,
					   client_secret = config.client_secret,
					   user_agent = "LyricTalkBot v 1.0")

def run_bot(r):
	for comment in r.subreddit('LyricTalk').stream.comments():
		print(comment.body)
		query = urllib.urlencode({'q': comment.body})
		r = requests.get('https://api.genius.com/search?' + query, headers={'Authorization': 'Bearer ' + config.access_token})
		comment.reply("KEK")
		print(r.json())


login_instance = bot_login()
run_bot(login_instance)