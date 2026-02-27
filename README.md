# YouTube Summarizer & Q&A Telegram Bot (OpenClaw)

This is a smart AI research assistant that fetches YouTube video transcripts, generates structured summaries, and answers follow-up questions via Telegram. Built using the OpenClaw framework.

## Features
- **YouTube Link Processing**: Send any YouTube link to get an instant summary.
- **Structured Summaries**: Includes Key Points, Timestamps, and Core Takeaways.
- **Contextual Q&A**: Ask questions about the video content.
- **Multi-language Support**: Supports English and Indian languages (e.g., Hindi, Kannada, Tamil).
- **Grounded Responses**: Answers are strictly based on the video transcript to avoid hallucinations.

## Architecture
- **Framework**: OpenClaw (Local AI Agent Orchestration).
- **Transcript Engine**: `youtube-transcript-api` (Python).
- **AI Model**: Gemini 3 Flash Preview (via latest `google-genai` SDK).
- **Gateway**: Telegram Bot API.

## Design Trade-offs
1. **Local Orchestration**: OpenClaw runs locally, ensuring privacy and control over agent logic.
2. **Python-based Core**: Using Python for transcript fetching and AI calls allows for easy integration with standard data processing libraries.
3. **Stateless Skill**: The transcript is fetched per request (or cached in the agent session) to keep the implementation simple and robust.

## Prerequisites
- [Node.js](https://nodejs.org/) installed.
- [Python 3.10+](https://www.python.org/) installed.
- A Telegram Bot Token from [@BotFather](https://t.me/BotFather).
- A Google Gemini API Key from [Google AI Studio](https://aistudio.google.com/).

## Setup Instructions

1. **Clone the project & Install Dependencies**:
   ```bash
   cd youtube-summarizer-claw
   npm install
   pip install youtube-transcript-api google-genai python-dotenv
   ```

2. **Configure Environment Variables**:
   Create a `.env` file in the root directory:
   ```env
   TELEGRAM_BOT_TOKEN=your_telegram_token
   GEMINI_API_KEY=your_gemini_api_key
   ```

3. **Start the Bot**:
   ```bash
   npx openclaw
   ```

4. **Interact**:
   - Open Telegram and find your bot.
   - Send a YouTube link.
   - Ask: "What are the main pricing points?"
   - Ask: "Summarize in Hindi".
