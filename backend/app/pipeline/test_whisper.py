from speech_to_text import transcribe_audio

text = transcribe_audio(
    "../uploads/audio/WhatsApp Video 2026-07-05 at 7.46.09 PM.wav"
)

with open("transcript.txt", "w", encoding="utf-8") as f:
    f.write(text)

print("Transcript saved to transcript.txt")