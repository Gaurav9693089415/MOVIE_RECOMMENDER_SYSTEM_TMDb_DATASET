# MOVIE_RECOMMENDER_SYSTEM_TMDb_DATASET

# Overview
A content-based movie recommendation system with a beautiful Streamlit web interface that suggests 5 similar movies and displays their posters. The system uses:

Movie data (genres, keywords, cast, crew)

TMDb API for fetching movie posters

Cosine similarity for recommendations

# Features 
Interactive UI: Clean web interface built with Streamlit

Visual Recommendations: Shows movie posters alongside titles

Fast Performance: Pre-computed similarity scores

API Integration: Fetches latest movie posters from TMDb
Processes text data to find meaningful connections between movies
# How It Works 
Select a movie from the dropdown

Click "Recommend" button

Get 5 similar movies with posters
# Technical Details ⚙️
* Data Processing:

Combines movie details (genres, keywords, cast, director)

Text cleaning and stemming

Cosine similarity calculation
* Web Interface:

Dropdown movie selector

5-column layout for recommendations

TMDb API integration for posters

# Credits 
Movie data from The Movie Database (TMDb)

Built with Python's data science stack

Streamlit for the web interface
# License 
This project is open source and available under the MIT License.


