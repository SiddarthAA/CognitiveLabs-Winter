import json

input_file = "final_adhd_dataset.json"    # your current file (NDJSON style)
output_file = "final_adhd_dataset-clean.json"

# Read all objects from NDJSON
data = []
with open(input_file, "r", encoding="utf-8") as f:
    for line in f:
        if line.strip():  # skip empty lines
            data.append(json.loads(line))

# Write as pretty JSON array
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"Reformatted {len(data)} entries into {output_file}")