import easyocr

# Load OCR model once
reader = easyocr.Reader(['en'])

def extract_text(image_path: str):
    """
    Extract text from an image.
    """

    results = reader.readtext(image_path)

    text = []

    for item in results:
        text.append(item[1])

    return "\n".join(text)