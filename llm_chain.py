import os
from dotenv import load_dotenv
from datetime import date
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from zodiac import get_zodiac
from translate import translate_text
from rag_retriever import retrieve_zodiac_context  # RAG retriever

# Load OpenAI API key
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY not found in .env")

def generate_daily_insight_openai(birth_date: str, name: str, language: str = "en") -> dict:
    """
    Generates a personalized daily astrological insight using OpenAI via LangChain.
    Includes RAG context and translates the output if needed.
    """

    zodiac_sign = get_zodiac(birth_date)
    today = date.today().strftime("%B %d, %Y")

    # --- Retrieve RAG context ---
    zodiac_context = retrieve_zodiac_context(zodiac_sign, top_k=1)

    # --- Prompt template ---
    prompt_template = """
You are an expert astrologer. Use the following context to create a personalized daily astrological insight.

Date: {today}
User Name: {name}
Zodiac Sign: {zodiac_sign}
Context: {zodiac_context}

Write a concise, friendly, and positive horoscope-style insight for today. Make it engaging and clear.
    """

    chat_prompt = ChatPromptTemplate.from_template(prompt_template)
    formatted_prompt = chat_prompt.format_prompt(
        name=name,
        zodiac_sign=zodiac_sign,
        zodiac_context=zodiac_context,
        today=today
    ).to_messages()

    # --- Call OpenAI ---
    llm = ChatOpenAI(
        model_name="gpt-4",
        temperature=0.7,
        openai_api_key=OPENAI_API_KEY
    )
    response = llm.invoke(formatted_prompt)
    insight = response.content

    # --- Translate if needed ---
    translated_insight = translate_text(insight, language)

    return {"insight": translated_insight}


# --- Self-test ---
if __name__ == "__main__":
    print("=== LLM Chain Self-Test ===")
    sample_name = "Alice"
    sample_birth_date = "1995-08-20"
    sample_language = "en"

    zodiac_sign = get_zodiac(sample_birth_date)
    context = retrieve_zodiac_context(zodiac_sign)
    print(f"Sample Name: {sample_name}")
    print(f"Birth Date: {sample_birth_date}")
    print(f"Zodiac Sign: {zodiac_sign}")
    print(f"Retrieved Context: {context}\n")

    result = generate_daily_insight_openai(sample_birth_date, sample_name, sample_language)
    print("Generated Insight:")
    print(result["insight"])