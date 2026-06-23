import os
import praw
import pandas as pd
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=os.getenv("REDDIT_USER_AGENT")
)

post_url = input("Paste the Reddit post URL: ")

submission = reddit.submission(url=post_url)

# Loads visible comments and avoids expanding too many hidden "more comments" blocks.
submission.comments.replace_more(limit=0)

comments_data = []

for comment in submission.comments.list():
    comments_data.append({
        "post_title": submission.title,
        "post_id": submission.id,
        "comment_id": comment.id,
        "author": str(comment.author) if comment.author else "[deleted]",
        "body": comment.body,
        "score": comment.score,
        "created_utc": datetime.fromtimestamp(comment.created_utc),
        "permalink": "https://www.reddit.com" + comment.permalink,
        "subreddit": str(submission.subreddit)
    })

df = pd.DataFrame(comments_data)
df.to_csv("reddit_comments.csv", index=False, encoding="utf-8-sig")

print(f"Saved {len(df)} comments to reddit_comments.csv")
