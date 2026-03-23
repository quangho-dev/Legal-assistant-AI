from agents import Agent
from pydantic import BaseModel

from config.groq_config import GROQ_LLAMA_MODEL

OUTPUT_ORGANIZER_AGENT_PROMPT = """Bạn là một agent chuyên viết ra câu trả lời cuối cùng cho người dùng đối với tình huống pháp lý, câu hỏi được cung cấp và danh sách các điều luật liên quan đến tình huống pháp lý đó.
"""

# class ReceiverResponse(BaseModel):
#     legal_case_summary: str
#     questions_of_user: list[str]

output_organizer_agent = Agent(
    name="Output organizer",
    instructions=OUTPUT_ORGANIZER_AGENT_PROMPT,
    model=GROQ_LLAMA_MODEL)