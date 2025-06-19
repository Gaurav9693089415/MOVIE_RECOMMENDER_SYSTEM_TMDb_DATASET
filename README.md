

---

# Movie Recommendation System based on TMDb 5000 Dataset

This project implements a content-based movie recommender system using the **TMDb 5000 Movies Dataset**. Given a selected movie, the system recommends similar movies based on textual features such as genres, keywords, cast, and crew.

Built using Python, Streamlit, and scikit-learn, the system includes a web interface where users can select a movie and view its top 5 similar recommendations along with their posters.

---

## Project Structure

```
MOVIE_RECOMMENDER_SYSTEM_TMDb/
├── app.py                        # Streamlit application (for recommendation & UI)
├── movie_recommender_system.ipynb # Notebook for data processing & feature extraction
├── movies.pkl                    # Serialized movie dataframe (for faster loading)
├── similarity.pkl                # Similarity matrix (not included in repo, download separately)
├── tmdb_5000_credits.csv         # Original TMDb credits dataset
├── tmdb_5000_movies.csv          # Original TMDb movies dataset
├── requirements.txt              # Python dependencies
├── .gitignore                    # Files & folders ignored by Git
├── LICENSE                       # Project license
└── README.md                     # Project documentation (this file)
```

---

## Overview

* **Recommendation Type:** Content-Based Filtering
* **Dataset:** TMDb 5000 Movies Dataset (from Kaggle)
* **Similarity Metric:** Cosine Similarity (on combined textual features)
* **Frontend:** Streamlit App

---

## Features

✔️ Recommends **Top 5 movies** similar to the selected title
✔️ Displays **movie posters using TMDb API**
✔️ Includes a **clean and interactive web app (Streamlit)**
✔️ Fast load time due to **pre-computed `similarity.pkl` and `movies.pkl` files**

---

## Installation

1. **Clone the repository**

```bash
git clone https://github.com/Gaurav9693089415/MOVIE_RECOMMENDER_SYSTEM_TMDb.git
cd MOVIE_RECOMMENDER_SYSTEM_TMDb
```

2. **Create & activate a virtual environment (optional but recommended)**

```bash
python -m venv venv
venv\Scripts\activate     # For Windows
source venv/bin/activate  # For Mac/Linux
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

---

## similarity.pkl (Required File)

Due to GitHub's file size limit (100MB), the `similarity.pkl` file (176MB) is not included in this repository.

Please manually download it from the following link:

🔗 [Download similarity.pkl](https://drive.google.com/file/d/1m9h0mVh0QuCdk7TZxbuVvtJ2_cqdM9c8/view?usp=drive_link)

After downloading, place the `similarity.pkl` file in the root directory of this project (same folder as `app.py`).

---

## Usage

### 1. Run the Streamlit App

```bash
streamlit run app.py
```

✔️ The app will open in your browser:
**[http://localhost:8501](http://localhost:8501)**

### 2. Using the App

* Select a movie from the dropdown list.
* Click **"Recommend"**.
* View the **Top 5 recommended movies with posters**.

---
# linkedin link for  Demo:
[https://www.linkedin.com/feed/update/urn:li:activity:7320848835965005826/](https://www.linkedin.com/posts/gaurav-kumar-85a602324_machinelearning-movierecommendation-ai-activity-7320866352255098881-Wsu8?utm_source=share&utm_medium=member_desktop&rcm=ACoAAFH1mkYBXlDYEs-UqzA3ip8sGKZV5ynAbgw)

## Dataset

* **Source:** [Kaggle TMDb 5000 Movies Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)
* **Files Used:**

  * `tmdb_5000_movies.csv`
  * `tmdb_5000_credits.csv`

---

## Dependencies

All dependencies are listed in `requirements.txt`:

```
streamlit
scikit-learn
nltk
pandas
numpy
requests
```

---

## Development & Notes

* Preprocessing (feature extraction, vectorization) done in `movie_recommender_system.ipynb`.
* Cosine similarity computed and saved as `similarity.pkl` (must be downloaded separately).
* **TMDb API** used for fetching poster images dynamically.

---

## License

This project is released under the **MIT License**.

---


