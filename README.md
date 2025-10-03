# Astrological Insight Generator 🌟

A personalized astrology insight generator built using Streamlit, LangChain, OpenAI GPT-4, and retrieval-augmented generation (RAG) using OpenAI Emebeddings. The application provides daily astrological insights for all zodiac signs and personalized insights based on user birth data. It also supports multiple languages including English, Hindi, and several Indian languages.

⸻

## Features

1. All Zodiac Daily Insights: <br>
	•	Generates daily insights for all 12 zodiac signs. <br>
	•	Uses insight_generator module for static daily insights. <br>
	•	Quick one-click generation for the entire zodiac.

2. Personalized Astrological Insights
	•	Users input Name, Birth Date, Birth Time, Birth Place, and Preferred Language. <br>
	•	Automatically calculates Zodiac Sign using zodiac.py. <br>
	•	Generates personalized daily insights using OpenAI GPT-4 through llm_chain.py. <br>
	•	Translates insights into multiple languages using translate.py: <br>
	•	English (en), Hindi (hi), Bengali (bn), Tamil (ta), Kannada (kn), Telugu (te) others can also be added as long as deep translate supports it<br>
	•	Includes mock RAG context via rag_retriever.py: <br>
	•	Uses a small corpus of descriptive zodiac traits. <br>
	•	Retrieves relevant context using OpenAI embeddings and FAISS vector store. <br>

3. RAG-Enhanced Insights <br>
	•	Mock corpus provides rich context for each zodiac. <br>
	•	Retrieval ensures the LLM leverages zodiac-specific traits. <br>
	•	Can be easily extended to a real corpus in the future. <br>

4. Translation Support <br>
	•	Uses Deep Translator (GoogleTranslator) for multi-language output. <br>
	•	Allows users to get insights in local languages while keeping the astrology context intact. <br>

5. Self-Testing <br>
	•	llm_chain.py and some other modules as well includes a built-in self-test to verify: <br>
	•	Zodiac calculation <br>
	•	RAG retrieval <br>
	•	OpenAI insight generation <br>
	•	Translation functionality <br>

6. Streamlit UI <br>
	•	Clean interface for selecting mode (All Zodiac / Personalized Insight). <br>
	•	Personalized insights display: <br>
	•	User Name <br>
	•	Zodiac Sign <br>
	•	Selected Language <br>
	•	Generated Insight <br>

⸻

## Installation
### Clone Repo
https -> `git clone https://github.com/SchrodingersDev/astro_insight.git` <br>
ssh  -> `git clone git@github.com:SchrodingersDev/astro_insight.git` <br>

then cd to repo

### Using Virtual Env(Optional)
`conda create -n astro_insight python=3.11 -y` <br>
I prefer miniconda you are free to use anything, the base should be 3.11.


### Install dependencies:

`pip install -r requirements.txt`

### Set up OpenAI API key in .env:

`OPENAI_API_KEY=your_openai_api_key`

### Run the fastAPI and Streamlit app

`python main.py` <br>
`streamlit run app_streamlit.py`


⸻

### Project Structure

```
astro_insight/
│
├── app_streamlit.py       # Streamlit front-end UI
├── llm_chain.py           # LLM integration with OpenAI and RAG context
├── rag_retriever.py       # Mock vector store and retrieval
├── translate.py           # Multi-language translation using Deep Translator
├── zodiac.py              # Zodiac calculation from birth date
├── insight_generator.py   # Static daily insights for all zodiac signs
├── requirements.txt       # Python dependencies
└── .env                   # OpenAI API key
```




### Future Scope
	1.	Real RAG Corpus 
	•	Replace mock corpus with real astrology articles, books, and horoscopes.
	•	Integrate more detailed and nuanced traits for each zodiac.
	2.	Dynamic Daily Updates
	•	Use live planetary positions and astrological data APIs to generate truly dynamic daily insights.
	3.	User History
	•	Save user insights in a database.
	•	Allow tracking of daily astrological trends.
	4.	Interactive Chat
	•	Extend the app to allow multi-turn conversations with the astrology LLM.
	5.	Improved Translation
	•	Fine-tune translations for astrological terminology to make them more culturally relevant.
	6.	Mobile-Friendly UI
	•	Optimize the Streamlit layout for mobile devices.
	•	Add downloadable insights or shareable PDF functionality.
	7.	Extended Languages
	•	Add support for more Indian languages and international languages.



### Credits
	•	OpenAI GPT-4 via LangChain for personalized insight generation. 
	•	Deep Translator for multi-language support.
	•	FAISS and OpenAI Embeddings for mock RAG retrieval.
	•	Streamlit for interactive web UI.
	•	Custom modules: zodiac.py, rag_retriever.py, translate.py, insight_generator.py.