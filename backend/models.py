# backend/models.py

import json
from typing import List, Dict
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from .db_config import Base

class ModelManager:
    def __init__(self, file_path: str = 'models/models.json'):
        self.file_path = file_path
        self.models = self.load_models()

    def load_models(self) -> List[Dict]:
        with open(self.file_path, 'r') as json_file:
            data = json.load(json_file)
        return data['data']

    def get_model_names(self) -> List[str]:
        return [model['id'] for model in self.models]

class Prompt(Base):
    __tablename__ = "prompts"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String, nullable=False)
    role = Column(String, nullable=False)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())