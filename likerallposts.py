import praw

r = praw.Reddit("Like /r/all posts bot v1.0 by /u/teejas"
                "https://github.com/teejas/reddit-bots/")
                
r.login(disable_warning=True);

while True:
    subreddit = r.get_subreddit('all')
    for submission in subreddit.get_hot(limit=10):
        submission.upvote()
    break
    
