# Git-first-Project
yessirski first project

## YouTube-Skript-Workflow

`workflow.py` holt den Top-Post des Tages aus r/sadstories und lässt Gemini daraus ein deutsches YouTube-Voiceover-Skript schreiben (gespeichert in `story.txt`).

### Setup

1. Abhängigkeiten installieren:
   ```
   pip install -r requirements.txt
   ```
2. In `workflow.py` die Platzhalter eintragen:
   - `REDDIT_CLIENT_ID`, `REDDIT_CLIENT_SECRET`, `REDDIT_USER_AGENT`: Reddit-App unter https://www.reddit.com/prefs/apps anlegen (Typ "script", Redirect-URI `http://localhost`).
   - `GEMINI_API_KEY`: Key aus dem Google AI Studio.
3. Ausführen:
   ```
   python workflow.py
   ```
