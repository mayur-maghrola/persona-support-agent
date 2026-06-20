import json

SENSITIVE_KEYWORDS = [
    "billing",
    "refund",
    "chargeback",
    "legal",
    "lawsuit",
    "account hacked",
    "account modification"
]


def should_escalate(
    query,
    retrieved_docs
):

    query_lower = query.lower()

    if len(retrieved_docs) == 0:
        return True

    for keyword in SENSITIVE_KEYWORDS:

        if keyword in query_lower:
            return True

    return False


def generate_handoff_summary(
    persona,
    query,
    retrieved_docs
):

    handoff = {
        "persona": persona,
        "issue": query,
        "documents_used": [
            doc["source"]
            for doc in retrieved_docs
        ],
        "attempted_steps": [
            "Knowledge Base Retrieval",
            "AI Generated Response"
        ],
        "recommendation":
        "Human review required."
    }

    return json.dumps(
        handoff,
        indent=4
    )