from pydantic import BaseModel, Field

class UserInput(BaseModel):
    name: str = Field(..., example="Ritika")
    birth_date: str = Field(..., example="1995-08-20")  # YYYY-MM-DD
    birth_time: str = Field(..., example="14:30")       # HH:MM (24hr)
    birth_place: str = Field(..., example="Jaipur, India")
    language: str = Field(default="en", example="en")

class InsightOutput(BaseModel):
    zodiac: str
    insight: str
    language: str