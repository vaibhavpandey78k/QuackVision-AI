from pathlib import Path

from app.video.frame_extractor import extract_frames
from app.video.scene_detector import detect_keyframes
from app.pipeline.audio_extractor import extract_audio


def process_video(video_path: str):
    """
    Main AI processing pipeline.
    """

    video_path = Path(video_path)

    uploads = video_path.parent
    video_name = video_path.stem

    frames_folder = uploads / "frames" / video_name
    keyframes_folder = uploads / "keyframes" / video_name
    audio_folder = uploads / "audio"

    audio_file = audio_folder / f"{video_name}.wav"

    # Step 1 - Extract Frames
    frame_count = extract_frames(
        str(video_path),
        str(frames_folder)
    )

    # Step 2 - Detect Key Frames
    keyframe_count = detect_keyframes(
        str(frames_folder),
        str(keyframes_folder)
    )

    # Step 3 - Extract Audio
    extract_audio(
        str(video_path),
        str(audio_file)
    )

    return {
        "frames": frame_count,
        "keyframes": keyframe_count,
        "audio": str(audio_file),
        "video_name": video_name
    }