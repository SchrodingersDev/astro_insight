# translate.py
from googletrans import Translator

# Initialize Google Translator
translator = Translator()

def translate_text(text: str, target_lang: str) -> str:
    """
    Translate text to target language using Google Translate.
    If target_lang is 'en', returns original text.
    """
    if target_lang.lower() == 'en':
        return text
    try:
        translated = translator.translate(text, dest=target_lang)
        return translated.text
    except Exception as e:
        print(f"Translation failed: {e}")
        return text

# Standalone test
if __name__ == "__main__":
    sample_text = "Your innate leadership and warmth will shine today."
    print("English:", sample_text)
    print("Hindi :", translate_text(sample_text, "hi"))