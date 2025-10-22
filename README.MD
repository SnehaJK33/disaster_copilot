Here’s the cleaned-up, star/hashtag-free version of your README, ready for submission:

---

Disaster Relief Agent

Hackathon: Composio x DevClub IITD x Chirality Labs – Agents in Production

Project Overview

The Disaster Relief Agent is a workflow automation system designed to fetch, summarize, and present disaster reports. The agent:

1. Fetches disaster-related emails/reports.
2. Summarizes each report using OpenAI GPT-4o-mini.
3. Logs the reports in a CSV file.
4. Generates a PDF summary report.
5. Displays the reports interactively on a dashboard.

Goal: Help authorities and citizens quickly understand emerging disaster situations and take timely action.

Demo

Dashboard Screenshot: (Add image here if available)
Video Demo: 1-2 minute video showcasing report fetching, summarization, PDF generation, and dashboard display.

Installation Instructions

1. Clone the repository

```bash
git clone <your-github-repo-link>
cd disaster_copilot
```

2. Create a virtual environment

```bash
python -m venv .venv
source .venv/Scripts/activate   # Windows
# OR
source .venv/bin/activate       # Linux/Mac
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Set environment variables
   Create a .env file:

```
OPENAI_API_KEY=your_openai_api_key
COMPOSIO_API_KEY=your_composio_api_key  # Optional / for future Tool Router integration
```

Running the Project

1. Fetch and process reports

```bash
python run_all.py
```

This will fetch sample disaster emails, summarize them, update the CSV, generate a PDF, and display alerts.

2. Launch the dashboard

```bash
python app.py
```

Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser to view reports.

Project Features

* Automated disaster report summarization
* CSV and PDF logging
* Interactive web dashboard
* Slack-style alerts (console output)
* Ready for future Composio Tool Router integration

Friction Log

We encountered issues with the Composio Tool Router integration:

1. Tool Router Import Errors – SDK version mismatch prevented importing ToolRouter.
2. Tool Execution Failures – Calls like Tools.execute() failed due to API mismatches.
3. Frontend Loading Issues – CSS/JS not loading until static folder structure was fixed.

Solution/Workaround:

* Fallback to OpenAI GPT-4o-mini for summarization.
* Created mock Tool Router functions to simulate multi-tool workflows.
* Corrected static file linking for a polished dashboard.

Full Friction Log: Friction_Log.md

Future Work

* Full Composio Tool Router integration once SDK issues are resolved
* Automate multi-step tasks across multiple tools (emails, calendars, notifications)
* Predictive disaster analysis and enhanced dashboard visualizations

Team

* Sneha Mohalanobish – Project Lead
  (Add other team members if any)

Notes

* Project is fully executable locally with OpenAI fallback.
* Ready for hackathon submission even without Tool Router integration.

---

If you want, I can **create a ready-to-submit GitHub folder structure** including `run_all.py`, `app.py`, `requirements.txt`, `Friction_Log.md`, `README.md`, and the `static/` folder, so you can push it directly for the hackathon.

Do you want me to do that?
