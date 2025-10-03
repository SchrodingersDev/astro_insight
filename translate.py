# translate.py
from deep_translator import GoogleTranslator

def translate_text(text: str, target_lang: str) -> str:
    """
    Translate text using Google Translate via deep-translator.
    Returns original text if target_lang is 'en'.
    """
    if target_lang.lower() == "en":
        return text
    try:
        translated = GoogleTranslator(source='auto', target=target_lang).translate(text)
        return translated
    except Exception as e:
        print(f"Translation failed: {e}")
        return text

# Standalone test
if __name__ == "__main__":
    sample_text = "Your innate leadership and warmth will shine today."
    print("English:", sample_text)
    print("Hindi :", translate_text(sample_text, "hi"))