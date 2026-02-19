def collect_intent(state):
    print("\n--- Collecting User Intent ---\n")
    user_input = input("Enter your proposal request: ")
    state["user_intent"] = user_input
    state["positioning_mode"] = "governance"
    return state
