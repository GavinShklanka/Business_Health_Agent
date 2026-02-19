from app.graph import build_graph

class AgentService:

    async def run(self, state: dict):
        graph = build_graph()
        result = await graph.ainvoke(state)
        return result
