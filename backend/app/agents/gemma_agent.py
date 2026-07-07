import requests
import base64

OLLAMA_URL = "http://localhost:11434/api/generate"

MODEL = "gemma3:4b"


def ask_gemma(prompt: str):
    """
    Normal text generation.
    """

    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(
        OLLAMA_URL,
        json=payload
    )

    response.raise_for_status()

    return response.json()["response"]


def ask_gemma_with_image(image_path: str, prompt: str):
    """
    Gemma Vision.
    """

    with open(image_path, "rb") as image:
        image_base64 = base64.b64encode(image.read()).decode("utf-8")

    payload = {
        "model": MODEL,
        "prompt": prompt,
        "images": [image_base64],
        "stream": False
    }

    response = requests.post(
        OLLAMA_URL,
        json=payload
    )

    response.raise_for_status()

    return response.json()["response"]