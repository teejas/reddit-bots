def check_condition(comment):
    if comment.score > 100:
        return True
    else:
        return False
        
def bot_action(comment, respond):
    msg = "Dank"
    print(msg)
    if respond:
        head = "Hello, I am the Dank Comment Bot and I thought your comment was: "
        tail = "\n\nI am a bot, please provide feedback in my inbox /u/dank_bot0"
        comment.reply(head + msg + tail)

import praw
r = praw.Reddit("Dank Comment Bot v1.0 by /u/dank_bot0"
                "https://github.com/teejas/reddit-bots/")
r.login(disable_warning=True)
i = 0
for comment in praw.helpers.comment_stream(r, 'dankmemes'):
    if i == 10:
        break
    if check_condition(comment):
        bot_action(comment, True)
    i += 1