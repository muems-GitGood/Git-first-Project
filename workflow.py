import praw
import google.generativeai as genai
import sys

# ==========================================
# 1. API KEYS EINTRAGEN
# ==========================================

# Trage hier deine Reddit API-Daten ein (siehe README.md)
REDDIT_CLIENT_ID = "DEINE_REDDIT_CLIENT_ID"
REDDIT_CLIENT_SECRET = "DEIN_REDDIT_CLIENT_SECRET"
REDDIT_USER_AGENT = "YoutubeStoryBot/1.0 by DeineRedditUsername"

# Trage hier deinen Gemini API-Key ein (aus dem Google AI Studio)
GEMINI_API_KEY = "DEIN_GEMINI_API_KEY"

# ==========================================
# 2. REDDIT POST ABRUFEN
# ==========================================

print("-> Verbinde mit Reddit...")
reddit = praw.Reddit(
    client_id=REDDIT_CLIENT_ID,
    client_secret=REDDIT_CLIENT_SECRET,
    user_agent=REDDIT_USER_AGENT
)

try:
    # Holt den absoluten Top-Post der letzten 24 Stunden aus r/sadstories
    subreddit = reddit.subreddit("sadstories")
    top_post = next(subreddit.top(time_filter="day", limit=1))

    reddit_title = top_post.title
    reddit_text = top_post.selftext
    print(f"-> Top-Post gefunden: '{reddit_title}'")

except StopIteration:
    print("Fehler: Keine Posts in den letzten 24 Stunden gefunden.")
    sys.exit()
except Exception as e:
    print(f"Reddit API Fehler: {e}")
    sys.exit()

# ==========================================
# 3. GEMINI API FÜR ÜBERSETZUNG & REWRITE
# ==========================================

print("-> Sende an Gemini für Translation & Rewrite...")
genai.configure(api_key=GEMINI_API_KEY)

# Wir nutzen gemini-1.5-pro für die beste Storytelling-Qualität
model = genai.GenerativeModel('gemini-1.5-pro')

prompt = f"""
Du bist ein professioneller YouTube-Skriptschreiber.
Hier ist eine wahre Geschichte aus dem Reddit-Forum "sadstories".

Titel: {reddit_title}
Text: {reddit_text}

Deine Aufgabe:
1. Übersetze die Geschichte in fehlerfreies, fesselndes Deutsch.
2. Schreibe sie so um, dass sie perfekt als Voiceover für ein 5-Minuten YouTube-Video funktioniert (ca. 800 - 1000 Wörter).
3. Entferne strikt jeglichen Reddit-Jargon (wie "AITA", "TL;DR", "Update:", "Edit:"). Das Publikum soll nicht wissen, dass es von Reddit ist.
4. Beginne das Skript mit einem starken, emotionalen Hook in den ersten 5 Sekunden, der den Zuschauer sofort fesselt.
5. Schreibe die Geschichte aus der Ich-Perspektive, flüssig und emotional.

Gib mir AUSSCHLIESSLICH den fertigen Text, den der Sprecher vorlesen soll. Keine Regieanweisungen, keine Einleitung, nur das reine Skript.
"""

try:
    response = model.generate_content(prompt)
    final_script = response.text
    print("-> Skript erfolgreich generiert!")
except Exception as e:
    print(f"Gemini API Fehler: {e}")
    sys.exit()

# ==========================================
# 4. SKRIPT SPEICHERN
# ==========================================

with open("story.txt", "w", encoding="utf-8") as file:
    file.write(final_script)

print("-> ERFOLG! Das Skript wurde in 'story.txt' gespeichert.")
