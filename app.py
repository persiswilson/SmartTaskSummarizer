import os
import google.generativeai as genai
import streamlit as st
from dotenv import load_dotenv

# Load .env with your Gemini API key
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

# Create Gemini model correctly
model = genai.GenerativeModel(model_name="gemini-2.5-pro")

# Task function
def process_task(task_description):
    prompt = f"""
    Given the following messy task description:
    ---
    {task_description}
    ---
    Do the following:
    1. Summarize the task in 1 clear sentence.
    2. Suggest 2–3 relevant tags (e.g., bug, frontend, urgent, backend, design, data).
    3. Assign a priority level from 1 to 5 (1 = lowest, 5 = highest) based on urgency and importance.

    Respond in this format:
    Summary: <summary>
    Tags: <tag1>, <tag2>, ...
    Priority: <number>
    """

    response = model.generate_content(prompt)
    return response.text.strip()

# Streamlit UI
st.set_page_config(page_title="Smart Task Summarizer", layout="centered")
st.title("Smart Task Summarizer + Tagger")

task_input = st.text_area("Enter a messy task description:", height=150, placeholder="e.g., Fix the checkout bug reported by the client on mobile...")

if st.button("Summarize Task"):
    if task_input.strip() == "":
        st.warning("Please enter a task description first.")
    else:
        with st.spinner("Generating..."):
            result = process_task(task_input)

        # Display results nicely
        try:
            summary = result.split("Summary:")[1].split("Tags:")[0].strip()
            tags = result.split("Tags:")[1].split("Priority:")[0].strip()
            priority = result.split("Priority:")[1].strip()

            st.subheader("✅ Result")
            st.markdown(f"**Summary:** {summary}")
            st.markdown(f"**Tags:** {tags}")
            st.markdown(f"**Priority:** {priority}")
        except:
            st.error("The AI response was not in the expected format. Try again or check your API.")




