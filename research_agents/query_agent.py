from agents import Agent

from config.groq_config import GROQ_LLAMA_MODEL

QUERY_AGENT_PROMPT = """Bạn là một trợ lý rất chuyên nghiệp và trung thực. 
"""

query_agent = Agent(
    name="Assistant",
    instructions=QUERY_AGENT_PROMPT,
    model=GROQ_LLAMA_MODEL)