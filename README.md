# Git-first-Project
yessirski first project

## YouTube Script Workflow

`workflow.py` fetches the top daily post from r/sadstories, r/beichtstuhl, r/funny and r/trending (whichever has the highest-scoring post) and uses Gemini to rewrite it as an English YouTube voiceover script (saved to `story.txt`).

### Setup

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
2. Fill in the placeholders in `workflow.py`:
   - `REDDIT_CLIENT_ID`, `REDDIT_CLIENT_SECRET`, `REDDIT_USER_AGENT`: create a Reddit app at https://www.reddit.com/prefs/apps (type "script", redirect URI `http://localhost`).
   - `GEMINI_API_KEY`: key from Google AI Studio.
3. Run:
   ```
   python workflow.py
   ```
