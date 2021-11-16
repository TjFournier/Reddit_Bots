import praw
import time
reddit = praw.reddit('bot0',user_agent='cs_40')

url = "https://www.reddit.com/r/funny/comments/3g1jfi/buttons/"
submission = reddit.submission(url=url)


for top_level_comment in submission.comments:
    print(top_level_comment.body)
