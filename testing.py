import os
from xml.parsers.expat import model
from dotenv import load_dotenv
from google import genai


def main():
    load_dotenv()

    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("Missing GEMINI_API_KEY")

    # Create client (Gemini Developer API mode)
    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model="gemini-2.0-flash-lite",
        contents="this is a test python file"
    )

    print("Response text:", response.text)

if __name__ == "__main__":
    main()
