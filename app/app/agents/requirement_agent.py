from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_requirements(text):

    prompt = f"""
    Analyze this requirement discussion.

    Identify:
    - key requirements
    - assumptions
    - dependencies
    - open questions

    Text:
    {text}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
