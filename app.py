import streamlit as st
import pickle
import pandas as pd

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬",
    layout="wide"
)

# ---------------- CUSTOM CSS ---------------- #

st.markdown("""
<style>

.main{
    background:#f8fafc;
}

.block-container{
    padding-top:2rem;
    padding-bottom:2rem;
}

h1{
    text-align:center;
    color:#1e3a8a;
    font-size:52px !important;
    margin-bottom:0px;
}

.subtitle{
    text-align:center;
    font-size:20px;
    color:#666;
    margin-bottom:35px;
}

.stButton>button{
    width:220px;
    height:48px;
    border-radius:10px;
    background:#2563eb;
    color:white;
    font-size:18px;
    font-weight:bold;
    border:none;
    transition:0.3s;
}

.stButton>button:hover{
    background:#60a5fa !important;   /* Light Blue */
    color:white !important;
    border:none !important;
}

.stButton>button:focus{
    background:#3b82f6 !important;
    color:white !important;
    border:none !important;
    box-shadow:none !important;
}

.stButton{
    display:flex;
    justify-content:center;
}

.movie-card{
    background:white;
    border-radius:15px;
    padding:20px;
    margin-bottom:18px;
    border:1px solid #e5e7eb;
    box-shadow:0px 4px 12px rgba(0,0,0,.08);
}

.movie-title{
    font-size:30px;
    font-weight:bold;
    color:#2563eb;
    margin-bottom:8px;
}

.heading{
    font-size:18px;
    font-weight:bold;
    color:#111827;
    margin-top:10px;
}

.badge{
    display:inline-block;
    background:#2563eb;
    color:white;
    padding:5px 12px;
    border-radius:20px;
    margin:4px;
    font-size:13px;
}

.overview{
    color:#444;
    font-size:15px;
    line-height:1.6;
}

.rating{
    color:#eab308;
    font-size:18px;
    font-weight:bold;
}

.similarity{
    color:#059669;
    font-size:17px;
    font-weight:bold;
}

</style>
""", unsafe_allow_html=True)

# ---------------- LOAD FILES ---------------- #

movies = pickle.load(open("movies.pkl","rb"))
similarity = pickle.load(open("similarity.pkl","rb"))

# ---------------- TITLE ---------------- #

st.markdown("<h1>🎬 Movie Recommendation System</h1>",unsafe_allow_html=True)

st.markdown(
"""
<div class='subtitle'>
Find movies similar to your favourite movie using Machine Learning
</div>
""",
unsafe_allow_html=True
)

movie_list = movies["title"].values

selected_movie = st.selectbox(
    "### 🔍 Search Movie",
    movie_list
)
def recommend(movie):

    movie_index = movies[movies['title'] == movie].index[0]

    distances = similarity[movie_index]

    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommendations = []

    for idx, score in movies_list:

        data = movies.iloc[idx]

        recommendations.append({
            "title": data["title"],
            "rating": data["vote_average"],
            "genres": data["genres"],
            "cast": data["cast"],
            "overview": data["overview"],
            "similarity": round(score*100,2)
        })

    return recommendations


# ---------------- BUTTON ---------------- #

if st.button("🎯 Recommend Movies"):

    recommendations = recommend(selected_movie)

    st.success(f"Top 5 Recommendations for **{selected_movie}**")

    for movie in recommendations:

        genres = ""

        if isinstance(movie["genres"], list):
            for g in movie["genres"]:
                genres += f"<span class='badge'>{g}</span>"

        else:
            genres = movie["genres"]


        if isinstance(movie["cast"], list):
            cast = ", ".join(movie["cast"][:3])
        else:
            cast = movie["cast"]


        overview = str(movie["overview"])

        if len(overview) > 180:
            overview = overview[:180] + "..."


        st.markdown(f"""

<div class="movie-card">

<div class="movie-title">
🎬 {movie['title']}
</div>

<div class="rating">
⭐ {movie['rating']}/10
</div>

<div class="heading">
Genres
</div>

{genres}

<div class="heading">
Top Cast
</div>

👥 {cast}

<div class="heading">
Overview
</div>

<div class="overview">
{overview}
</div>

<br>

<div class="similarity">
Similarity Score : {movie['similarity']}%
</div>

""", unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)