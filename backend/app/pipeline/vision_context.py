from pathlib import Path

from app.agents.gemma_agent import ask_gemma_with_image


def build_visual_context(keyframes_folder: str):
    """
    Uses Gemma 3 Vision to understand
    the important keyframes of a video.
    """

    folder = Path(keyframes_folder)

    images = sorted(folder.glob("*.jpg"))

    if not images:
        return "No keyframes detected."

    descriptions = []

    # Analyze at most 5 representative keyframes
    for image in images[:5]:

        print(f"🖼️ Analyzing {image.name}")

        prompt = """
You are an expert video understanding AI.

Analyze this image as one frame of a short video.

Describe:

1. Main subject
2. Actions happening
3. Environment
4. Objects
5. Emotions
6. Mood
7. Visual style
8. Important details useful for generating social media captions.

Keep the answer under 80 words.
"""

        try:

            answer = ask_gemma_with_image(
                str(image),
                prompt
            )

            descriptions.append(answer.strip())

        except Exception as e:

            print(f"Vision Error: {e}")

    return "\n\n".join(descriptions)