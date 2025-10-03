from zodiac import get_zodiac
from translate import translate_text
import random

# Dummy zodiac templates
ZODIAC_MESSAGES = {
    "Aries": ["Take bold steps today and trust your instincts.", "Your energy will attract opportunities."],
    "Taurus": ["Stay grounded and patient today.", "Focus on practical decisions."],
    "Gemini": ["Your curiosity will lead to new insights.", "Communicate clearly to avoid misunderstandings."],
    "Cancer": ["Your intuition guides you well today.", "Spend time with loved ones."],
    "Leo": ["Your innate leadership and warmth will shine today.", "Embrace spontaneity and avoid overthinking."],
    "Virgo": ["Attention to detail will pay off.", "Balance work with self-care."],
    "Libra": ["Seek harmony in relationships today.", "Your creativity will be noticed."],
    "Scorpio": ["Channel your intensity into productive tasks.", "Avoid conflicts where possible."],
    "Sagittarius": ["Adventure awaits, stay open to new experiences.", "Your optimism inspires others."],
    "Capricorn": ["Focus on long-term goals.", "Persistence will bring rewards."],
    "Aquarius": ["Innovative ideas will come naturally today.", "Collaborate for maximum impact."],
    "Pisces": ["Trust your intuition and emotions.", "Creativity flows in quiet moments."]
}

def generate_insight(birth_date: str, name: str, language: str = "en") -> dict:
    """
    Generates a zodiac-based insight for the user, with optional translation.
    Returns dict compatible with InsightOutput.
    """
    zodiac = get_zodiac(birth_date)
    templates = ZODIAC_MESSAGES.get(zodiac, ["Today brings new opportunities."])
    message = random.choice(templates)
    insight_text = f"{name}, {message}"

    # Translate if required
    if language.lower() != "en":
        insight_text = translate_text(insight_text, language)

    return {
        "zodiac": zodiac,
        "insight": insight_text,
        "language": language
    }

# Example standalone test
if __name__ == "__main__":
    example = generate_insight("1995-08-20", "Ritika", "hi")
    print(example)