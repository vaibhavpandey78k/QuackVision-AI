import json

from app.agents.gemma_agent import ask_gemma
from app.pipeline.json_parser import parse_ai_response


def load_timeline(timeline_file: str):
    with open(timeline_file, "r", encoding="utf-8") as f:
        return json.load(f)


def build_prompt(data):

    prompt = f"""
You are QuackVision AI.

You are a world-class multimodal AI Video Caption Generator built for professional content creators.

====================================================
VIDEO INFORMATION
====================================================

Video Name:
{data["video_name"]}

Frames Extracted:
{data["frames"]}

Keyframes:
{data["keyframes"]}

Detected Spoken Language:
{data["detected_language"]}

Visual Understanding:
{data["visual_context"]}

Speech Transcript:
{data["speech"]}

OCR Text:
{chr(10).join(data["ocr"])}

====================================================
MISSION
====================================================

Your task is NOT to describe the video.

Your task is to understand the complete story behind the video and generate captions that people would actually post on social media.

Think like an experienced creator with millions of followers.

Your goal is to understand:

• Story
• Emotion
• Audience
• Creator Intent
• Visual Mood
• Social Media Context

====================================================
MULTIMODAL REASONING POLICY
====================================================

Use all available information.

Default reasoning priority:

Speech Transcript → 65%

Visual Understanding → 30%

OCR Text → 5%

Decision Rules:

1. If Speech and Vision agree,
combine both naturally.

2. If Speech expresses emotions,
relationships,
heartbreak,
motivation,
education,
storytelling,
or poetry,

Speech becomes the PRIMARY source.

Vision should enhance atmosphere,
emotion,
scene,
and cinematic context.

3. If speech is missing,
silent,
or unreliable,

increase the importance of Vision automatically.

4. OCR should only reinforce important subtitles,
quotes,
lyrics,
or text inside the video.

5. Never allow a background object
or single frame
to override the spoken meaning.

6. Understand the complete story,
not individual frames.

====================================================
WRITING STYLE
====================================================

Write naturally.

Sound like a real human creator.

Avoid AI sounding phrases like:

- depicts
- portrays
- illustrates
- visual representation
- fragmented transcript
- insufficient information
- unable to understand

Avoid writing like an academic paper.

Create captions that people would actually post.

====================================================
CAPTION REQUIREMENTS
====================================================

Generate:

1. Formal Caption
   • Professional
   • Emotional
   • Suitable for LinkedIn

2. Sarcastic Caption
   • Clever
   • Relatable
   • Never offensive

3. Humorous Tech Caption
   • Original
   • Programmer humour
   • AI / Coding jokes
   • Avoid generic "404 Error"

4. Humorous Non-Tech Caption
   • Meme style
   • Funny
   • Shareable

5. Summary
   • 2-3 sentences

6. Hashtags
   • Exactly 20
   • Trending
   • Relevant

7. SEO Keywords
   • Exactly 15

Determine:

• Video Category
• Overall Mood
• Confidence Score (0-100)

Also determine:

• Primary Source Used
(Speech / Vision / OCR)

• Reasoning Mode
(Speech + Vision,
Vision + OCR,
Speech + Vision + OCR)

====================================================
IMPORTANT
====================================================

If the detected language is not English,

Understand its meaning first.

Then generate fluent English captions while preserving the original emotion.

Never translate word-for-word.

Capture the emotional meaning instead.

Return ONLY valid JSON.

====================================================
JSON FORMAT
====================================================

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