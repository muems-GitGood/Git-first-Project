import praw
import google.generativeai as genai
import sys

# ==========================================
# 1. SET YOUR API KEYS
# ==========================================

# Fill in your Reddit API credentials (see README.md)
REDDIT_CLIENT_ID = "YOUR_REDDIT_CLIENT_ID"
REDDIT_CLIENT_SECRET = "YOUR_REDDIT_CLIENT_SECRET"
REDDIT_USER_AGENT = "YoutubeStoryBot/1.0 by YourRedditUsername"

# Fill in your Gemini API key (from Google AI Studio)
GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"

# Subreddits to pull the story from
SUBREDDITS = ["sadstories", "beichtstuhl", "funny", "trending"]

# ==========================================
# 2. FETCH THE TOP REDDIT POST
# ==========================================

print("-> Connecting to Reddit...")
reddit = praw.Reddit(
    client_id=REDDIT_CLIENT_ID,
    client_secret=REDDIT_CLIENT_SECRET,
    user_agent=REDDIT_USER_AGENT
)

candidates = []
for name in SUBREDDITS:
    try:
        # Top post of the last 24 hours from this subreddit
        top_post = next(reddit.subreddit(name).top(time_filter="day", limit=1))
        candidates.append(top_post)
    except StopIteration:
        print(f"-> No posts found today in r/{name}, skipping.")
    except Exception as e:
        print(f"Reddit API error for r/{name}: {e}")

if not candidates:
    print("Error: No posts found in any of the configured subreddits.")
    sys.exit()

# Pick the highest-scoring post across all subreddits
top_post = max(candidates, key=lambda post: post.score)
reddit_title = top_post.title
reddit_text = top_post.selftext
print(f"-> Top post found in r/{top_post.subreddit.display_name}: '{reddit_title}'")

# ==========================================
# 3. GEMINI API FOR REWRITE
# ==========================================

print("-> Sending to Gemini for rewrite...")
genai.configure(api_key=GEMINI_API_KEY)

# Using gemini-1.5-pro for the best storytelling quality
model = genai.GenerativeModel('gemini-1.5-pro')

prompt = f"""
You are a professional YouTube scriptwriter.
Here is a true story from the Reddit forum "r/{top_post.subreddit.display_name}".

Title: {reddit_title}
Text: {reddit_text}

Your task:
1. Rewrite the story in polished, engaging English.
2. Adapt it so it works perfectly as a voiceover for a 5-minute YouTube video (about 800-1000 words).
3. Strictly remove any Reddit jargon (like "AITA", "TL;DR", "Update:", "Edit:"). The audience should not know it came from Reddit.
4. Start the script with a strong, emotional hook in the first 5 seconds that grabs the viewer immediately.
5. Tell the story in the first person, fluently and with emotion.

Give me ONLY the finished text the narrator should read. No stage directions, no introduction, just the script itself.
"""

try:
    response = model.generate_content(prompt)
    final_script = response.text
    print("-> Script generated successfully!")
except Exception as e:
    print(f"Gemini API error: {e}")
    sys.exit()

# ==========================================
# 4. SAVE THE SCRIPT
# ==========================================

with open("story.txt", "w", encoding="utf-8") as file:
    file.write(final_script)

print("-> SUCCESS! The script was saved to 'story.txt'.")
