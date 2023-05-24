<h1 align="center"> #What2Watch2Nite </h1> 
<h3 align="center"> Movies/TV Shows Recommendation System </h3> 

<p align="center">
  <img src="https://github-production-user-asset-6210df.s3.amazonaws.com/44728723/238146270-e9781802-ee01-4207-8713-f26bce4727a9.jpeg" alt="image"/>
</p>

## Table of Contents
1. [Motivation](#motivation)
2. [Data Description](#datadesc)
3. [Machine Learning Approach](#machinelearning)
4. [Web Application Overview](#webapp)
5. [Project Overview](#project)
6. [Movies](#movies)
7. [TV Shows](#shows)
8. [Our Team Page](#team)
9. [Future Consideratuion](#future)


<a name="motivation"></a>
# Motivation
With so many viewing and entertainment choices, it can be difficult and frustrating to select which movie or TV show to watch. In our research, we found that the vast majority of viewing recommendation engines were for movies, with very few focused on TV Shows. So we set out to build a recommendation system for movies AND television shows to make it easier for our users to choose **"What2Watch2Nite"**.

## Tools:
Flask
Pickle 
Pandas
Matplotlib
HTML/CSS/JavaScript
Bootstrap
Font-Awesome
Tableau


<a name="datadesc"></a>
# Data Description
- We used 2 datasets housed on Kaggle for this project. A movie dataset containing over 700,000 records scraped daily from The Movie Dabtbase (TMDB) which contain the following information:  title, cast, crew, plot keywords, genres, budget, revenue, posters, release dates, languages, production companies, countries, TMDB vote count, vote average and reviews.
- The second dataset has over 150,000 records for TV Series scraped from TMDB and updated weekly.  This dataset contains the following metadata: title, first/last air date, in production (T/F), number of episodes/seasons, country, language, series overview, popularity, TMDB vote count and vote average. 
- After cleaning and pre-processing the data, the final datasets contained: 23,000 Movie records and 8,000 TV Show records.
- The original data can be found here:  [movie data](https://www.kaggle.com/datasets/akshaypawar7/millions-of-movies) and [tv show data](https://www.kaggle.com/datasets/bourdier/all-tv-series-details-dataset).

- Data Distribution:  both final datasets have normal distributions
<p align="center"> <img width="612" alt="movie histogram" src="https://github.com/OlgaDlzk/What2Watch2Nite/assets/44728723/c4849070-f086-428e-ac97-370bc73667f1">

<p align="center"> <img width="612" alt="tv show histogram" src="https://github.com/OlgaDlzk/What2Watch2Nite/assets/44728723/e7aea493-b553-4321-a28b-7dfe7d99913f">

<a name="machinelearning"></a>
# Machine Learning Approach

- We deployed Machine Learning using Scikit-learn's K-Nearest Neighbors algorithm with cosine similarity as the metric parameter.
- We tested two approaches to the NLP when transforming the text features into vectors: CountVectorizer and TF-IDF Vectorizer. We found that TF-IDF performed better than the Count Vectorizer as it considers the importance of a word along with its frequency while Count Vectorizer relys soley on frequency count. 
- We also tested Pearson Correlation Coeffecient as a measure of distance for KNN similarity scores and found that this approached produced extremely similar results to the cosine similarity approach.

<a name="webapp"></a>
# Web Application Overview

- We deployed Flask as the web server to host the page routes and pass the data through the gateway to their designated machine learning files and back on to their respective pages to be displayed.
- We have two file for machine learning to increase speed and effectiveness of the web application since the algorithms will either only have to contend with the data in the tv show dataset or the movie dataset instead of navigating through all the data.
- The web application navigation contains links to 5 webpages (Project Overview, Movies, TV Shows, Our tableau data, and Our Team) and a link to this GitHub repository. 
- To see the live version of the website application, download the source code and launch the Flask app.py file.  The web app is also hosted on render.com through the following link (UPDATE LINK):  [What2Watch2Nite](https://grape-choice.onrender.com/)

<a name="project"></a>
# Project Overview

<p align="center"> <img width="614" alt="index" src="https://github.com/OlgaDlzk/What2Watch2Nite/assets/44728723/63feed96-2b86-4209-b4a0-5ddbfdbc4832">
__________________________________________________________________________________
 
<a name="movies"></a>
## Movies

The item-based movie machine learning model is a recommendation system that utilizes the TF-IDF vectorizer and stemming techniques. It aims to provide personalized movie recommendations to users based on their preferences and similarities between movies. For this particular model we used the following parameters: genres, overview, keywords, cast and original language. TF-IDF (Term Frequency-Inverse Document Frequency) is a numerical representation technique that assigns weights to words in a document based on their frequency and importance. Additionally, stemming is a text normalization technique that reduces words to their root or base form. By applying stemming, variations of words with the same meaning are grouped together, improving the model's ability to identify similarities between movies.

In the item-based approach, the model calculates the similarity between movies based on their TF-IDF vector representations. This similarity is used to generate recommendations. When a user expresses their preferences or watches certain movies, the model identifies similar movies based on their TF-IDF vectors and suggests them to the user. By combining TF-IDF vectorization and stemming, the model can effectively capture the unique features of each movie and provide personalized recommendations based on the user's interests and the similarities between movies. This approach helps enhance the accuracy and relevance of movie recommendations, improving the overall user experience.

<p align="center"> <img width="612" alt="movies engine screenshot" src="https://raw.githubusercontent.com/OlgaDlzk/What2Watch2Nite/main/static/design/img/movies_eng_screenshot.jpg">

__________________________________________________________________________________

<a name="shows"></a> 
## TV Shows

- text
- text
INSERT SCREENSHOT

__________________________________________________________________________________

<a name="team"></a> 
# Our Team Page

Our team page contains links to each member's GitHub repository, LinkedIn profile and Twitter account that displays when the user hovers over an avatar.
<p align="center"> <img width="614" alt="Our Team" src="https://github.com/OlgaDlzk/What2Watch2Nite/assets/44728723/806815aa-97ef-49a3-b188-3265ff2dee5d">

<a name="future"></a> 
# Future Considerations
In the future, we could expand upon this web application by:
- Add video data like trailers to be presented along with the selected suggestions.
- Include local spots or media streaming sites where the suggestions could be found.
