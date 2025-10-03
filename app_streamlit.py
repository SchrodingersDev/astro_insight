import streamlit as st
from insight_generator import generate_insight
import datetime

st.set_page_config(page_title="Astrological Insight Chat", page_icon="✨")
st.title("Astrological Insight Generator 🌟")

mode = st.radio("Select Mode:", ["Daily Insights for All Zodiac Signs", "Personalized Insight Chat"])

# --- Mode 1: All Zodiac Daily Insights ---
if mode == "Daily Insights for All Zodiac Signs":
    if st.button("Generate Today's Insights for All Signs"):
        all_zodiacs = ["Aries","Taurus","Gemini","Cancer","Leo","Virgo","Libra","Scorpio","Sagittarius","Capricorn","Aquarius","Pisces"]
        for sign in all_zodiacs:
            insight = generate_insight("2000-01-01", sign)
            st.subheader(sign)
            st.write(insight["insight"])

# --- Mode 2: Personalized Insight Chat ---
elif mode == "Personalized Insight Chat":

    # Initialize session state
    if "user_info_submitted" not in st.session_state:
        st.session_state.user_info_submitted = False
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # --- Step 1: Collect user info ---
    if not st.session_state.user_info_submitted:
        with st.form(key="user_info_form"):
            st.subheader("Enter your personal details first")
            name = st.text_input("Name")
            birth_date = st.date_input(
                "Birth Date",
                value=datetime.date(1995, 8, 20),
                min_value=datetime.date(1900, 1, 1),
                max_value=datetime.date.today()
            )
            birth_time = st.time_input("Birth Time")
            birth_place = st.text_input("Birth Place")
            language = st.selectbox("Language", ["en", "hi"])
            submit_info = st.form_submit_button("Save Info and Start Chat")

        if submit_info:
            st.session_state.user_info = {
                "name": name,
                "birth_date": birth_date.strftime("%Y-%m-%d"),
                "birth_time": birth_time.strftime("%H:%M"),
                "birth_place": birth_place,
                "language": language
            }
            st.session_state.user_info_submitted = True

    # --- Step 2: Chat interface ---
    if st.session_state.user_info_submitted:
        st.subheader(f"Hello, {st.session_state.user_info['name']}! Start chatting:")

        # Container for chat history to allow scrolling
        chat_container = st.container()

        # Chat input
        user_input = st.text_input("Type your message here...", key="chat_input")

        if st.button("Send") and user_input.strip() != "":
            response = generate_insight(
                st.session_state.user_info['birth_date'],
                st.session_state.user_info['name'],
                st.session_state.user_info['language']
            )
            # Append to messages
            st.session_state.messages.append({"user": user_input, "bot": response["insight"]})
            # Clear input box
            st.experimental_rerun()

        # Display messages inside container
        with chat_container:
            for chat in st.session_state.messages:
                st.markdown(f"**You:** {chat['user']}")
                st.markdown(f"**AstroBot:** {chat['bot']}")