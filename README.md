# MOVIE_RECOMMENDER_SYSTEM_TMDb_DATASET
Overview
This is a content-based movie recommendation system that suggests similar movies based on their features like genres, keywords, cast, crew, and overview. The system uses cosine similarity to find the most similar movies to the one you select.

Features
Recommends 5 most similar movies for any given movie

Uses movie details like plot, genres, actors, and directors

Processes text data to find meaningful connections between movies
How It Works
The system combines multiple data points about each movie:

Genres (e.g., Action, Comedy)

Keywords/tags (e.g., "space war", "alien planet")

Top 3 actors

Director

Movie overview/plot

It then processes this data to:

Clean and standardize text

Convert words to their root forms (stemming)

Create numerical representations of each movie

Dataset
The project uses two main datasets from TMDB (The Movie Database):

tmdb_5000_movies.csv - Contains movie details

tmdb_5000_credits.csv - Contains cast and crew information

Finally, it calculates similarity scores between movies to find the best matches
