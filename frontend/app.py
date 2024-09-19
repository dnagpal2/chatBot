import streamlit as st
import sys
import os
import json
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from backend.chat_manager import ChatManager
from backend.db_config import engine
from backend.models import Base

# Create database tables
Base.metadata.create_all(bind=engine)

def load_models():
    with open('models/models.json', 'r') as f:
        data = json.load(f)
    return [model['id'] for model in data['data']]

def main():
    st.set_page_config(page_title="Groq Chatbot", page_icon="🤖")
    st.title("Groq Chatbot")

    # Initialize session state
    if 'chat_manager' not in st.session_state:
        st.session_state.chat_manager = ChatManager()

    # Model selection
    models = load_models()
    model = st.selectbox("Select a model:", models)

    # Chat interface
    for message in st.session_state.chat_manager.conversation_history:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    user_input = st.chat_input("Type your message here...")

    if user_input:
        st.session_state.chat_manager.add_message("user", user_input)
        with st.chat_message("user"):
            st.write(user_input)

        with st.chat_message("assistant"):
            bot_response = st.session_state.chat_manager.get_bot_response(model)
            st.write(bot_response)

    # Clear chat button
    if st.button("Clear Chat"):
        st.session_state.chat_manager.clear_history()
        st.rerun()

    # Display all prompts
    if st.button("Show All Prompts"):
        prompts = st.session_state.chat_manager.get_prompts()
        for prompt in prompts:
            st.write(f"{prompt.timestamp}: [{prompt.role}] {prompt.content}")

if __name__ == "__main__":
    main()