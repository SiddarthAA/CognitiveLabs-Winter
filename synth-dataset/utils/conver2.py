import json

# input + output file paths
input_file = "final_adhd_dataset-clean.json"
output_file = "final_adhd_dataset-train.json"  # JSONL format is better for training


# load the full array
with open(input_file, "r") as f:
    data = json.load(f)

print(f"📂 Loaded {len(data)} entries")

# transform into training format
train_data = []
for obj in data:
    if "prompt" in obj and "completion_structured" in obj:
        train_entry = {
            "prompt": obj["prompt"],
            "completion": obj["completion_structured"]
        }
        train_data.append(train_entry)

# save as JSONL
with open(output_file, "w") as f:
    for entry in train_data:
        f.write(json.dumps(entry) + "\n")

print(f"✅ Converted {len(train_data)} entries into training format at {output_file}")