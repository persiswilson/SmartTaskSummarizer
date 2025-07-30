# Smart Task Summarizer + Tagger

An AI-powered Streamlit tool that transforms messy task descriptions into clean summaries, relevant tags, and priority scores.
## Description

Smart Task Summarizer + Tagger is an AI-powered tool designed to convert cluttered, unstructured task descriptions into clear, actionable items. It uses Google's Gemini Pro LLM to summarize each task, assign meaningful tags, and classify its priority level (High, Medium, or Low).
This tool is ideal for project managers, productivity enthusiasts, and professionals who deal with messy to-do lists, meeting notes, or backlog items and want to quickly clean them up with AI.
---

## Features

- **Summarize** unstructured task descriptions.
- **Auto-tag** tasks based on content.
- **Score priority** on a scale from 1 (Low) to 5 (High).
- Simple, fast, and interactive UI built with **Streamlit**.
- Powered by **Gemini Pro (Google Generative AI)**.

---
## Technologies Used:
Language: Python

AI API: Google Gemini (via google-generativeai)

UI Framework: Streamlit

Environment Management: venv + .env

Others: dotenv, prompt engineering

## Project Initialization
Create a new folder: SmartTaskSummarizer

Inside, run:

python -m venv env
env\Scripts\activate  # Windows

Install necessary libraries:

pip install streamlit google-generativeai python-dotenv

## Set Up Gemini API
Get API key from Google AI Studio

Create a .env file:

GEMINI_API_KEY=your_actual_key_here

## Code the Core Functionality
Create app.py:
- Load API key using dotenv
- Use Gemini's generate_content() to:
     - Summarize input text
     - Tag tasks with categories (e.g., "Bug", "Research", "Urgent")
     - Score task priorities logically
- Output a cleaned-up task list

## Demo UI

> Enter a messy task and get an instant AI-curated summary.
> 

