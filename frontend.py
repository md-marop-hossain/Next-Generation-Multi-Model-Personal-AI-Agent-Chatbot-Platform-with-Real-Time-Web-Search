# ========================== #
# Load Environment Variables
# ========================== #
from dotenv import load_dotenv
load_dotenv()

# ========================== #
# Step 1: Setup UI with Streamlit
# ========================== #
import streamlit as st

# Configure Streamlit page
st.set_page_config(page_title="LangGraph Agent UI", layout="centered")

# Title and description
st.title("AI Chatbot Agents")
st.write("Create and Interact with the AI Agents!")

# Text area for system prompt input
system_prompt = st.text_area(
    "Define your AI Agent: ",
    height=70,
    placeholder="Type your system prompt here..."
)

# Available models grouped by provider
MODEL_NAMES_GROQ = ["llama-3.3-70b-versatile", "mixtral-8x7b-32768"]
MODEL_NAMES_OPENAI = ["gpt-4o-mini", "gpt-4-turbo", "gpt-3.5-turbo"]

# Provider selection radio button
provider = st.radio("Select Provider:", ("Groq", "OpenAI"))

# Select model based on chosen provider
if provider == "Groq":
    selected_model = st.selectbox("Select Groq Model:", MODEL_NAMES_GROQ)
elif provider == "OpenAI":
    selected_model = st.selectbox("Select OpenAI Model:", MODEL_NAMES_OPENAI)

# Option to allow web search tool usage
allow_web_search = st.checkbox("Allow Web Search")

# Text area for user query input
user_query = st.text_area(
    "Enter your query: ",
    height=150,
    placeholder="Ask Anything!"
)

# Backend API URL
API_URL = "http://127.0.0.1:9999/chat"

# ========================== #
# Step 2: Trigger Request to Backend on Button Click
# ========================== #
if st.button("Ask Agent!"):
    if user_query.strip():
        # Import requests locally to avoid global dependency if unused
        import requests

        # Prepare payload for backend API
        payload = {
            "model_name": selected_model,
            "model_provider": provider,
            "system_prompt": system_prompt,
            "messages": [user_query],
            "allow_search": allow_web_search
        }

        # Send POST request to backend
        response = requests.post(API_URL, json=payload)

        # Handle the response
        if response.status_code == 200:
            response_data = response.json()
            if "error" in response_data:
                st.error(response_data["error"])
            else:
                st.subheader("Agent Response")
                st.markdown(f"**Final Response:** {response_data}")
