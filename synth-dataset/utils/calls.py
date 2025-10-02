from groq import Groq
from google import genai

class GroqChat:
    def __init__(self):
        self.client = Groq(api_key="") #inset Groq API
        self.model = "gemma2-9b-it"

    def ask(self, prompt: str) -> str:
        chat_completion = self.client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model=self.model
        )
        return chat_completion.choices[0].message.content

class GeminiChat: 
    def __init__(self):
        self.client = genai.Client(api_key="") #insert Gemini API
    
    def ask(self, query, model="gemini-2.5-flash-lite"):
        response = self.client.models.generate_content(
            model=model,
            contents=query
        )
        return response.text