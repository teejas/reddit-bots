import praw
import time

r = praw.Reddit("Related-Question Monitor v1.0 by /u/teejas"
                "https://github.com/teejas/reddit-bots/")

r.login(disable_warning=True)
already_done = []

