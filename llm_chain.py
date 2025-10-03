import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from zodiac import get_zodiac
from translate import translate_text  # import your translator

# Load environment variables from .env
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY not found in .env")

def generate_daily_insight_openai(birth_date: str, name: str, language: str = "en") -> dict:
    """
    Generates personalized astrological insight using OpenAI via LangChain.
    Translates the insight to the target language if needed.
    """

    zodiac_sign = get_zodiac(birth_date)

    prompt_template = """
You are an expert astrologer. Generate a concise and friendly personalized daily astrological insight
for {name}, whose zodiac sign is {zodiac_sign}. Keep it positive, clear, and engaging.
    """

    chat_prompt = ChatPromptTemplate.from_template(prompt_template)
    formatted_prompt = chat_prompt.format_prompt(
        name=name,
        zodiac_sign=zodiac_sign
    ).to_messages()

    # Initialize ChatOpenAI from langchain-openai
    llm = ChatOpenAI(
        model_name="gpt-4",
        temperature=0.7,
        openai_api_key=OPENAI_API_KEY
    )

    # Generate insight
    response = llm.invoke(formatted_prompt)
    insight = response.content

    # Translate if target language is not English
    translated_insight = translate_text(insight, language)

    return {"insight": translated_insight}