from reasoning_engine import load_timeline, build_prompt

data = load_timeline("demo.json")

prompt = build_prompt(data)

print(prompt)