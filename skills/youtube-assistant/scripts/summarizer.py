import sys
import json
import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client()
MODEL_NAME = "gemini-3-flash-preview"

def generate_summary(transcript_text, language="English"):
    prompt = f"""
    You are a professional YouTube research assistant. Summarize the following YouTube video transcript in {language}.
    
    The summary must be structured as follows:
    🎥 Video Title: [Inferred from context if possible, or 'Video Summary']
    
    📌 5 Key Points:
    - Point 1
    - Point 2
    - Point 3
    - Point 4
    - Point 5
    
    ⏱ Important Timestamps:
    - [Approximate time] - Description
    
    🧠 Core Takeaway:
    One sentence summary of the main message.

    Transcript:
    {transcript_text[:30000]} # Limit transcript to avoid token issues
    """
    
    response = client.models.generate_content(
        model=MODEL_NAME, 
        contents=prompt
    )
    return response.text

def answer_question(transcript_text, question, language="English"):
    prompt = f"""
    You are a professional YouTube research assistant. Answer the following question about the YouTube video in {language} based ONLY on the provided transcript.
    
    If the answer is not found in the transcript, respond exactly with:
    "This topic is not covered in the video."

    Question: {question}

    Transcript:
    {transcript_text[:30000]}
    """
    
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )
    return response.text

if __name__ == "__main__":
    # Expecting: python summarizer.py --task [summary|qa] --transcript [txt] --file [path] --lang [lang] --question [q]
    args = sys.argv[1:]
    task = "summary"
    transcript = ""
    file_path = ""
    language = "English"
    question = ""

    for i in range(len(args)):
        if args[i] == "--task": task = args[i+1]
        if args[i] == "--transcript": transcript = args[i+1]
        if args[i] == "--file": file_path = args[i+1]
        if args[i] == "--lang": language = args[i+1]
        if args[i] == "--question": question = args[i+1]

    if file_path:
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                transcript = f.read()
        except Exception as e:
            print(f"Error reading transcript file: {str(e)}")
            sys.exit(1)

    if task == "summary":
        print(generate_summary(transcript, language))
    elif task == "qa":
        print(answer_question(transcript, question, language))
