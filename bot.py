import praw
import random
import datetime
import time

# FIXME:
# copy your generate_comment function from the madlibs assignment here

madlibs = [
    "[BIDEN] is [DOING] [NOTHING] about the [COVID] vaccine rates in the [US].  [BIDEN] [SHOULD] have [MORE] [REWARDS] for getting a vaccine.",
    "[BIDEN]'s Infrastructure [DEAL] was [PASSED]. [GOVT] now have to decide which [STATES] get the money.", 
    "[BIDEN] needs a nap. The [OLD] man clearly missed it [TODAY]. Next time he falls asleep there might be [CONSEQ].",
    "[TRUMP] and [BIDEN] argue about topics. This displays the state of the [US], where two [OLD] men argue.",
    "[BIDEN] and [TRUMP] have [ANNOUNCED] they wil have a pay-per-view boxing match. The [WINNER] will fight [UTUBE].",
    "[BIDEN] has [ANNOUNCED] he will fight [CONGRESS]. The [WINNER] will be [PRESIDENT] for the week."
    ]

replacements = {
    'BIDEN' : ['Biden', 'President Biden', 'The President', 'Preseident Joe Biden'],
    'DOING' : ['doing', 'acomplishing', 'achieving'],
    'NOTHING' : ['nothing', 'nought', 'naught'],
    'COVID' : ['Covid', 'Covid-19', 'Corona Virus',],
    'MORE'  : ['more', 'added', 'increased'],
    'US' : ['US', 'USA', 'United States', 'United States of America'],
    'REWARDS' : ['rewards', 'perks', 'like'],
    'DEAL' : ['deal', 'bill'],
    'SHOULD' : ['should', 'must', 'need to'],
    'STATES' : ['States', 'State governments'],
    'PASSED' : ['passed', 'authorized', 'approved', 'confirmed'],
    'GOVT' : ['The Government', 'The US Government', 'The United States Government'],
    'OLD' : [ 'old', 'ancient', 'aged', 'elderly'],
    'CONSEQ' : ['consequences', 'ramifications'],
    'TODAY' : ['today', 'this time'],
    'TRUMP' : ['Trump', 'Donald Trump', 'former President Trump'],
    'ANNOUNCED' : ['announced', 'released', 'declared'],
    'WINNER' : ['winner', 'victor'],
    'UTUBE' : ['Jake Paul', 'Logan Paul', 'KSI'],
    'CONGRESS' : ['all of Congress', 'the Democrats', 'the Republicans', 'Kamala Harris'],
    'PRESIDENT' : ['the President', 'the POTUS', 'the President of the US', 'the President of the United States']
    }



def generate_comment():
    '''
    This function generates random comments according to the patterns specified in the `madlibs` variable.

    To implement this function, you should:
    1. Randomly select a string from the madlibs list.
    2. For each word contained in square brackets `[]`:
        Replace that word with a randomly selected word from the corresponding entry in the `replacements` dictionary.
    3. Return the resulting string.

    For example, if we randomly seleected the madlib "I [LOVE] [PYTHON]",
    then the function might return "I like Python" or "I adore Programming".
    Notice that the word "Programming" is incorrectly capitalized in the second sentence.
    You do not have to worry about making the output grammatically correct inside this function.
    '''

    s = random.choice(madlibs)
    for k in replacements.keys():
        s = s.replace('['+k+']',random.choice(replacements[k]))
    return s

# FIXME:
# connect to reddit 
reddit = praw.Reddit('Bidenbot0',user_agent='cs_40')

# FIXME:
# select a "home" submission in the /r/BotTown subreddit to post to,
# and put the url below
submission_url = 'https://www.reddit.com/r/BotTown2/comments/r0yi9l/main_discussion_thread/'
submission = reddit.submission(url=submission_url)

# each iteration of this loop will post a single comment;
# since this loop runs forever, your bot will continue posting comments forever;
# (this is what makes it a deamon);
# recall that you can press CTRL-C in the terminal to stop your bot
#
# HINT:
# while you are writing and debugging your code, 
# you probably don't want it to run in an infinite loop;
# you can change this while loop to an if statement to make the code run only once
if True:

    # printing the current time will help make the output messages more informative
    # since things on reddit vary with time
    print()
    print('new iteration at:',datetime.datetime.now())
    print('submission.title=',submission.title)
    print('submission.url=',submission.url)

    # FIXME (task 0): get a list of all of the comments in the submission
    # HINT: this requires using the .list() and the .replace_more() functions
    all_comments = []
    submission.comments.replace_more(limit=None)
    all_comments = submission.comments.list()

    # HINT: 
    # we need to make sure that our code is working correctly,
    # and you should not move on from one task to the next until you are 100% sure that 
    # the previous task is working;
    # in general, the way to check if a task is working is to print out information 
    # about the results of that task, 
    # and manually inspect that information to ensure it is correct; 
    # in this specific case, you should check the length of the all_comments variable,
    # and manually ensure that the printed length is the same as the length displayed on reddit;
    # if it's not, then there are some comments that you are not correctly identifying,
    # and you need to figure out which comments those are and how to include them.
    print('len(all_comments)=',len(all_comments))

    # FIXME (task 1): filter all_comments to remove comments that were generated by your bot
    # HINT: 
    # use a for loop to loop over each comment in all_comments,
    # and an if statement to check whether the comment is authored by you or not
    not_my_comments = []
    for comment in all_comments:
         print('comment.author=', comment.author)
         print('type(comment.author)=',type(comment.author))
         if str(comment.author) != 'babysFirsTb0t':
             not_my_comments.append(comment)

    # HINT:
    # checking if this code is working is a bit more complicated than in the previous tasks;
    # reddit does not directly provide the number of comments in a submission
    # that were not gerenated by your bot,
    # but you can still check this number manually by subtracting the number
    # of comments you know you've posted from the number above;
    # you can use comments that you post manually while logged into your bot to know 
    # how many comments there should be. 
    print('len(not_my_comments)=',len(not_my_comments))

    # if the length of your all_comments and not_my_comments lists are the same,
    # then that means you have not posted any comments in the current submission;
    # (your bot may have posted comments in other submissions);
    # your bot will behave differently depending on whether it's posted a comment or not
    has_not_commented = len(not_my_comments) == len(all_comments)
    comments_without_replies = []
    if has_not_commented:
        text = generate_comment()
        submission.reply(text)
    
        
        # FIXME (task 2)
        # if you have not made any comment in the thread, then post a top level comment
        #
        # HINT:
        # use the generate_comment() function to create the text,
        # and the .reply() function to post it to reddit;
        # a top level comment is created when you reply to a post instead of a message
        

    else:
        for comments in not_my_comments:
            havent_replied = True
            for replies in comments.replies:
                try:
                    if str(replies.author) == 'babysFirsTb0t':
                        havent_replied = False
                        break
                except NameError:
                    pass

            if havent_replied:
                comments_without_replies.append(replies)
        # FIXME (task 3): filter the not_my_comments list to also remove comments that 
        # you've already replied to
        # HINT:
        # there are many ways to accomplish this, but my solution uses two nested for loops
        # the outer for loop loops over not_my_comments,
        # and the inner for loop loops over all the replies of the current comment from the outer loop,
        # and then an if statement checks whether the comment is authored by you or not
       
        # HINT:
        # this is the most difficult of the tasks,
        # and so you will have to be careful to check that this code is in fact working correctly
        print('len(comments_without_replies)=',len(comments_without_replies))

        # FIXME (task 4): randomly select a comment from the comments_without_replies list,
        # and reply to that comment
        #
        # HINT:
        # use the generate_comment() function to create the text,
        # and the .reply() function to post it to reddit;
        # these will not be top-level comments;
        # so they will not be replies to a post but replies to a message
        comment = random.choice(comments_without_replies)
        try:
            comment.reply(generate_comment())
        except praw.exceptions.APIexceptions:
            print('not replying to a comment that was deleted')

    # FIXME (task 5): select a new submission for the next iteration;
    # your newly selected submission should be randomly selected from the 5 hottest submissions
    
    submission = random.choice(comments_without_replies)
    for submission in reddit.subreddit('https://www.reddit.com/r/BotTown2/').hot(limit=5):

    # We sleep just for 1 second at the end of the while loop.
    # This doesn't avoid rate limiting
    # (since we're not sleeping for a long period of time),
    # but it does make the program's output more readable.
        time.sleep(10)


print('='*40)
print('Bot Finished')
print('='*40)