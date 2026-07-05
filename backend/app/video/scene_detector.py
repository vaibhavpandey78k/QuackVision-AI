import cv2
from pathlib import Path


def detect_keyframes(
    frames_folder: str,
    output_folder: str,
    threshold: float = 25.0,
):
    """
    Saves only frames where a major scene change occurs.
    """

    frames_folder = Path(frames_folder)
    output_folder = Path(output_folder)

    output_folder.mkdir(parents=True, exist_ok=True)

    frame_list = sorted(frames_folder.glob("*.jpg"))

    if len(frame_list) == 0:
        return 0

    previous = cv2.imread(str(frame_list[0]))

    # Always save the first frame
    cv2.imwrite(
        str(output_folder / frame_list[0].name),
        previous,
    )

    saved = 1

    for frame in frame_list[1:]:

        current = cv2.imread(str(frame))

        difference = cv2.absdiff(previous, current)

        score = difference.mean()

        if score > threshold:

            cv2.imwrite(
                str(output_folder / frame.name),
                current,
            )

            saved += 1

        previous = current

    return saved