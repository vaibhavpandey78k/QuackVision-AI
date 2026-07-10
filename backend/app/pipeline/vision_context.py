from pathlib import Path
import time

from app.agents.gemma_agent import ask_gemma_with_images


MAX_KEYFRAMES = 7


def build_visual_context(keyframes_folder: str):
    """
    Uses Gemma 4 Vision to understand multiple keyframes
    from the same video in ONE inference call.
    """

    folder = Path(keyframes_folder)

    images = sorted(folder.glob("*.jpg"))

    if not images:
        return "No keyframes detected."

    # Select evenly spaced keyframes across the whole video
    if len(images) <= MAX_KEYFRAMES:
        selected_images = images
    else:
        total = len(images)

        indices = [
            round(i * (total - 1) / (MAX_KEYFRAMES - 1))
            for i in range(MAX_KEYFRAMES)
        ]

        selected_images = [images[i] for i in indices]

    print("\n📸 Selected Keyframes:")
    for img in selected_images:
        print(f"   • {img.name}")

    print(f"\n🖼️ Sending {len(selected_images)} keyframes together to Gemma 4...\n")

    prompt = """
You are QuackVision AI.

You are given chronologically ordered keyframes from the SAME video.

First understand each keyframe internally.

Then infer the complete story across the sequence.

Focus on:

• Story progression
• Main subject
• Important actions
• Environment
• Objects
• Emotions
• Overall mood
• Camera style
• Creator intent

Return ONE coherent visual understanding.

Keep the response under 120 words.

Do NOT mention frame numbers.
Do NOT describe each image separately.
Write one combined understanding of the entire video.
"""

    start = time.perf_counter()

    try:

        response = ask_gemma_with_images(
            [str(img) for img in selected_images],
            prompt
        )

        print(
            f"🟢 Multi-frame Vision : {time.perf_counter() - start:.2f} sec"
        )

        return response.strip()

    except Exception as e:

        print(f"❌ Vision Error: {e}")

        return "Vision understanding failed."