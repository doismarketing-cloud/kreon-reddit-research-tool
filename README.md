# Kreon Reddit Research Tool

This is a personal, non-commercial Python research tool that uses the Reddit Data API to analyze public Reddit comments from selected posts and subreddits.

The purpose of this tool is market research and content analysis.

## What the tool does

- Reads public Reddit posts and comments.
- Extracts public comment text, score, date, subreddit, and permalink.
- Saves the results locally in a CSV file for analysis.

## What the tool does not do

- It does not post to Reddit.
- It does not vote.
- It does not send messages.
- It does not spam users.
- It does not automate engagement.
- It does not collect private information.
- It does not sell Reddit data.
- It does not store deleted or private content.

## API usage

The tool uses OAuth authentication, a clear User-Agent, and respects Reddit API rate limits.

## Environment variables

API credentials are stored locally in an `.env` file and are not included in this repository.
