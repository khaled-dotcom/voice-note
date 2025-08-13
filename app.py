import streamlit as st
from groq import Groq
from pathlib import Path

API_KEY = "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"  # Replace with your actual Groq API key

client = Groq(api_key=API_KEY)

st.title("Speech to Text with Groq API")

audio_input = st.audio(
    st.file_uploader("Upload an audio file (wav, mp3, m4a)", type=["wav", "mp3", "m4a"])
)

if audio_input is not None:
    # Save uploaded file temporarily
    audio_bytes = audio_input.read()
    temp_audio_path = Path("temp_audio.wav")
    with open(temp_audio_path, "wb") as f:
        f.write(audio_bytes)

    with open(temp_audio_path, "rb") as f:
        transcription = client.audio.transcriptions.create(
            file=(str(temp_audio_path), f.read()),
            model="whisper-large-v3",
            response_format="verbose_json",
        )
    st.markdown("### Transcription:")
    st.write(transcription.get("text", "No transcription found"))

    temp_audio_path.unlink()  # delete temp file
