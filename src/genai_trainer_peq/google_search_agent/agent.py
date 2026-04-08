"""Google Search Agent definition for ADK Bidi-streaming demo."""

from google.adk.agents import Agent
from google.adk.tools import google_search
from genai_trainer_peq.config.settings import get_settings

settings = get_settings()

# Default models for Live API with native audio support:
# - Gemini Live API: gemini-2.5-flash-native-audio-preview-12-2025
# - Vertex AI Live API: gemini-live-2.5-flash-native-audio
agent = Agent(
    name="google_search_agent",
    model=settings.gemini_model,
    tools=[google_search],
    instruction="You are a helpful assistant that can search the web.",
)
