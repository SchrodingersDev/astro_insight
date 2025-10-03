import os
from dotenv import load_dotenv
from langchain.schema import Document
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Load OpenAI API key
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY not found in .env")

# --- Expanded mock corpus ---
MOCK_CORPUS = {
    "Aries": """Aries are energetic and courageous. They take initiative and love new challenges. 
Aries people are natural leaders who thrive when pursuing ambitious goals. 
They can be impulsive but are also passionate and inspiring to others.""",
    "Taurus": """Taurus are practical and reliable. They value comfort, stability, and beauty. 
They enjoy sensory pleasures like good food and music. Taurus individuals are patient, determined, 
and loyal, making them strong friends and partners.""",
    "Gemini": """Geminis are curious, versatile, and lively. They adapt easily to new situations and enjoy learning. 
Their communication skills are exceptional, making them great conversationalists. 
Sometimes they can be indecisive but are always engaging and witty.""",
    "Cancer": """Cancers are nurturing and intuitive. They deeply care about loved ones and create safe, cozy spaces. 
They are empathetic and often guided by emotions, making them sensitive and compassionate individuals.""",
    "Leo": """Leos are confident and charismatic. They love being in the spotlight and are natural performers. 
Creative and generous, Leos inspire others with their optimism. They can be proud but have big hearts.""",
    "Virgo": """Virgos are analytical and meticulous. They value order and efficiency and often notice details others miss. 
They are reliable, helpful, and strive for perfection, sometimes being overly critical of themselves.""",
    "Libra": """Libras are diplomatic and charming. They seek balance, fairness, and harmony in all relationships. 
They have a strong aesthetic sense and enjoy art, culture, and social connections.""",
    "Scorpio": """Scorpios are intense and passionate. They are deeply perceptive and have strong emotional depth. 
Their determination and focus make them unstoppable when pursuing goals. They value loyalty and honesty.""",
    "Sagittarius": """Sagittarius are adventurous and optimistic. They love freedom, exploration, and learning about the world. 
Honest and philosophical, they inspire others with their enthusiasm and love for life.""",
    "Capricorn": """Capricorns are disciplined and ambitious. They value responsibility and hard work. 
Practical and strategic, they steadily climb toward long-term goals, earning respect and admiration.""",
    "Aquarius": """Aquarius are innovative and independent. They think outside the box and often challenge the status quo. 
Humanitarian and forward-thinking, they value progress and freedom of expression.""",
    "Pisces": """Pisces are compassionate and imaginative. They have strong intuition and empathy for others. 
Creative and dreamy, they often express themselves through art, music, or helping those in need."""
}

# --- Prepare documents ---
docs = [Document(page_content=text, metadata={"zodiac": sign}) for sign, text in MOCK_CORPUS.items()]

# Optional: split documents into smaller chunks if needed
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
split_docs = text_splitter.split_documents(docs)

# --- Initialize embeddings and FAISS vector store ---
embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
vector_store = FAISS.from_documents(split_docs, embeddings)

def retrieve_zodiac_context(zodiac_sign: str, top_k: int = 1) -> str:
    """
    Retrieves top_k most relevant documents for the zodiac sign from the vector store.
    Returns concatenated text.
    """
    results = vector_store.similarity_search(zodiac_sign, k=top_k)
    return " ".join([doc.page_content for doc in results])