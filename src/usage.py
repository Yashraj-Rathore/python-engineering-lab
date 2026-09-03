records = [
    {"project_id": "p1", "tokens": 100},
    {"project_id": "p1", "tokens": 150},
    {"project_id": "p2", "tokens": 50},
]


def summarize_usage(records):
    total_requests = len(records)
    total_tokens=0
    for record in records:
        total_tokens+=record["tokens"]

    return {"total_requests": total_requests, "total_tokens": total_tokens}

