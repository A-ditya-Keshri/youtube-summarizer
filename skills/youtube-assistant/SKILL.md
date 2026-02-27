---
name: youtube-assistant
description: Summarize YouTube videos and answer questions based on transcripts. Use when a message contains a YouTube URL or a user asks about a video.
---

# YouTube assistant

Use the provided Python scripts in the `scripts/` directory to process YouTube videos.

## Workflow

1. **Extract Transcript**: Use `bash` to run `python scripts/transcript_fetcher.py --url <YOUTUBE_URL> --save transcript.txt`.
   - On success, it saves the transcript to `transcript.txt`.
   - On failure, it returns an error message.

2. **Generate Summary**: Use `bash` to run `python scripts/summarizer.py --task summary --file transcript.txt --lang <LANGUAGE>`.
   - The summary includes Key Points, Timestamps, and Takeaway.

3. **Answer Question**: Use `bash` to run `python scripts/summarizer.py --task qa --file transcript.txt --question "<USER_QUESTION>" --lang <LANGUAGE>`.
   - Answers must be grounded in the transcript.

## Rules
- Default language is English.
- If the question is not covered, respond with "This topic is not covered in the video."
- Wrap transcript text in quotes when passing to shell if it contains spaces or special characters.
