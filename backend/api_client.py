import streamlit as st
import requests
import json
from typing import Dict, Any
import os

class GroqAPIClient:
    def __init__(self):
        self.api_key = st.secrets["api_keys"]["groq"]
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
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w') as json_file:
            json.dump(data, json_file, indent=4)

# Example usage in a Streamlit app
def main():
    st.title("Groq API Client Demo")

    client = GroqAPIClient()

    if st.button("Get Available Models"):
        models = client.get_models()
        st.json(models)

    st.subheader("Chat Completion")
    model = st.selectbox("Select Model", ["mixtral-8x7b-32768", "llama2-70b-4096"])
    user_input = st.text_input("Enter your message")
    
    if st.button("Send"):
        messages = [{"role": "user", "content": user_input}]
        response = client.chat_completion(model, messages)
        st.json(response)

    if st.button("Save Models to File"):
        client.save_models_to_file()
        st.success("Models saved to file!")

if __name__ == "__main__":
    main()