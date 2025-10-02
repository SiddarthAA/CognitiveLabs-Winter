# ADHD Task-Planning Synthetic Dataset

## Overview
The **ADHD Task-Planning Synthetic Dataset** (~12–15k entries) transforms fragmented, ADHD-style prompts into **structured task plans** (`completion_structured`) with concise **prompt summaries** (`prompt_summary`) and rich **metadata**. Each entry captures realistic, multi-step, task-planning scenarios, designed to fine-tune LLaMA 3 1B for **coherent, multi-step reasoning**.

The dataset is stored in `final_adhd_dataset.json` and is fully **schema-compliant**, ensuring high-quality, diverse, and research-ready entries.

---

## Schema

Each entry in the dataset follows this structure:

| Key | Type | Description |
| --- | --- | --- |
| `id` | string | Unique identifier for each entry (e.g., `adhd_001`) |
| `prompt` | string | Fragmented, ADHD-style task prompt |
| `prompt_summary` | string | Concise summary of what the prompt actually means |
| `completion_structured` | string | Clear, actionable, step-by-step task plan |
| `metadata` | object | Extra information for filtering and analysis |
| `metadata.domain` | string | Task domain (e.g., `task_planning`) |
| `metadata.noise_level` | string | Level of fragmentation/noise: `low` / `medium` / `high` |
| `metadata.style` | string | Cognitive style: `adhd` |
| `metadata.tags` | list of strings | Descriptive labels for evaluation and analysis |

---

## Usage

This dataset is designed for **text-to-text generation** tasks, particularly **fine-tuning LLMs** like LLaMA 3 1B. Example usage:

```python
from datasets import load_dataset

dataset = load_dataset("SiddarthAhhh/ADHD_TaskPlanning-Synthetic")

for entry in dataset['train']:
    print("Prompt:", entry['prompt'])
    print("Structured Completion:", entry['completion_structured'])
````

The dataset can help LLaMA 3 1B learn to **convert messy, fragmented input into coherent, actionable guidance**.

---

## License

This dataset is released under **CC BY 4.0**. Attribution is required for any usage or redistribution.

---