import json
import re


def parse_ai_response(response: str):
    """
    Converts Gemma's response into a Python dictionary.

    Handles:
    - ```json ... ```
    - extra text before JSON
    - extra text after JSON
    - validates required fields
    """

    if not response:
        raise ValueError("Empty AI response.")

    response = response.strip()

    # Remove markdown code fences
    response = re.sub(r"^```json", "", response, flags=re.IGNORECASE)
    response = re.sub(r"^```", "", response)
    response = re.sub(r"```$", "", response)

    response = response.strip()

    # Find JSON object
    start = response.find("{")
    end = response.rfind("}")

    if start == -1 or end == -1:
        raise ValueError("No JSON object found.")

    response = response[start:end + 1]

    try:
        data = json.loads(response)

    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON returned by Gemma.\n\n{response}") from e

    # Required keys
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

    # Ensure hashtags & keywords are lists
    if not isinstance(data["hashtags"], list):
        data["hashtags"] = []

    if not isinstance(data["keywords"], list):
        data["keywords"] = []

    return data