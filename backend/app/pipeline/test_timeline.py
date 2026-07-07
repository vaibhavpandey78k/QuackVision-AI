from timeline_builder import build_timeline, save_timeline

timeline = build_timeline(
    video_name="demo.mp4",
    frame_count=120,
    keyframe_count=15,
    transcript="Today we are discussing Artificial Intelligence.",
    ocr_text=[
        "Introduction",
        "Machine Learning",
        "Deep Learning"
    ]
)

save_timeline(timeline, "demo.json")

print(timeline)