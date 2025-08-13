import streamlit as st
from groq import Groq
from pathlib import Path
import tempfile

API_KEY = "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"  # Put your Groq API key here
client = Groq(api_key=API_KEY)

st.title("Voice to Text and Back to Speech")

uploaded_audio = st.file_uploader("Upload your audio (wav, mp3, m4a)", type=["wav", "mp3", "m4a"])

if uploaded_audio is not None:
    # Save audio to temp file
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp_file:
        tmp_file.write(uploaded_audio.read())
        tmp_filepath = tmp_file.name

    # Send audio to Groq whisper-large-v3 speech-to-text
    with open(tmp_filepath, "rb") as f:
        transcription = client.audio.transcriptions.create(
            file=(tmp_filepath, f.read()),
            model="whisper-large-v3",
            response_format="verbose_json",
        )
    
    text = transcription.get("text", "")
    st.markdown("### Transcribed Text:")
    st.write(text)

    if text:
        # Convert text back to speech using Groq TTS
        tts_response = client.audio.speech.create(
            model="playai-tts",
            voice="Aaliyah-PlayAI",
            response_format="wav",
            input=text,
        )
        audio_path = tempfile.NamedTemporaryFile(suffix=".wav", delete=False).name
        tts_response.stream_to_file(audio_path)
        
        st.audio(audio_path)

    # Clean up temp audio file
    Path(tmp_filepath).unlink()

