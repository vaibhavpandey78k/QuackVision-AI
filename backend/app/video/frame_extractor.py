import cv2
from pathlib import Path


def extract_frames(video_path: str, output_folder: str):

    output_path = Path(output_folder)
    output_path.mkdir(parents=True, exist_ok=True)

    cap = cv2.VideoCapture(video_path)

    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    duration = total_frames / fps if fps else 0

    # ----------------------------------------
    # Dynamic Frame Sampling
    # ----------------------------------------

    if duration <= 30:
        target_frames = 5

    elif duration <= 60:
        target_frames = 8

    else:
        target_frames = 10

    interval = max(1, total_frames // target_frames)

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

    print(f"Video Duration : {duration:.1f} sec")
    print(f"Frames Saved   : {saved_count}")

    return saved_count