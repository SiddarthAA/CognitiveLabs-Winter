import json

# input + output file paths
input_file = "final_adhd_dataset-clean.json"   # your original big JSON
output_file = "final_adhd_dataset-train2.json"       # one single JSON array

# load the full array
with open(input_file, "r") as f:
    data = json.load(f)

print(f"📂 Loaded {len(data)} entries")

# transform into training format
train_data = []
for obj in data:
    if "prompt" in obj and "completion_structured" in obj:
        train_entry = {
            "instruction": "Organize the messy input into a structured task list.",
            "input": obj["prompt"],
            "output": obj["completion_structured"]
        }
        train_data.append(train_entry)

# save as one single JSON array
with open(output_file, "w") as f:
    json.dump(train_data, f, indent=2)

print(f"✅ Saved {len(train_data)} entries into one JSON array at {output_file}")