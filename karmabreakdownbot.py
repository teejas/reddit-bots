import praw

user_agent = ("Karma Breakdown v1.0 by /u/teejas"
            "https://github.com/teejas/reddit-bots/")
                
r = praw.Reddit(user_agent = user_agent)
user_name = "_Daimon_"
user = r.get_redditor(user_name)
gen = user.get_submitted()
karma_by_subreddit = {}
for thing in gen:
    subreddit = thing.subreddit.display_name
    karma_by_subreddit[subreddit] = (karma_by_subreddit.get(subreddit, 0) + thing.score)

import pprint

pprint.pprint(karma_by_subreddit)