import praw
import pprint

# FIXME:
# login to reddit with your bot's credentials;
# recall that this requires creating a praw.ini file
# 
# WARNING:
# If you include any credential information in your final submission,
# you will receive NEGATIVE POINTS on your lab!!!
reddit = praw.Reddit('Bidenbot0',user_agent='cs_40')

# connect to the "Main Discussion Thread" reddit submission
submission = reddit.submission(url='https://www.reddit.com/r/BotTown2/comments/r0yi9l/main_discussion_thread/')

# FIXME:
# Click the "view more comments" buttons in the reddit submission in order to download all comments.
#
# HINT:
# This step takes a long time.
# It takes the PRAW library about 1 second to "click" a link,
# and so it takes about 1 minute total to click all of them.
# I recommend saving this step for last since it will slow down your ability to run the steps below considerably.
# Get those working, then come back here and get this working.
submission.comments.replace_more(limit=None)

# FIXME:
# Loop through all the top level comments to calculate:
# 1. The total number of non-deleted top level comments,
# 2. The total number of deleted top level comments,
# 3. The total number of comments sent by each user.
#    You should use a dictionary where the keys are the username and the values are the total number of comments.

redditors = {}
authors = []
nondelcom = 0
delcom = 0
numauthor = 0

toplvlcom = list(submission.comments)
for i in range(len(toplvlcom)):
    numauthor = 0
    author = submission.comments[i].author
    if author:
        nondelcom += 1
        authors.append(author)
        for a in authors:
            if author == a:
                numauthor += 1
    else:
        delcom += 1
    if author:
        redditors[author] = numauthor

print('='*40)
print('top level comments')
print('='*40)
print('nondeleted _comments=',nondelcom)
print('deleted_comments=',delcom)
pprint.pprint(redditors)


# FIXME:
# Repeat the calculations above,
# but do it for ALL comments,
# not just top level comments.

redditors = {}
authors = []
nondelcom = 0
delcom = 0
numauthor = 0

allcom = submission.comments.list()
for comment in submission.comments.list():
    author = comment.author
    numauthor = 0
    if author:
        nondelcom += 1
        authors.append(author)
        for a in authors:
            if author == a:
                numauthor += 1
    else:
        delcom += 1
    if author:
        redditors[author] = numauthor

print('='*40)
print('top level comments')
print('='*40)
print('nondeleted _comments=',nondelcom)
print('deleted_comments=',delcom)
pprint.pprint(redditors)

