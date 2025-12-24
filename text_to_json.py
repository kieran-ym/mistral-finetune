import json

INPUT_FILE = "diary of john evelyn.txt"
OUTPUT_FILE = "notes.jsonl"
WORDS_PER_CHUNK = 600  # adjust between 400–800

with open(INPUT_FILE, "r", encoding="utf-8") as f:
    text = f.read()

# Clean up whitespace
text = text.replace("\n", " ").strip()

words = text.split()
chunks = []

for i in range(0, len(words), WORDS_PER_CHUNK):
    chunk = " ".join(words[i:i + WORDS_PER_CHUNK])
    if len(chunk) > 0:
        chunks.append(chunk)

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    for chunk in chunks:
        json_line = {"note": chunk}
        f.write(json.dumps(json_line, ensure_ascii=False) + "\n")

print(f"Created {len(chunks)} entries in {OUTPUT_FILE}")
