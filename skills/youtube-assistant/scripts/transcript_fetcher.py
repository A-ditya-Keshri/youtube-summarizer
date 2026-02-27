import sys
import json
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter

def get_video_id(url):
    """Extracts video ID from a YouTube URL."""
    if "youtube.com/watch?v=" in url:
        return url.split("v=")[1].split("&")[0]
    elif "youtu.be/" in url:
        return url.split("youtu.be/")[1].split("?")[0]
    return None

def fetch_transcript(url):
    video_id = get_video_id(url)
    if not video_id:
        return {"error": "Invalid YouTube URL"}
    
    try:
        # Instantiating the class or using the correct static approach
        # In many versions it's YouTubeTranscriptApi.get_transcript(video_id)
        # but dir showed 'list' and 'fetch'. Let's try listing first.
        api = YouTubeTranscriptApi()
        transcript = api.fetch(video_id)
        # We'll return both the raw transcript (for timestamps) and formatted text
        return {
            "video_id": video_id,
            "raw": transcript,
            "text": TextFormatter().format_transcript(transcript)
        }
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(json.dumps({"error": "No URL provided"}))
    else:
        result = fetch_transcript(sys.argv[1])
        print(json.dumps(result))
