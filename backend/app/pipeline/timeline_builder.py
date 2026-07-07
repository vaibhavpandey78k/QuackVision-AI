import json


def build_timeline(
    video_name,
    frame_count,
    keyframe_count,
    transcript,
    detected_language,
    visual_context,
    ocr_text,
):
    """
    Creates the structured timeline used by the AI reasoning engine.
    """

    data = {
        "video_name": video_name,
        "frames": frame_count,
        "keyframes": keyframe_count,
        "detected_language": detected_language,
        "speech": transcript,
        "visual_context": visual_context,
        "ocr": ocr_text,
    }

    return data


def save_timeline(data, output_file):
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(
            data,
            f,
            indent=4,
            ensure_ascii=False
        )