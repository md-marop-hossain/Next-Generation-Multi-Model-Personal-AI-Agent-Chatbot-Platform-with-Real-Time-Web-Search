# ========================== #
# Step 1: Setup API Keys
# ========================== #
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# ========================== #
# Step 2: Setup LLMs & Tools
# ========================== #
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults

# Default LLM instances (used as fallbacks or for testing)
openai_llm = ChatOpenAI(model="gpt-4o-mini")
groq_llm = ChatGroq(model="llama-3.3-70b-versatile")

# Tavily search tool for web augmentation
search_tool = TavilySearchResults(max_results=2)

# ========================== #
# Step 3: Setup AI Agent Logic
# ========================== #
from langgraph.prebuilt import create_react_agent
from langchain_core.messages.ai import AIMessage

# Default system prompt
system_prompt = "Act as an AI chatbot who is smart and friendly"

# Function to generate a response from AI agent
def get_response_from_ai_agent(llm_id, query, allow_search, system_prompt, provider):
    # Select appropriate model based on provider
    if provider == "Groq":
        llm = ChatGroq(model=llm_id)
    elif provider == "OpenAI":
        llm = ChatOpenAI(model=llm_id)

    # Enable tools if web search is allowed
    tools = [TavilySearchResults(max_results=2)] if allow_search else []

    # Create LangGraph AI agent with model and tools
    agent = create_react_agent(
        model=llm,
        tools=tools,
        state_modifier=system_prompt
    )

    # Construct the input state with the user's message history
    state = {"messages": query}

    # Get response from the agent
    response = agent.invoke(state)

    # Extract only AI-generated messages
    messages = response.get("messages")
    ai_messages = [message.content for message in messages if isinstance(message, AIMessage)]

    # Return the last AI response
    return ai_messages[-1]
