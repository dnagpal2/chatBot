import os
from dotenv import load_dotenv
from backend.api_client import GroqAPIClient

load_dotenv()

def update_models():
    client = GroqAPIClient()
    client.save_models_to_file()

if __name__ == "__main__":
    update_models()
    print("Models updated successfully!")