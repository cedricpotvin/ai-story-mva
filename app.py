import streamlit as st
import requests
import uuid

# Zapier webhook URLs
ZAPIER_GPT_WEBHOOK = "https://hooks.zapier.com/hooks/catch/6652482/2z9cojg/"
ZAPIER_ELEVENLABS_WEBHOOK = "https://hooks.zapier.com/hooks/catch/6652482/2z90tsd/"

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
    payload = {
        "session_id": st.session_state.session_id,
        "request_type": "new_concept"
    }
    response = requests.post(ZAPIER_GPT_WEBHOOK, json=payload)

    if response.status_code == 200:
        st.session_state.generated_script = response.json().get("script", "No script generated.")
        st.success("New concept generated successfully!")
    else:
        st.error("Failed to generate a new concept. Please try again.")

# Display and Review Generated Script
if st.session_state.generated_script:
    st.header("2. Review the Generated Script")
    st.text_area("Generated Script", value=st.session_state.generated_script, height=300)

    # Provide Feedback
    feedback = st.text_input("Provide Feedback for the Script (optional)")
    if st.button("Submit Feedback"):
        feedback_payload = {
            "session_id": st.session_state.session_id,
            "feedback": feedback
        }
        feedback_response = requests.post(ZAPIER_GPT_WEBHOOK, json=feedback_payload)
        if feedback_response.status_code == 200:
            st.success("Feedback submitted successfully!")
        else:
            st.error("Failed to submit feedback. Please try again.")

    # Approve Script and Generate AI Voice
    st.header("3. Approve Script & Generate AI Voice")
    if st.button("Approve & Generate AI Voice"):
        voice_payload = {
            "session_id": st.session_state.session_id,
            "approved_script": st.session_state.generated_script
        }
        voice_response = requests.post(ZAPIER_ELEVENLABS_WEBHOOK, json=voice_payload)
        if voice_response.status_code == 200:
            st.success("AI voice generated successfully! Check Zapier for the output.")
        else:
            st.error("Failed to generate AI voice. Please try again.")
