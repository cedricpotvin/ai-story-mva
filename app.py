import streamlit as st
import uuid
import requests

# Constants
ZAPIER_WEBHOOK_GPT_URL = "https://hooks.zapier.com/hooks/catch/6652482/2z9cojg/"
ZAPIER_WEBHOOK_ELEVENLABS_URL = "https://hooks.zapier.com/hooks/catch/6652482/2z90tsd/"

# Streamlit App Title
st.title("Personal Injury Assist - Story Ad Generator")

# Session State for Unique Session ID
if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

# Session State for Generated Script
if "generated_script" not in st.session_state:
    st.session_state.generated_script = ""

# Generate New Concept Section
st.header("1. Generate a New Concept")
if st.button("Generate New Concept"):
    # Payload for GPT Webhook
    payload = {
        "session_id": st.session_state.session_id,
        "request_type": "new_concept"
    }

    # Sending POST request to Zapier GPT Webhook
    response = requests.post(ZAPIER_WEBHOOK_GPT_URL, json=payload)
    if response.status_code == 200:
        st.session_state.generated_script = response.json().get("script", "No script generated yet.")
        st.success("New concept generated successfully!")
    else:
        st.error("Failed to generate a new concept. Please try again.")

# Display Generated Script
if st.session_state.generated_script:
    st.header("2. Review Generated Script")
    st.text_area("Generated Script", value=st.session_state.generated_script, height=300)

    # Feedback Section
    st.subheader("Provide Feedback")
    feedback = st.text_input("Enter your feedback for improvements (optional)")
    if st.button("Submit Feedback"):
        # Send feedback via Zapier webhook (optional, depends on Zapier setup)
        feedback_payload = {
            "session_id": st.session_state.session_id,
            "feedback": feedback
        }
        feedback_response = requests.post(ZAPIER_WEBHOOK_GPT_URL, json=feedback_payload)
        if feedback_response.status_code == 200:
            st.success("Feedback submitted successfully!")
        else:
            st.error("Failed to submit feedback. Please try again.")

# Approve Script and Generate AI Voice
if st.session_state.generated_script:
    st.header("3. Approve Script & Generate AI Voice")
    if st.button("Approve & Generate AI Voice"):
        # Payload for Eleven Labs Webhook
        ai_voice_payload = {
            "session_id": st.session_state.session_id,
            "approved_script": st.session_state.generated_script
        }

        # Sending POST request to Zapier Eleven Labs Webhook
        ai_voice_response = requests.post(ZAPIER_WEBHOOK_ELEVENLABS_URL, json=ai_voice_payload)
        if ai_voice_response.status_code == 200:
            st.success("AI voice generated successfully! Check Zapier for the output.")
        else:
            st.error("Failed to generate AI voice. Please try again.")
