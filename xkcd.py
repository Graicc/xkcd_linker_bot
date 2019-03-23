import praw
import re
from time import sleep

f=open("DONTUPLOAD.txt", "r")
f.readline(1) # This made it work and I don't know why.
r=praw.Reddit(client_id=f.readline().strip(), client_secret=f.readline().strip(), user_agent='xkcdlinkerbot:v0.1 (by /u/Graic628)', username='xkcd_linker_bot', password=f.readline().strip()) 

replied_to=[]

while True:
	for comment in r.subreddit('test').stream.comments():
		print(comment.body)
		if re.match(r'xkcd:(\d+)',comment.body, re.IGNORECASE):
			if comment.id not in replied_to: 
				replyTextFull = ""
				for m in re.finditer(r'xkcd:(\d+)',comment.body, re.IGNORECASE):
					num=m.group(1)
					replyText="\n[XKCD "+num+"](http://xkcd.com/"+num+")"+" | [Mobile](http://m.xkcd.com/"+num+")"
					replyTextFull+=replyText
					print(replyText)
				comment.reply(replyTextFull)
				replied_to.append(comment.id)
	sleep(1)
