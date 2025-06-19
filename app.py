import streamlit as st
import pickle
import requests

# TMDb API key
API_KEY = 'your_api_key'

# Load data
movies_list = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))
movies = movies_list['title'].values


# Function to fetch poster from TMDb API
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=11648f74f07d0e8d1143fc6f4c8bfd45&language=en-US"#
    response = requests.get(url) #This line sends a request to the API using the URL above.and The response (data from the API) is stored in the variable response.
    data = response.json()#This converts the response into a dictionary (key-value pairs) so we can easily access specific information.
    poster_path = data.get('poster_path', '')#Get the poster path from the data
    full_path = f"https://image.tmdb.org/t/p/w500{poster_path}"#The result is a full URL that points to the movie's poster image.
    return full_path


# Recommendation function
def recommend(movie):
    movie_index = movies_list[movies_list['title'] == movie].index[0]
    distances = similarity[movie_index]
    similar_movies = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_posters = []
    for i in similar_movies:
        movie_id = movies_list.iloc[i[0]].movie_id  # Make sure 'movie_id' column exists
        recommended_movies.append(movies_list.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_posters


# Streamlit App UI
st.title('🎬 Movie Recommender System')

selected_movie_name = st.selectbox(
    'Select a movie to get recommendations:',
    movies
)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)
    st.subheader("Top 5 Recommended Movies:")
    cols = st.columns(5)#This line creates 5 equal columns side by side on the Streamlit page.
    for idx in range(5):
        with cols[idx]:#It tells Streamlit which column to place the content in.
            st.image(posters[idx])# shows the poster image of the recommended movie at position idx.
            st.caption(names[idx])#shows the name/title of the recommended movie just below the image.