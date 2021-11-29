import random
import praw
import time


from praw.reddit import Comment
'''
This lab has three tasks.

TASK 1:
Implement the `generate_comment` function below.

TASK 2:
Redefine the `madlibs` and `replacements` variables so that the generated comments are what you want your reddit bot to say.
You must have at least 6 different madlibs.
Each madlib should be 2-5 sentences long and have at least 5 [REPLACEMENT] [WORDS].

TASK 3:
Use your `generate_comment` function to post at least 100 messages to the `Practice posting messages here :)` submission, located at:
https://old.reddit.com/r/BotTown/comments/qr05je/practice_posting_messages_here/
You should have at least 10 top level comments and at least 10 replies to comments (but it's okay if they're all replies to the same comment).

SUBMISSION:
Upload your bot's name and your `madlib.py` file to sakai.
'''

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


reddit = praw.Reddit('Bidenbot0',user_agent='cs_40')
url = 'https://www.reddit.com/r/BotTown2/comments/r0yi9l/main_discussion_thread/'
submission=reddit.submission(url=url)


for i in range(50):
    submission.reply(generate_comment())
    time.sleep(60)

for i in range(50):
    submission.comments[i].reply(generate_comment())
    time.sleep(60)

print('='*40)
print('Finished')
print('='*40)