import os
import json
import chainlit as cl
from dotenv import load_dotenv
from typing import Optional, Dict
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from agents.tool import function_tool
from openai.types.responses import ResponseTextDeltaEvent
from agents import Runner
from data import data  
from instructions import instruction

# Load environment variables
load_dotenv()

# Get OpenRouter API config
openrouter_api_key = os.getenv("OPENROUTER_API_KEY")
openrouter_base_url = os.getenv("OPENROUTER_BASE_URL")
openrouter_model = os.getenv("OPENROUTER_MODEL")

# Initialize OpenAI provider with OpenRouter
provider = AsyncOpenAI(
    api_key=openrouter_api_key,
    base_url=openrouter_base_url,
)

# Model configuration
model = OpenAIChatCompletionsModel(model=openrouter_model, openai_client=provider)


# ✅ Function tool to fetch data locally from data.py
@function_tool("get_afaqulislam_data")
def get_afaqulislam_data() -> str:
    """
    Fetches profile data about Afaq Ul Islam from the local data.py file.

    Returns:
        str: JSON string containing Afaq Ul Islam profile information
    """
    try:
        return json.dumps(data, indent=4)
    except Exception as e:
        return f"Error loading Afaq Ul Islam data: {str(e)}"


# ✅ Agent Definition
agent = Agent(
    name="Afaq Info Agent",
    instructions=instruction,
    model=model,
    tools=[get_afaqulislam_data],
)


# ✅ OAuth Callback (if you’re using GitHub login)
@cl.oauth_callback
def oauth_callback(
    provider_id: str,
    token: str,
    raw_user_data: Dict[str, str],
    default_user: cl.User,
) -> Optional[cl.User]:

    # use these print statements for debugging
    # print(f"Provider: {provider_id}")
    # print(f"User data: {raw_user_data}")
    return default_user


# ✅ On Chat Start
@cl.on_chat_start
async def handle_chat_start():
    cl.user_session.set("history", [])
    # await cl.Message(
    #     content="👋 Salam! I'm Afaq Ul Islam's personal AI assistant. You can ask me about his skills, projects, services, and experience."
    # ).send()


# ✅ On Message
@cl.on_message
async def handle_message(message: cl.Message):
    history = cl.user_session.get("history", [])
    history.append({"role": "user", "content": message.content})

    # Create an empty message placeholder on frontend
    msg = cl.Message(content="🔃 Thinking...")
    await msg.send()
    try:
        result = Runner.run_streamed(agent, input=history)

        full_response = ""
        first_token = True

        async for event in result.stream_events():
            if event.type == "raw_response_event" and isinstance(
                event.data, ResponseTextDeltaEvent
            ):
                delta = event.data.delta

                # Only clear "Thinking..." when the first **non-empty token** arrives
                if first_token and delta.strip() != "":
                    msg.content = ""  # Clear placeholder
                    await msg.update()
                    first_token = False

                full_response += delta
                await msg.stream_token(delta)

        await msg.update()

        # Save final response to chat history
        history.append({"role": "assistant", "content": full_response})
        cl.user_session.set("history", history)
    except Exception as e:
        msg.content = f"Error: {e}"
        await msg.update()
        # print("Error:", e)