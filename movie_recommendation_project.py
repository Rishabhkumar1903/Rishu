import streamlit as st
import joblib
import requests
import base64
from PIL import Image
from io import BytesIO
import concurrent.futures

# -------------------- Load Data --------------------
df = joblib.load("movie_df.pkl")
model = joblib.load("model.pkl")
vectors = joblib.load("movie_vector.pkl")
def run_movie_recommendation():
    st.markdown("""
        <div style=text-align:center;">
            <h1 style="color:burlywood;">MOVIE RECOMMENDATION</h1>
        </div>
    """, unsafe_allow_html=True)

    # -------------------- Custom CSS for Staggered Fade-in --------------------
    st.markdown("""
        <style>
        @keyframes fadeIn {
            from {opacity: 0; transform: scale(0.95);}
            to {opacity: 1; transform: scale(1);}
        }
        .fade-in {
            animation: fadeIn 1s ease-in-out forwards;
            opacity: 0;
        }
        /* Delay for each poster */
        .fade-in:nth-child(1) { animation-delay: 0.1s; }
        .fade-in:nth-child(2) { animation-delay: 0.3s; }
        .fade-in:nth-child(3) { animation-delay: 0.5s; }
        .fade-in:nth-child(4) { animation-delay: 0.7s; }
        .fade-in:nth-child(5) { animation-delay: 0.9s; }
        </style>
    """, unsafe_allow_html=True)

    # -------------------- Poster & Rating Fetch Function --------------------
    def get_poster_and_rating(movie_id):
        try:
            data = requests.get(f"http://www.omdbapi.com/?i={movie_id}&apikey=a8f8711e", timeout=5).json()
            poster_url = data.get('Poster', "")
            rating = data.get('imdbRating', "N/A")

            if not poster_url or poster_url in ["N/A", "0", "", None]:
                return None

            img_data = requests.get(poster_url, timeout=5).content
            Image.open(BytesIO(img_data))  # Validate image

            return poster_url, rating
        except:
            return None

    # -------------------- Parallel Poster & Rating Fetch --------------------
    def fetch_posters_and_ratings_parallel(movie_ids):
        with concurrent.futures.ThreadPoolExecutor() as executor:
            return list(executor.map(get_poster_and_rating, movie_ids))

    # -------------------- Movie Selection --------------------
    movie = st.selectbox("What are you looking for today:", sorted(df["name"]))

    # -------------------- Recommend Button --------------------
    if st.button("Recommend",key="movie_recommend"):
        if movie in df["name"].values:
            movie_index = df[df["name"] == movie].index[0]
            movie_vector = vectors[movie_index]

            distances, indexes = model.kneighbors([movie_vector], n_neighbors=25)
            candidate_ids = [df.loc[i, "movie_id"] for i in indexes[0][1:]]

            # Fetch posters & ratings
            poster_data = fetch_posters_and_ratings_parallel(candidate_ids)

            valid_movies = []
            for idx, result in enumerate(poster_data):
                if result:
                    poster, rating = result
                    valid_movies.append((df.loc[indexes[0][idx+1], "name"], poster, rating))
                if len(valid_movies) == 5:
                    break

            # Display
            cols = st.columns(len(valid_movies))
            for idx, (name, poster, rating) in enumerate(valid_movies):
                with cols[idx]:
                    st.markdown(
                        f'<div class="fade-in"><img src="{poster}" width="100%"></div>',
                        unsafe_allow_html=True
                    )
                    st.markdown(
                        f"""
                        <div style='text-align:center; color:white; font-size:20px; font-weight:bold; margin-top:5px;
                                    text-shadow: 2px 2px 4px rgba(0,0,0,0.7);'>
                            {name}
                        </div>
                        <div style='text-align:center; color:gold; font-size:18px; font-weight:bold;'>
                            ⭐ {rating}
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

            if not valid_movies:
                st.warning("No valid posters found for recommendations.")
        else:
            st.error("Movie not found, please select a different movie")
