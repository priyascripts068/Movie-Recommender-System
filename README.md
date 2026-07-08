# 🎬 Movie Recommendation System

A Content-Based Movie Recommendation System built using **Python**, **Machine Learning**, and **Streamlit**. The application recommends the top 5 movies similar to a selected movie based on genres, keywords, cast, crew, and overview using cosine similarity.

---

## 📌 Features

- 🎥 Search and select any movie from the dataset
- 🤖 Content-Based Recommendation System
- ⭐ Displays IMDb Rating
- 🎭 Shows Movie Genres
- 👥 Displays Top 3 Cast Members
- 📝 Shows Movie Overview
- 📊 Similarity Score with Progress Bar
- 🎨 Interactive and Responsive Streamlit UI
- ⚡ Fast recommendations using precomputed similarity matrix

---

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- NLTK
- Streamlit
- Pickle

---

## 🧠 Machine Learning Workflow

1. Data Collection
2. Data Cleaning
3. Exploratory Data Analysis (EDA)
4. Feature Engineering
5. Text Preprocessing
   - Tokenization
   - Lowercasing
   - Stemming
6. CountVectorizer
7. Cosine Similarity
8. Recommendation Generation
9. Streamlit Deployment

---

## 📂 Project Structure

```
Movie-Recommender-System/
│
├── app.py
├── movie-recommender-system.ipynb
├── movies.pkl
├── similarity.pkl
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 📊 Dataset

Dataset used:

- TMDB 5000 Movies Dataset
- TMDB 5000 Credits Dataset

The datasets include:

- Movie Title
- Genres
- Cast
- Crew
- Keywords
- Overview
- Rating

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Movie-Recommender-System.git
```

Go to project folder

```bash
cd Movie-Recommender-System
```

Create virtual environment (Optional)

```bash
python -m venv .venv
```

Activate environment

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

## 📸 Application Preview

### Home Page

- Select a movie
- Click **Recommend Movies**

### Recommendation Card

Each recommendation displays:

- Movie Name
- IMDb Rating
- Genres
- Top Cast
- Movie Overview
- Similarity Score

---

## 🧩 Recommendation Algorithm

The recommendation system follows a **Content-Based Filtering** approach.

Movie features including:

- Genres
- Keywords
- Overview
- Cast
- Crew

are merged into a single text feature called **Tags**.

The tags are vectorized using **CountVectorizer**.

Cosine Similarity is then calculated between all movie vectors.

The application recommends the Top 5 most similar movies.

---

## 🚀 Future Improvements

- Movie Posters using TMDB API
- Search Autocomplete
- Genre-wise Recommendations
- Filter by Rating
- User Authentication
- Favorite Movies
- Hybrid Recommendation System
- TF-IDF Based Recommendation
- Deep Learning Recommendation Model

---

## 💡 Skills Demonstrated

- Machine Learning
- Natural Language Processing (NLP)
- Data Cleaning
- Feature Engineering
- Exploratory Data Analysis
- Content-Based Recommendation Systems
- Streamlit Web Development
- Model Serialization using Pickle
- Git & GitHub

---

## 👩‍💻 Author

**Priya Kumari**

Electrical Engineering Undergraduate

National Institute of Technology Kurukshetra

---
