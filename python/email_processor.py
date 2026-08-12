import re


def analyze_email(sender, subject, body):
    """
    Basic email processing function.
    Classifies an email based on keywords and assigns priority.
    """

    text = f"{subject} {body}".lower()

    if any(word in text for word in ["job", "interview", "recruiter", "career"]):
        category = "Job Opportunity"
        priority = "High"

    elif any(word in text for word in ["invoice", "payment", "bill"]):
        category = "Finance"
        priority = "Medium"

    elif any(word in text for word in ["meeting", "schedule", "calendar"]):
        category = "Meeting"
        priority = "Medium"

    else:
        category = "General"
        priority = "Low"

    return {
        "sender": sender,
        "subject": subject,
        "category": category,
        "priority": priority,
        "summary": body[:150]
    }


if __name__ == "__main__":

    result = analyze_email(
        "recruiter@example.com",
        "Interview Opportunity",
        "We would like to schedule an interview with you."
    )

    print("Email Analysis")
    print("----------------")
    print(f"Sender   : {result['sender']}")
    print(f"Subject  : {result['subject']}")
    print(f"Category : {result['category']}")
    print(f"Priority : {result['priority']}")
    print(f"Summary  : {result['summary']}")
