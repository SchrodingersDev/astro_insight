# main.py
from fastapi import FastAPI
from pydantic import BaseModel
from schemas import UserInput, InsightOutput
from insight_generator import generate_insight

app = FastAPI(title="Astrological Insight Generator")

@app.post("/predict", response_model=InsightOutput)
def predict(user: UserInput):
    """
    Accepts user birth details and returns zodiac + personalized insight.
    """
    result = generate_insight(user.birth_date, user.name, user.language)
    return result

# Run via: uvicorn main:app --reload
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)