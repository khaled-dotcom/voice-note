import streamlit as st
from groq import Groq
import tempfile

# Your Groq API key
API_KEY = "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"
client = Groq(api_key=API_KEY)

st.title("Text to Speech with Groq")

text_input = st.text_area("Type your text here:")

if st.button("Convert to Speech"):
    if text_input.strip() == "":
        st.warning("Please enter some text!")
    else:
        # Call Groq API to convert text to speech
        tts_response = client.audio.speech.create(
            model="playai-tts",
            voice="Aaliyah-PlayAI",
            response_format="wav",
            input=text_input,
        )
        
        # Save audio to temporary file
        audio_path = tempfile.NamedTemporaryFile(suffix=".wav", delete=False).name
        tts_response.stream_to_file(audio_path)

        # Play audio in Streamlit
        st.audio(audio_path)
