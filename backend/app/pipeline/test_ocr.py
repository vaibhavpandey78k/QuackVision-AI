from ocr import extract_text

text = extract_text(
    "../uploads/keyframes/WhatsApp Video 2026-07-05 at 7.46.09 PM/frame_0000.jpg"
)

print("\n========== OCR ==========\n")
print(text)