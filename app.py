import streamlit as st
import requests
import os
import uuid

# FastAPI server URL
FASTAPI_URL = "https://ai-story-mva.onrender.com/receive-script/"

# Session State for unique session ID
if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

# Session State for generated script
if "generated_script" not in st.session_state:
    st.session_state.generated_script = ""

st.title("Personal Injury Assist - Story Ad Generator")

# Generate New Concept Section
st.header("1. Generate a New Concept")
if st.button("Generate New Concept"):
    # Send a POST request to Zapier (this is your integration with GPT)
    # Example placeholder: simulate sending request
    st.success("New concept request sent successfully! Waiting for the script.")
    st.write("Ensure Zapier sends the script to FastAPI.")

# Check for Updates
st.header("2. Fetch the Script from Server")
if st.button("Fetch Script"):
    try:
        # Send GET request to FastAPI to fetch the script
        response = requests.get(f"{FASTAPI_URL}?session_id={st.session_state.session_id}")
        if response.status_code == 200:
            st.session_state.generated_script = response.json().get("script", "No script found.")
            st.success("Script fetched successfully!")
        else:
            st.warning("Script not found. Please wait or check your session ID.")
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching script: {e}")

# Display the Script
if st.session_state.generated_script:
    st.text_area("Generated Script", value=st.session_state.generated_script, height=300)

    # Provide Feedback
    feedback = st.text_input("Provide Feedback for the Script (optional)")
    if st.button("Submit Feedback"):
        feedback_payload = {
            "session_id": st.session_state.session_id,
            "feedback": feedback
        }
        # Replace with Zapier webhook if you're forwarding feedback
        st.success("Feedback submitted successfully!")

    # Approve Script and Generate AI Voice
    st.header("3. Approve Script & Generate AI Voice")
    if st.button("Approve & Generate AI Voice"):
        # Replace with the actual webhook for ElevenLabs
        st.success("AI voice generation request sent!")
