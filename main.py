import asyncio
from dotenv import load_dotenv
from coordinator import ResearchCoordinator

load_dotenv()

example_legal_case = """Gần nhà em có đám trung tâm aerobic sáng nào 5 giờ cũng hú hét bật nhạc đùng đùng. Gọi điện báo công an xã chục lần nhiều ngày cũng không thấy ai ra làm việc. Có ai có cách nào cho em xin tham khảo ý kiến ạ. (Do ảnh hưởng đến người già và trẻ nhỏ. Mấy người đó ý thức kém nên nói chuyện cũng không ăn thua ạ - họ còn kêu phá việc làm ăn của họ)"""

async def main(query: str):
    research_coordinator = ResearchCoordinator(query=query)
    report = await research_coordinator.research()
    return report

if __name__ == "__main__":
    asyncio.run(main())