def format_prompt(id,prompt,noise_level):
    with open("prompt/prompt.txt", "r") as f: 
        template = f.read()
    
    formatted_prompt = template.replace("{id}", id).replace("{prompt}", prompt).replace("{noise_level}", noise_level)
    return formatted_prompt

import os 
import re
import json

from utils.calls import GroqChat, GeminiChat
from index.store import BaseFaissIndex
from utils.base import build_base_database

START_INDEX = 5609

if __name__ == "__main__":
    if os.path.exists("base_adhd_dataset.json"): 
        print("✅ Base dataset found: 'base_adhd_dataset.json'")
    else:
        print("⚠ Base dataset not found. Building base database...")
        build_base_database()
        print("✅ Base database created.")

    index = BaseFaissIndex()
    llm = GeminiChat()

    with open("base_adhd_dataset.json", "r") as f: 
        data = json.load(f)
    print(f"📂 Loaded base dataset with {len(data)} entries.")

    with open("final_adhd_dataset.json", "a") as fh:
        for count, obj in enumerate(data[START_INDEX-1:], start=START_INDEX):
            prompt = obj["prompt"]
            exists = index.search_text(prompt)
            
            if exists: 
                print(f"[{count}] ❌ Prompt already exists in vector store, skipping: {prompt[:50]}...")
                pass 
            else: 
                index.add_text(prompt)
                print(f"[{count}] ✅ Added prompt to vector store: {prompt[:50]}...")

            noise_level = obj["noise_level"]

            formatted_prompt = format_prompt(
                f"adhd_{count}",
                prompt=prompt, 
                noise_level=noise_level
            )
            
            print(f"[{count}] 💬 Sending prompt to LLM...")
            try: 
                response = llm.ask(formatted_prompt)
            except: 
                pass

            # Strip code fences
            cleaned = re.sub(r"```[a-z]*\n", "", response)
            cleaned = cleaned.replace("```", "").strip() 

            try:
                json_obj = json.loads(cleaned)
                fh.write(json.dumps(json_obj) + "\n")
                print(f"[{count}] ✅ JSON written to file.")
            except json.JSONDecodeError:
                print(f"[{count}] ⚠ JSON decode failed, trying fallback parsing...")
                start, end = response.find("{"), response.rfind("}")
                try:
                    json_obj = json.loads(response[start:end+1])
                    fh.write(json.dumps(json_obj) + "\n")
                    print(f"[{count}] ✅ JSON written using fallback parsing.")
                except json.JSONDecodeError:
                    print(f"[{count}] ❌ Failed to parse JSON even with fallback. Skipping entry.")