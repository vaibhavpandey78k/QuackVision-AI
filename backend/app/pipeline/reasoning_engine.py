import json

from app.agents.gemma_agent import ask_gemma
from app.pipeline.json_parser import parse_ai_response


def load_timeline(timeline_file: str):
    with open(timeline_file, "r", encoding="utf-8") as f:
        return json.load(f)


def build_prompt(data):

    prompt = f"""
You are QuackVision AI.

Analyze the video using:

Speech:
{data["speech"]}

Visual Context:
{data["visual_context"]}

OCR:
{chr(10).join(data["ocr"])}

Instructions:

• Understand the complete story.
• Speech is the primary source.
• Vision should improve context, actions and emotions.
• OCR only supports important visible text.
• If speech is missing, rely on vision.

Generate:

- detected_language
- video_category
- overall_mood
- confidence_score (0-100)

- primary_source
- reasoning_mode

- formal_caption
- sarcastic_caption
- humorous_tech_caption
- humorous_nontech_caption

- summary (2 sentences)

- exactly 20 hashtags

- exactly 15 SEO keywords

If speech is not English,
understand it first,
then write fluent English captions.

Return ONLY this JSON.

{{
  "detected_language":"",
  "video_category":"",
  "overall_mood":"",
  "confidence_score":0,

  "primary_source":"",
  "reasoning_mode":"",

  "formal_caption":"",
  "sarcastic_caption":"",
  "humorous_tech_caption":"",
  "humorous_nontech_caption":"",

  "summary":"",

  "hashtags":[],

  "keywords":[]
}}
"""

    return prompt


def analyze_video(timeline_file):

    data = load_timeline(timeline_file)

    prompt = build_prompt(data)

    print(f"\n📝 Prompt Size : {len(prompt)} characters")

    ai_response = ask_gemma(prompt)

    parsed_response = parse_ai_response(ai_response)

    return parsed_response