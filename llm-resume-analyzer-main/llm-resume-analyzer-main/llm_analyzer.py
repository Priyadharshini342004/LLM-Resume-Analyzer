import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()  # .env file load karega

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_resume(text):
    prompt = f"""
    Analyze this resume and provide:
    1. Strengths
    2. Weaknesses
    3. Career suggestions

    Resume:
    {text}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
