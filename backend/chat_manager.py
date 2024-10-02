# backend/chat_manager.py

from .api_client import GroqAPIClient
from datetime import datetime

class ChatManager:
    def __init__(self):
        self.api_client = GroqAPIClient()
        self.conversation_history = []
        self.all_prompts = []

    def add_message(self, role: str, content: str):
        timestamp = datetime.now().isoformat()
        self.conversation_history.append({"role": role, "content": content})
        self.all_prompts.append({"timestamp": timestamp, "role": role, "content": content})

    def get_bot_response(self, model: str) -> str:
        response = self.api_client.chat_completion(model, self.conversation_history)
        bot_message = response['choices'][0]['message']['content']
        self.add_message("assistant", bot_message)
        return bot_message

    def clear_history(self):
        self.conversation_history = []
        self.all_prompts = []

    def get_prompts(self):
        return self.all_prompts