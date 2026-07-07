import whisper

# Load Whisper model once when the server starts
model = whisper.load_model("base")


def transcribe_audio(audio_path: str):
    """
    Transcribes audio and detects the spoken language.

    Returns:
    {
        "transcript": "...",
        "language": "en"
    }
    """

    result = model.transcribe(audio_path)

    return {
        "transcript": result["text"].strip(),
        "language": result["language"]
    }