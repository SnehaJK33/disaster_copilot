from flask import Flask, render_template
import pandas as pd
import os

app = Flask(__name__)
CSV_FILE = "data/disaster_logs.csv"

@app.route("/")
def dashboard():
    if os.path.exists(CSV_FILE):
        df = pd.read_csv(CSV_FILE)
        # Ensure columns exist
        for col in ["title", "summary"]:
            if col not in df.columns:
                df[col] = ""
        summaries = df.to_dict(orient="records")
    else:
        summaries = []

    return render_template("dashboard.html", summaries=summaries)

if __name__ == "__main__":
    app.run(debug=True)
