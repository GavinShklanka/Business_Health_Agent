import os
print("Working directory:", os.getcwd())

import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv


load_dotenv()


def send_email_node(state):
    print("\n--- Sending Email with Attachment ---\n")

    sender_email = os.getenv("SENDER_EMAIL")
    receiver_email = state.get("recipient_email")
    app_password = os.getenv("GMAIL_APP_PASSWORD")
    draft_email = state.get("draft_email")

    msg = EmailMessage()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = "PhD Inquiry – AI Governance and Enterprise Decision Systems"
    msg.set_content(draft_email)

    attachment_added = False
    pdf_path = "Business_Health_App_Market_Analysis_Proposal_Polished.pdf"

    print("Working directory:", os.getcwd())
    print("Looking for:", pdf_path)

    if os.path.exists(pdf_path):
        print("File FOUND.")
        with open(pdf_path, "rb") as f:
            msg.add_attachment(
                f.read(),
                maintype="application",
                subtype="pdf",
                filename=os.path.basename(pdf_path),
            )
        attachment_added = True
    else:
        print("File NOT found.")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, app_password)
        server.send_message(msg)

    print("Email sent.")
    return state
