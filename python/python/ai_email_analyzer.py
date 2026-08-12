import os
from openai import OpenAI


def analyze_email(sender, subject, body):
    """
    Analyze an email using an AI model and return
    its category, priority, summary, and suggested action.
    """

    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    prompt = f"""
You are an email analysis assistant.

Analyze the following email:

Sender: {sender}
Subject: {subject}
Body: {body}

Return the following:
1. Category
2. Priority (High, Medium, or Low)
3. Short summary
4. Suggested action

Keep the response concise.
"""

    response = client.responses.create(
        model="gpt-4o-mini",
        input=prompt
    )

    return response.output_text


if __name__ == "__main__":
    result = analyze_email(
        sender="recruiter@example.com",
        subject="Interview Opportunity",
        body="We would like to schedule an interview with you."
    )

    print("AI Email Analysis")
    print("-----------------")
    print(result)
