import base64
import streamlit as st


# ---------- Background Function ----------
def set_bg_local(image_file):
    with open(image_file, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded}") !important;
            background-size: cover !important;
            background-position: center !important;
            background-repeat: no-repeat !important;
            background-attachment: fixed !important;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# ---------- Page Config ----------
st.set_page_config(page_title="ML Project Hub", layout="wide")

st.markdown("""
        <style>
        [data-testid="stSidebar"] {
            background-color: black; /* black - change to any color */
        }
        </style>
    """, unsafe_allow_html=True)

with st.sidebar:
        st.sidebar.image("rishu.jpg")
        st.sidebar.header("👥About US")
        
        st.sidebar.header("💬CONTACT US")
        st.sidebar.text("📞8809972414")
        st.sidebar.text("✉️rishabhverma190388099@gmail.com")

        st.sidebar.text("We are a group of ML engineers working on food sentiment")


# ---------- Import Project Functions ----------
from introduction1 import run_introduction1_classifier
from movie_recommendation_project import run_movie_recommendation
from food_sentiment_project import run_sentiment_analysis
from spam_detection_project import run_spam_classifier
from English_Hindi_project import run_language_classifier


# ---------- Tabs using radio ----------
tabs = {
    "Introduction" :"artificial-intelligence-technology.jpg",
    "🎬 Movie Recommendation": "movie recommendation.jpg",
    "🍔 Food Sentiment Analysis": "Sentiment-Analysis.jpg",
    "📩 Spam Detection" : "spam.jpg",
    "🌐 English-Hindi Classifier": "english Hindi.jpg"
}

selected_tab = st.radio("Choose a Project", list(tabs.keys()), horizontal=True)

# ---------- Dynamic Background ----------
set_bg_local(tabs[selected_tab])

# ---------- Dynamic Tab Content ----------
if selected_tab == "Introduction":
    run_introduction1_classifier()

elif selected_tab == "🎬 Movie Recommendation":
    run_movie_recommendation()

elif selected_tab == "🍔 Food Sentiment Analysis":
    run_sentiment_analysis()

elif selected_tab == "📩 Spam Detection":
    run_spam_classifier()

elif selected_tab == "🌐 English-Hindi Classifier":
    run_language_classifier()


