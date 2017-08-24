import praw
import config

def bot_login():
	return praw.Reddit(username = config.username,
				passsword = config.password,
				client_id = config.client_id,
				client_secret = config.client_secret,
				user_agent = "LyricTalkBot v 1.0")

def run_bot(r):
	for comment in r.subreddit('LyricTalk').comments(limits=25):
		if "test" in comment.body:
		print("donion rings")

login_instance = bot_login()
run_bot(login_instance)