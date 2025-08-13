import streamlit as st
from groq import Groq
import tempfile

API_KEY = "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"
client = Groq(api_key=API_KEY)

st.title("Text to Speech")

text = st.text_area("Enter text to convert:")

if st.button("Speak"):
    if not text.strip():
        st.warning("Please enter some text!")
    else:
        try:
            # This returns raw bytes of the audio
            response = client.audio.speech.create(
                model="playai-tts",
                voice="Aaliyah-PlayAI",
                response_format="wav",
                input=text,
            )

            # Save bytes to a temporary wav file
            with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp_file:
                tmp_file.write(response)  # write raw bytes
                tmp_file_path = tmp_file.name

            st.audio(tmp_file_path)

        except Exception as e:
            st.error(f"API Error: {e}")
