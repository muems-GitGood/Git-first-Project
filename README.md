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

### Turning the script into a voiceover (CapCut Pro)

CapCut Pro's built-in Text-to-Speech has more natural-sounding voices than most free TTS APIs, so use it instead of scripting a cloud TTS call:

1. Open CapCut Pro and start a new project.
2. Add a Text element, then paste in the contents of `story.txt`.
3. Select the text and choose **Text-to-Speech** (in the Captions/Audio panel).
4. Preview a few voices before picking one — avoid the default/first voice, as it tends to sound the most robotic. Voices labeled as "natural" or "conversational" generally sound best.
5. Generate the audio and it's added to your timeline as a separate audio track, ready to edit alongside your footage.
