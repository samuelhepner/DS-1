# import important libraries
import praw

reddit = praw.Reddit(
    client_id='fpc5FKLaEpjoyw',
    client_secret='h1EhwL6_wf2AS6RxMT6_Gt1ofY4',
    user_agent='BWPostHere/0.1 by u/BWPostHere',
    username='BWPostHere',
    password='Passlock1'
)

print(reddit.read_only)
