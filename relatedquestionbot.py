import praw

r = praw.Reddit("Related-Question Monitor v1.0 by /u/teejas"
                "https://github.com/teejas/reddit-bots/")

r.login(disable_warning=True)
already_done = []
searchReddit = raw_input("Enter the subreddit you'd like to search: ")
prawWords = ["" for x in range(10)]
word = ""
counter = 0
while word != "done":
    word = raw_input("Enter the words you want to search for: (enter 'done' when done)")
    prawWords[counter] = word
    counter += 1

i = 0
while i < 10:
    subreddit = r.get_subreddit(searchReddit)
    for submission in subreddit.get_hot(limit = 10):
        op_text = submission.selftext.lower()
        has_praw = any(string in op_text for string in prawWords)
        # Test for questions related to the PRAW words
        if has_praw:
            msg = "[Related threads](%s)" % submission.short_link
            print("Thread", msg)
            #   already_done.append(submission.id)
    break
