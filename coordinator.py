from agents import Runner, trace

from research_agents.law_researcher import law_research_agent
from research_agents.legal_case_receiver import legal_case_receiver_agent
from research_agents.output_organizer import output_organizer_agent
from research_agents.query_agent import query_agent


class ResearchCoordinator:
    def __init__(self, query: str):
        self.query = query

    async def research(self) -> str:
        with trace("Legal assist workflow"):
            receiver_response = await self.receive_legal_case()

            law_researcher_response = await self.research_relevant_laws(receiver_res=receiver_response.final_output)

            context = f"\nBản tóm tắt tình huống pháp lý và câu hỏi người dùng: {receiver_response.final_output}\n Các điều luật liên quan: {law_researcher_response.final_output}"

            final_output_res = await self.organise_output(context=context)

            return final_output_res.final_output

    async def receive_legal_case(self) -> str:
        result = await Runner.run(legal_case_receiver_agent, input=self.query)

        return result

    async def research_relevant_laws(self, receiver_res: str):
        res = await Runner.run(law_research_agent, input=receiver_res)

        return res

    async def organise_output(self, context: str):
        res = await Runner.run(output_organizer_agent, input=context)

        return res