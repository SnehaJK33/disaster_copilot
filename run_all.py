import os
import pandas as pd
from fpdf import FPDF
from composio_router import process_reports

CSV_FILE = "data/disaster_logs.csv"
PDF_FILE = "reports/daily_disaster_report.pdf"

os.makedirs("data", exist_ok=True)
os.makedirs("reports", exist_ok=True)


def fetch_disaster_emails():
    """Dummy disaster emails for demo"""
    return [
        {"subject": "Flood in Ward 3", "snippet": "Water levels rising quickly; evacuation needed"},
        {"subject": "Cyclone Warning", "snippet": "High winds expected; prepare emergency teams"}
    ]


def generate_pdf(summaries):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    for s in summaries:
        pdf.multi_cell(0, 10, f"{s['title']}\n{s['summary']}\n\n")
    pdf.output(PDF_FILE)
    print(f"📄 PDF report saved to {PDF_FILE}")


def main():
    print("🔹 Fetching disaster emails...")
    emails = fetch_disaster_emails()

    # Load existing CSV or create new
    if os.path.exists(CSV_FILE):
        df = pd.read_csv(CSV_FILE)
    else:
        df = pd.DataFrame(columns=["title", "summary"])

    new_entries = []

    # Convert to set for fast lookup (avoid duplicates)
    existing_titles = set(df["title"].str.strip().tolist())

    for email in emails:
        if email["subject"].strip() in existing_titles:
            print(f"⚠️ Skipping duplicate: {email['subject']}")
            continue

        summary = process_reports([email["snippet"]])[0]
        df = pd.concat([df, pd.DataFrame([{"title": email["subject"], "summary": summary}])], ignore_index=True)
        new_entries.append({"title": email["subject"], "summary": summary})
        print(f"🚨 Slack alert: {email['subject']}\n{summary}")

    # Save CSV only if new entries were added
    if new_entries:
        df.to_csv(CSV_FILE, index=False)
        print(f"✅ CSV updated: {CSV_FILE} ({len(new_entries)} new entries added)")
    else:
        print("ℹ️ No new entries added to CSV.")

    generate_pdf(df.to_dict(orient="records"))
    print("✅ Workflow completed successfully!")


if __name__ == "__main__":
    main()
