import streamlit as st
from groq import Groq
from io import BytesIO

API_KEY = "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"
client = Groq(api_key=API_KEY)

st.title("Text to Speech with Groq API")

text_input = st.text_area("Enter text to convert to speech", height=150)

if st.button("Generate Speech"):
    if not text_input.strip():
        st.warning("Please enter some text!")
    else:
        with st.spinner("Generating speech..."):
            try:
                response = client.audio.speech.create(
                    model="playai-tts",
                    voice="Aaliyah-PlayAI",
                    response_format="wav",
                    input=text_input,
                )
                audio_bytes = BytesIO()
                response.stream_to_file(audio_bytes)
                audio_bytes.seek(0)
                st.audio(audio_bytes, format="audio/wav")
                st.success("Speech generated successfully!")
            except Exception as e:
                st.error(f"Error: {e}")
