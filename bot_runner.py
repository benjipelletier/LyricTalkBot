import urllib
import requests
import json
import praw
import config

replyTemplate = ""

def bot_login():
	return praw.Reddit(username = config.username,
					   password = config.password,
					   client_id = config.client_id,
					   client_secret = config.client_secret,
					   user_agent = "LyricTalkBot v 1.0")

def run_bot(r):
	for comment in r.subreddit('LyricTalk').stream.comments():
		if comment.is_root:
			query = urllib.urlencode({'q': comment.body})
			req = requests.get('https://api.genius.com/search?' + query, headers={'Authorization': 'Bearer ' + config.access_token})
			resp = req.json()
			comment.refresh()
			print(comment.replies.list())
			if len(resp['response']['hits']) > 0 and len(comment.replies.list()) == 0:
				comment.reply('"' + comment.body + '"' + ' from [' + resp['response']['hits'][0]['result']['title'] + '](' + 
								resp['response']['hits'][0]['result']['url'] + ')' + ' by [' + 
								resp['response']['hits'][0]['result']['primary_artist']['name'] + '](' + 
								resp['response']['hits'][0]['result']['primary_artist']['image_url'] + ')')


login_instance = bot_login()
run_bot(login_instance)