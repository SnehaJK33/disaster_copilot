from composio_router import send_slack_alert

def alert_team(summary):
    channel = "#disaster-alerts"  # Replace with your Slack channel
    send_slack_alert(channel, summary)
