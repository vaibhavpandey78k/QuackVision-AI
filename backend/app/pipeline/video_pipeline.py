from pathlib import Path
import json
import time

from app.video.frame_extractor import extract_frames
from app.video.scene_detector import detect_keyframes

from app.pipeline.reasoning_engine import analyze_video
from app.pipeline.vision_context import build_visual_context

from app.pipeline.audio_extractor import extract_audio
from app.pipeline.speech_to_text import transcribe_audio
from app.pipeline.ocr import extract_text
from app.pipeline.timeline_builder import (
    build_timeline,
    save_timeline,
)

from app.pipeline.progress_tracker import (
    update_progress,
    reset_progress,
)


def process_video(video_path: str):
    """
    Main AI processing pipeline.
    """

    total_start = time.time()

    # Reset Progress
    reset_progress()

    video_path = Path(video_path)

    uploads = video_path.parent
    video_name = video_path.stem

    # --------------------------------
    # Output Folders
    # --------------------------------
    frames_folder = uploads / "frames" / video_name
    keyframes_folder = uploads / "keyframes" / video_name

    audio_folder = uploads / "audio"
    transcripts_folder = uploads / "transcripts"
    timelines_folder = uploads / "timelines"
    reports_folder = uploads / "reports"

    audio_folder.mkdir(exist_ok=True)
    transcripts_folder.mkdir(exist_ok=True)
    timelines_folder.mkdir(exist_ok=True)
    reports_folder.mkdir(exist_ok=True)

    audio_file = audio_folder / f"{video_name}.wav"
    transcript_file = transcripts_folder / f"{video_name}.txt"
    timeline_file = timelines_folder / f"{video_name}.json"
    report_file = reports_folder / f"{video_name}.json"

    # --------------------------------
    # Step 1 - Extract Frames
    # --------------------------------
    start = time.time()

    frame_count = extract_frames(
        str(video_path),
        str(frames_folder)
    )

    print(f"🟢 Frame Extraction : {time.time()-start:.2f} sec")

    update_progress(15, "🎥 Extracting Frames")

    # --------------------------------
    # Step 2 - Detect Keyframes
    # --------------------------------
    start = time.time()

    keyframe_count = detect_keyframes(
        str(frames_folder),
        str(keyframes_folder)
    )

    print(f"🟢 Scene Detection : {time.time()-start:.2f} sec")

    update_progress(30, "🖼 Detecting Key Scenes")

    # --------------------------------
    # Step 3 - Extract Audio
    # --------------------------------
    start = time.time()

    extract_audio(
        str(video_path),
        str(audio_file)
    )

    print(f"🟢 Audio Extraction : {time.time()-start:.2f} sec")

    update_progress(45, "🔊 Extracting Audio")

    # --------------------------------
    # Step 4 - Speech to Text
    # --------------------------------
    start = time.time()

    speech_result = transcribe_audio(
        str(audio_file)
    )

    print(f"🟢 Whisper : {time.time()-start:.2f} sec")

    transcript = speech_result["transcript"]
    detected_language = speech_result["language"]

    with open(transcript_file, "w", encoding="utf-8") as f:
        f.write(transcript)

    update_progress(60, "🗣 Understanding Speech")

    # --------------------------------
    # Step 5 - OCR
    # --------------------------------
    start = time.time()

    keyframe_images = sorted(keyframes_folder.glob("*.jpg"))

    ocr_text = []

    for image in keyframe_images:

        text = extract_text(str(image))

        if text.strip():
            ocr_text.append(text)

    print(f"🟢 OCR : {time.time()-start:.2f} sec")

    update_progress(72, "👁 Reading On-screen Text")

    # --------------------------------
    # Step 6 - Vision Context
    # --------------------------------
    start = time.time()

    visual_context = build_visual_context(
        str(keyframes_folder)
    )

    print(f"🟢 Vision Context : {time.time()-start:.2f} sec")

    update_progress(82, "👀 Understanding Visual Context")

    # --------------------------------
    # Step 7 - Build Timeline
    # --------------------------------
    start = time.time()

    timeline = build_timeline(
        video_name=video_name,
        frame_count=frame_count,
        keyframe_count=keyframe_count,
        transcript=transcript,
        detected_language=detected_language,
        visual_context=visual_context,
        ocr_text=ocr_text,
    )

    save_timeline(
        timeline,
        str(timeline_file)
    )

    print(f"🟢 Timeline : {time.time()-start:.2f} sec")

    update_progress(90, "🧠 Understanding Story")

    # --------------------------------
    # Step 8 - AI Analysis
    # --------------------------------
    start = time.time()

    ai_analysis = analyze_video(
        str(timeline_file)
    )

    print(f"🟢 AI Reasoning : {time.time()-start:.2f} sec")

    update_progress(98, "✨ Generating Captions")

    with open(report_file, "w", encoding="utf-8") as f:
        json.dump(
            ai_analysis,
            f,
            indent=4,
            ensure_ascii=False
        )

    update_progress(100, "✅ Completed")

    print(f"\n🚀 TOTAL PIPELINE TIME : {time.time()-total_start:.2f} sec\n")

    # --------------------------------
    # Return Results
    # --------------------------------
    return {
        "video_name": video_name,
        "frames": frame_count,
        "keyframes": keyframe_count,
        "detected_language": detected_language,
        "visual_context": visual_context,
        "audio": str(audio_file),
        "transcript": str(transcript_file),
        "timeline": str(timeline_file),
        "report": str(report_file),
        "analysis": ai_analysis,
    }