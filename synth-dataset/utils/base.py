import json
import random

def build_base_database():
    # Building blocks
    actions = ["submit", "call", "clean", "finish", "email", "organize", "plan", "check", "prep", "buy"]
    objects = ["report", "mom", "room", "assignment", "groceries", "laundry", "presentation", "project", "notes", "schedule"]
    fillers = ["maybe", "I should probably", "oh", "but also", "…", "and then", "I forgot to"]
    noise_levels = ["low", "medium", "high"]

    # Step 1: Generate 1000 base templates
    base_templates = []
    for _ in range(1000):
        n_tasks = random.randint(2, 5)
        tasks = []
        for _ in range(n_tasks):
            task = f"{random.choice(actions)} {random.choice(objects)}"
            if random.random() < 0.5:
                task = f"{random.choice(fillers)} {task}"
            tasks.append(task)
        prompt = ", ".join(tasks) + "…"
        base_templates.append(prompt)

    # Step 2: Apply noise
    def apply_noise(prompt, level):
        words = prompt.split(", ")
        if level == "low":
            return ", ".join(words) + "."
        elif level == "medium":
            for i in range(len(words)):
                if random.random() < 0.5:
                    words[i] = random.choice(fillers) + " " + words[i]
            return ", ".join(words) + "…"
        elif level == "high":
            for i in range(len(words)):
                if random.random() < 0.7:
                    words[i] = random.choice(fillers) + " " + words[i]
            random.shuffle(words)
            return ", ".join(words) + "…"

    # Step 3: Generate dataset with variations
    dataset_entries = []
    variations_per_template = 5  # <--- ensures expansion to 12k–15k

    for template in base_templates:
        for level in noise_levels:
            for _ in range(variations_per_template):
                tasks = template.split(", ")
                random.shuffle(tasks)
                noisy_prompt = apply_noise(", ".join(tasks), level)
                dataset_entries.append({
                    "prompt": noisy_prompt,
                    "noise_level": level
                })

    # Step 4: Shuffle and trim to 12k–15k
    random.shuffle(dataset_entries)
    final_size = random.randint(12000, 15000)
    dataset_entries = dataset_entries[:final_size]

    # Step 5: Save
    with open("base_adhd_dataset.json", "w") as f:
        json.dump(dataset_entries, f, indent=2)

    print(f"✅ Generated {len(dataset_entries)} entries -> saved to base_adhd_dataset.json")