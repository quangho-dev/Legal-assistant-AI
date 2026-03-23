from dotenv import load_dotenv
from agents import AsyncOpenAI, OpenAIChatCompletionsModel
import os

load_dotenv()

groq_key = os.getenv("GROQ_API_KEY")
base_url = os.getenv("BASE_URL_GROQ")

gemini_client = AsyncOpenAI(api_key=groq_key, base_url=base_url)

GROQ_LLAMA_MODEL = OpenAIChatCompletionsModel(model='openai/gpt-oss-20b', openai_client=gemini_client)
