from agents import Agent
from pydantic import BaseModel

from config.groq_config import GROQ_LLAMA_MODEL

LEGAL_CASE_RECEIVER_AGENT_PROMPT = """Bạn là một chuyên viên tiếp nhận các tình huống pháp lý. Hãy phân tích tình huống pháp lý và hiểu rõ câu hỏi của người dùng. Kết quả trả về là một tóm tắt về tình huống pháp lý đó, trong đó bao gồm các ý quan trọng và câu hỏi của người dùng. Bảng tóm tắt này dùng để chuyển cho chuyên viên nghiên cứu các luật liên quan đến tình huống pháp lý đó.
"""

# class ReceiverResponse(BaseModel):
#     legal_case_summary: str
#     questions_of_user: list[str]

legal_case_receiver_agent = Agent(
    name="Legal case receiver",
    instructions=LEGAL_CASE_RECEIVER_AGENT_PROMPT,
    model=GROQ_LLAMA_MODEL)