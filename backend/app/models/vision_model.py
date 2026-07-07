from transformers import AutoModelForCausalLM, AutoTokenizer
from PIL import Image
import torch

MODEL_ID = "vikhyatk/moondream2"

print("🚀 Loading Moondream Vision Model...")

tokenizer = AutoTokenizer.from_pretrained(
    MODEL_ID,
    trust_remote_code=True
)

model = AutoModelForCausalLM.from_pretrained(
    MODEL_ID,
    trust_remote_code=True,
    torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32
)

if torch.cuda.is_available():
    model = model.cuda()

print("✅ Moondream Loaded")


def describe_image(image_path: str) -> str:
    """
    Generates a detailed scene description
    for a single image.
    """

    image = Image.open(image_path).convert("RGB")

    prompt = """
Describe this image for an AI video caption generator.

Focus on:

- Main objects
- People
- Actions
- Environment
- Mood
- Emotion
- Visual style
- Lighting

Keep the answer under 80 words.
"""

    answer = model.answer_question(
        image=image,
        question=prompt,
        tokenizer=tokenizer,
    )

    return answer.strip()