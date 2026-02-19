from dotenv import load_dotenv
import os

load_dotenv()

from app.graph import build_graph

if __name__ == "__main__":
    graph = build_graph()
    graph.invoke({})
