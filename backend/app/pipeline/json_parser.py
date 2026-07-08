import json
import re


def parse_ai_response(response: str):
    """
    Converts Gemma's response into a Python dictionary.
    """

    if not response:
        raise ValueError("Empty AI response.")

    # -----------------------------
    # Clean Gemma Output
    # -----------------------------
    response = response.strip()

    # Remove markdown
    response = response.replace("```json", "")
    response = response.replace("```", "")

    # Remove Gemma SentencePiece spaces
    response = response.replace("▁", " ")

    # Remove zero-width unicode characters
    response = re.sub(r'[\u200B-\u200D\uFEFF]', '', response)

    # Collapse repeated whitespace
    response = re.sub(r"[ \t]+", " ", response)

    response = response.strip()

    # -----------------------------
    # Extract JSON
    # -----------------------------
    start = response.find("{")
    end = response.rfind("}")

    if start == -1 or end == -1:
        raise ValueError("No JSON object found.")

    response = response[start:end + 1]

    try:
        data = json.loads(response)

    except json.JSONDecodeError as e:
        print("\n========== INVALID JSON ==========\n")
        print(response)
        print("\n==================================\n")
        raise ValueError("Invalid JSON returned by Gemma.") from e

    # -----------------------------
    # Required Keys
    # -----------------------------
    required_keys = [
        "detected_language",
        "video_category",
        "confidence_score",
        "formal_caption",
        "sarcastic_caption",
        "humorous_tech_caption",
        "humorous_nontech_caption",
        "summary",
        "hashtags",
        "keywords",
    ]

    for key in required_keys:
        if key not in data:
            raise ValueError(f"Missing key: {key}")

    if not isinstance(data["hashtags"], list):
        data["hashtags"] = []

    if not isinstance(data["keywords"], list):
        data["keywords"] = []

    return data