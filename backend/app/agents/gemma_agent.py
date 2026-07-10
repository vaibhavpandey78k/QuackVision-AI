import requests
import base64

OLLAMA_URL = "http://localhost:11434/api/generate"

VISION_MODEL = "gemma4:e4b"


def ask_gemma(prompt: str):

    payload = {
        "model": VISION_MODEL,
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(
        OLLAMA_URL,
        json=payload
    )

    response.raise_for_status()

    return response.json()["response"]


def ask_gemma_with_images(image_paths, prompt):

    encoded_images = []

    for image_path in image_paths:

        with open(image_path, "rb") as image:

            encoded_images.append(
                base64.b64encode(image.read()).decode("utf-8")
            )

    payload = {
        "model": VISION_MODEL,
        "prompt": prompt,
        "images": encoded_images,
        "stream": False
    }

    response = requests.post(
        OLLAMA_URL,
        json=payload
    )

    response.raise_for_status()

    return response.json()["response"]