def human_approval(state):
    print("\n--- Human Approval Required ---")

    email_options = [
        "gshk02@gmail.com",
        "gavinshk07@gmail.com"
    ]

    # Default recipient for assignment
    default_recipient = "Yilin.Huang@smu.ca"

    # Initialize state if missing
    if not state.get("sender_email"):
        state["sender_email"] = email_options[0]

    if not state.get("recipient_email"):
        state["recipient_email"] = default_recipient

    while True:
        print("\n----------------------------------------")
        print("Draft Email Preview")
        print("----------------------------------------")
        print(f"From: {state['sender_email']}   [switch]")
        print(f"To:   {state['recipient_email']}   [edit]")
        print("----------------------------------------")

        print("\nOptions:")
        print("1 → Approve & Send")
        print("2 → Cancel")
        print("3 → Switch Sender")
        print("4 → Edit Recipient")

        choice = input("\nSelect option (1–4): ").strip()

        if choice == "1":
            state["approved"] = True
            return state

        elif choice == "2":
            state["approved"] = False
            return state

        elif choice == "3":
            current = state["sender_email"]
            new_sender = email_options[1] if current == email_options[0] else email_options[0]
            state["sender_email"] = new_sender
            print(f"\nSender switched to: {new_sender}")

        elif choice == "4":
            new_recipient = input("Enter new recipient email: ").strip()
            state["recipient_email"] = new_recipient
            print(f"\nRecipient updated to: {new_recipient}")

        else:
            print("Invalid selection.")
