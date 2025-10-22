from composio_router import fetch_urgent_emails

def get_disaster_emails():
    emails = fetch_urgent_emails()
    results = []
    for e in emails:
        results.append({
            "subject": e["subject"],
            "snippet": e["snippet"]
        })
    return results
