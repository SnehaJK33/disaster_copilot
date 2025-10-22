import os
import pandas as pd
from dotenv import load_dotenv
from openai import OpenAI
from fpdf import FPDF

# -----------------------------
# Load environment variables
# -----------------------------
load_dotenv()
OPENAI_KEY = os.getenv("OPENAI_API_KEY")

# -----------------------------
# Initialize OpenAI client
# -----------------------------
client = OpenAI(api_key=OPENAI_KEY)

# -----------------------------
# Files and directories
# -----------------------------
CSV_FILE = "data/disaster_logs.csv"
PDF_FILE = "reports/daily_disaster_report.pdf"

os.makedirs("data", exist_ok=True)
os.makedirs("reports", exist_ok=True)

# -----------------------------
# Functions
# -----------------------------
def fetch_disaster_emails():
    """Dummy disaster emails for demo"""
    return [
        {"subject": "Flood in Ward 3", "snippet": "Water levels rising quickly; evacuation needed"},
        {"subject": "Cyclone Warning", "snippet": "High winds expected; prepare emergency teams"}
    ]

def summarize_report(text):
    """Summarize disaster report using OpenAI GPT-4o-mini"""
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are an assistant that summarizes disaster reports in 1-2 sentences."},
                {"role": "user", "content": text}
            ],
            temperature=0.2
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print("⚠️ Error summarizing:", e)
        return text

def send_slack_alert(message):
    """Print alert instead of Slack for demo"""
    print(f"🚨 Slack alert: {message}")

def generate_pdf(summaries):
    """Generate PDF from summaries"""
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    for s in summaries:
        pdf.multi_cell(0, 10, f"{s['title']}\n{s['summary']}\n\n")
    pdf.output(PDF_FILE)
    print(f"PDF report saved to {PDF_FILE}")

# -----------------------------
# Main Workflow
# -----------------------------
def main():
    print("🔹 Fetching disaster emails...")
    emails = fetch_disaster_emails()

    # Load existing CSV or create new with correct columns
    if os.path.exists(CSV_FILE):
        df = pd.read_csv(CSV_FILE)
        for col in ["title", "summary"]:
            if col not in df.columns:
                df[col] = ""
    else:
        df = pd.DataFrame(columns=["title", "summary"])

    new_entries = []
    for email in emails:
        summary = summarize_report(email["snippet"])

        if email["subject"] in df['title'].values:
            # Update summary for existing title
            df.loc[df['title'] == email["subject"], 'summary'] = summary
        else:
            # Add new entry
            df = pd.concat([df, pd.DataFrame([{"title": email["subject"], "summary": summary}])], ignore_index=True)
            new_entries.append({"title": email["subject"], "summary": summary})
            send_slack_alert(f"{email['subject']}\n{summary}")

    # Save updated CSV
    df.to_csv(CSV_FILE, index=False)
    print(f"CSV updated: {CSV_FILE}")

    # Generate PDF report
    generate_pdf(df.to_dict(orient="records"))

    print("✅ Demo workflow completed successfully!")

# -----------------------------
# Run the script
# -----------------------------
if __name__ == "__main__":
    main()
