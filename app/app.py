import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movies_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=######&language=en-US'.format(movies_id))
    data = response.json()
    print(data)
    return ("https://image.tmdb.org/t/p/w500/" + data['poster_path'])

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse = True, key = lambda x:x[1])[1:6]
    
    your_movies = []
    poster_movies = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        your_movies.append((movies.iloc[i[0]].title))
        poster_movies.append(fetch_poster(movie_id))
    
    return your_movies,poster_movies

movies_list = pickle.load(open('movies1.pkl','rb'))
similarity = pickle.load(open('similarity1.pkl','rb'))
movies = pd.DataFrame(movies_list)

st.title('Know the Movie You Want')

option = st.selectbox(
'Select a movie', movies['title'].values
)

if st.button('Recommend'):
    name,posters = recommend(option)
    print(name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(name[0])
        st.image(posters[0])
    
    with col2:
        st.text(name[1])
        st.image(posters[1])
    
    with col3:
        st.text(name[2])
        st.image(posters[2])
    
    with col4:
        st.text(name[3])
        st.image(posters[3])
    
    with col5:
        st.text(name[4])
        st.image(posters[4])
    


    
