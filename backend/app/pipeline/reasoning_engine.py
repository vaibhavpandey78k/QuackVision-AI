import json

from app.agents.gemma_agent import ask_gemma
from app.pipeline.json_parser import parse_ai_response


def load_timeline(timeline_file: str):
    with open(timeline_file, "r", encoding="utf-8") as f:
        return json.load(f)


def build_prompt(data):

    prompt = f"""
You are QuackVision AI, a multimodal video understanding assistant.

Analyze the following video using Speech, Vision and OCR together.

VIDEO INFORMATION

Video Name:
{data["video_name"]}

Frames:
{data["frames"]}

Keyframes:
{data["keyframes"]}

Detected Language:
{data["detected_language"]}

Visual Context:
{data["visual_context"]}

Speech Transcript:
{data["speech"]}

OCR Text:
{chr(10).join(data["ocr"])}

TASK

Understand the complete story instead of describing individual frames.

Reasoning Priority:
1. Speech (primary)
2. Vision
3. OCR

Rules:

- If speech clearly explains the story, let it dominate.
- Use vision to improve atmosphere, actions, emotions and setting.
- Use OCR only for important subtitles, signs or quotes.
- Never let a single image contradict the spoken meaning.
- If speech is missing, rely mainly on vision.

Generate natural social-media captions.

Avoid robotic phrases such as:
depicts, portrays, illustrates, visual representation, fragmented transcript, insufficient information.

OUTPUT

Return ONLY valid JSON.

Generate:

- detected_language
- video_category
- overall_mood
- confidence_score (0-100)

- primary_source
- reasoning_mode

- formal_caption (professional, LinkedIn style)

- sarcastic_caption (clever, relatable)

- humorous_tech_caption (programmer humour)

- humorous_nontech_caption (meme style)

- summary (2-3 sentences)

- hashtags (exactly 20)

- keywords (exactly 15)

If the spoken language is not English, first understand its meaning and then write fluent English captions while preserving the original emotion.

JSON FORMAT

{{
    "detected_language": "",
    "video_category": "",
    "overall_mood": "",
    "confidence_score": 0,

    "primary_source": "",
    "reasoning_mode": "",

    "formal_caption": "",
    "sarcastic_caption": "",
    "humorous_tech_caption": "",
    "humorous_nontech_caption": "",

    "summary": "",

    "hashtags": [],

    "keywords": []
}}
"""

    return prompt


def analyze_video(timeline_file):

    data = load_timeline(timeline_file)

    prompt = build_prompt(data)

    ai_response = ask_gemma(prompt)

    parsed_response = parse_ai_response(ai_response)

    return parsed_response