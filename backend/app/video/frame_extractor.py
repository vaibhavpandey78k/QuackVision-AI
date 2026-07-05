import cv2
from pathlib import Path

def extract_frames(video_path: str, output_folder: str, interval: int = 30):
    output_path = Path(output_folder)
    output_path.mkdir(parents=True, exist_ok=True)

    cap = cv2.VideoCapture(video_path)

    frame_count = 0
    saved_count = 0

    while True:
        success, frame = cap.read()

        if not success:
            break

        if frame_count % interval == 0:
            filename = output_path / f"frame_{saved_count:04d}.jpg"
            cv2.imwrite(str(filename), frame)
            saved_count += 1

        frame_count += 1

    cap.release()

    return saved_count