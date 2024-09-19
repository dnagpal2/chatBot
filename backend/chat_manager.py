# backend/chat_manager.py

from .api_client import GroqAPIClient
from .db_config import get_db
from .models import Prompt
from sqlalchemy.orm import Session

class ChatManager:
    def __init__(self):
        self.api_client = GroqAPIClient()
        self.db: Session = next(get_db())
        self.conversation_history = self.load_conversation_history()

    def load_conversation_history(self):
        prompts = self.db.query(Prompt).order_by(Prompt.timestamp).all()
        return [{"role": p.role, "content": p.content} for p in prompts]

    def add_message(self, role: str, content: str):
        prompt = Prompt(role=role, content=content)
        self.db.add(prompt)
        self.db.commit()
        self.conversation_history.append({"role": role, "content": content})

    def get_bot_response(self, model: str) -> str:
        response = self.api_client.chat_completion(model, self.conversation_history)
        bot_message = response['choices'][0]['message']['content']
        self.add_message("assistant", bot_message)
        return bot_message

    def clear_history(self):
        self.db.query(Prompt).delete()
        self.db.commit()
        self.conversation_history = []

    def get_prompts(self):
        return self.db.query(Prompt).all()