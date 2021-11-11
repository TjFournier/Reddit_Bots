import praw

reddit = praw.reddit("bot")

url = "https://www.reddit.com/r/funny/comments/3g1jfi/buttons/"
submission = reddit.submission(url=url)
'''
for top_level_comment in submission.comments:
    print(top_level_comment.body)
'''