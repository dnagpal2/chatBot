import requests
import json
from typing import Dict, Any
import os
from dotenv import load_dotenv

load_dotenv()

class GroqAPIClient:
    def __init__(self):
        self.api_key = os.getenv('GROQ_API_KEY')
        self.base_url = "https://api.groq.com/openai/v1"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def get_models(self) -> Dict[str, Any]:
        url = f"{self.base_url}/models"
        response = requests.get(url, headers=self.headers)
        return response.json()

    def chat_completion(self, model: str, messages: list) -> Dict[str, Any]:
        url = f"{self.base_url}/chat/completions"
        payload = {
            "model": model,
            "messages": messages
        }
        response = requests.post(url, headers=self.headers, json=payload)
        return response.json()

    def save_models_to_file(self, file_path: str = 'models/models.json'):
        data = self.get_models()
        with open(file_path, 'w') as json_file:
            json.dump(data, json_file, indent=4)