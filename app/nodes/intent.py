def collect_intent(state):
    """
    Collect user intent from incoming API state.
    This version is web-safe (no input(), no blocking).
    """

    print("\n--- Collecting User Intent (API Mode) ---\n")

    user_input = state.get("user_input")

    if not user_input:
        raise ValueError("user_input is missing from state.")

    state["user_intent"] = user_input
    state["positioning_mode"] = "governance"

    return state
