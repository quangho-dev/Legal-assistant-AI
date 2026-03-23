from agents import Agent, function_tool
from pydantic import BaseModel
from config.groq_config import GROQ_LLAMA_MODEL
import inngest


def get_inngest_client() -> inngest.Inngest:
    return inngest.Inngest(app_id="rag_app", is_production=False)


@function_tool
async def look_up_relevant_laws(question: str):
    client = get_inngest_client()
    result = await client.send(
        inngest.Event(
            name="rag/query_pdf_ai",
            data={
                "question": question,
                "top_k": 5,
            },
        )
    )

    return result[0]


LAW_RESEARCHER_AGENT_PROMPT = """Bạn là một chuyên viên tra cứu luật. Dựa trên tóm tắt của vụ án được cung cấp và câu hỏi của người dùng, bạn trích dẫn những luật liên quan đến vụ án. Kết quả trả về là trích dẫn các điều luật liên quan đến vụ án đuọc cung cấp. Bạn phải sử dụng tool look_up_relevant_laws.
"""


class LawResearchResponse(BaseModel):
    relevant_laws: list[str]


law_research_agent = Agent(
    name="Law reasearcher",
    instructions=LAW_RESEARCHER_AGENT_PROMPT,
    model=GROQ_LLAMA_MODEL,
    tools=[look_up_relevant_laws],
    # output_type=LawResearchResponse
)
