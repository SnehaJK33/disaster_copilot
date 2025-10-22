import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables (make sure OPENAI_API_KEY is set in .env)
load_dotenv()

# Initialize new OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def summarize_text(text: str) -> str:
    """Summarize a disaster report using the new OpenAI API syntax"""
    try:
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "You are an assistant that writes one-sentence summaries of disaster reports."
                },
                {"role": "user", "content": text}
            ],
        )
        summary = completion.choices[0].message.content.strip()
        print(f"💬 Summarized: {summary}")
        return summary
    except Exception as e:
        print(f"⚠️ Error summarizing: {e}")
        return text
