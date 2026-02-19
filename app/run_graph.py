from app.graph import build_graph

if __name__ == "__main__":
    graph = build_graph()

    # Example test state
    state = {
        "user_input": "Test run",
        "parameters": {}
    }

    result = graph.invoke(state)
    print(result)
