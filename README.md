# MOVIE RECOMMENDATION SYSTEM
<br />


  <p align="center">
   
<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#dataset">Dataset</a></li>
    </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project



This is a simple movie recommendation system. I have used Content Based Recommendation technique for this particular project. At an abstract level the system takes an input from the user i.e the user has to give the movie of their choice and the system in turn will recommend them with the top 5 movies that are similar of the user's input. 
 
  All you have to do is search for the movie in the text-bar and hit the recommend button. 
  



### Built With


* Python 3.9
* Scikit Learn 0.24.2
* Streamlit==0.87.0
* Streamlit==0.87.0
* Pandas==1.3.2
  



<!-- GETTING STARTED -->
## Getting Started

Prior to running it into your local machine following steps need to be done
  
  


1. Get a free API Key at [ https://www.themoviedb.org/ ](Refer to the section of API KEY)
2. Clone the repo
   ```sh
   git clone https://github.com/naix5526/movie_recommender.git
   ```
3. Install all the libraries mentioned in the requirements.txt file with the command 
   ```sh
   pip install -r requirements.txt
   ```
4. Enter your API in `app.py` file located inside app folder. Replace ##### located in line 7
5. Open your terminal/command prompt from the app directory and run the app.py file by using the command 
   ```sh
   streamlit run app.py
   ```
## Dataset

Dataset used in this project has been taken from kaggle
  
https://www.kaggle.com/tmdb/tmdb-movie-metadata


