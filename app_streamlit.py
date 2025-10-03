import streamlit as st
import datetime
from llm_chain import generate_daily_insight_openai
from insight_generator import generate_insight  # still used for all-zodiac daily insights

st.set_page_config(page_title="Astrological Insight Chat", page_icon="✨")
st.title("Astrological Insight Generator 🌟")

mode = st.radio("Select Mode:", ["Daily Insights for All Zodiac Signs", "Personalized Insight"])

# --- Mode 1: All Zodiac Daily Insights ---
if mode == "Daily Insights for All Zodiac Signs":
    if st.button("Generate Today's Insights for All Signs"):
        all_zodiacs = ["Aries","Taurus","Gemini","Cancer","Leo","Virgo",
                       "Libra","Scorpio","Sagittarius","Capricorn","Aquarius","Pisces"]
        for sign in all_zodiacs:
            insight = generate_insight("2000-01-01", sign)
            st.subheader(sign)
            st.write(insight["insight"])

# --- Mode 2: Personalized Insight ---
elif mode == "Personalized Insight":

    # --- Collect user info ---
    with st.form(key="user_info_form"):
        st.subheader("Enter your personal details to get your insight")
        name = st.text_input("Name")
        birth_date = st.date_input(
            "Birth Date",
            value=datetime.date(1995, 8, 20),
            min_value=datetime.date(1900, 1, 1),
            max_value=datetime.date.today()
        )
        birth_time = st.time_input("Birth Time")
        birth_place = st.text_input("Birth Place")
        language = st.selectbox("Language", ["en", "hi", "bn", "ta", "kn", "te"])  # example languages (We can add more)
        submit_info = st.form_submit_button("Generate Insight")

    if submit_info:
        response = generate_daily_insight_openai(
            birth_date.strftime("%Y-%m-%d"),
            name,
            language
        )

        # Display zodiac sign and language
        from zodiac import get_zodiac
        zodiac_sign = get_zodiac(birth_date.strftime("%Y-%m-%d"))

        st.subheader(f"Hello, {name}!")
        st.markdown(f"**Zodiac Sign:** {zodiac_sign}")
        st.markdown(f"**Language:** {language.upper()}")
        st.markdown("**Your Personalized Astrological Insight:**")
        st.write(response["insight"])