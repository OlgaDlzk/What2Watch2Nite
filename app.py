import csv
import os
import sys
import subprocess
import pandas as pd
#from flask import Flask, redirect
from flask import Flask, render_template, request, jsonify, redirect
import pickle

#Import Machine Learning file
from other_python_files import movies_machineLearning
from other_python_files import tv_machineLearning

app = Flask(__name__)

model = pickle.load('static/etl/pkl/tfidf.pkl', 'rb')
matrix = pickle.load('static/etl/pkl/tfidf_matrix.pkl', 'rb')
                    

# autocomplete suggestions for search bar - movies
def get_movie_suggestions():
    data = pd.read_csv('static/etl/csv/movies_data_cleaned.csv')
    return list(data['title'].str.capitalize())

# autocomplete suggestions for search bar - movies
def get_tv_suggestions():
    data = pd.read_csv('static/etl/csv/tv_shows_data_cleaned.csv')
    return list(data['original_name'].str.capitalize())


# Basic Pages Routes
@app.route('/', methods=['GET'])
def home_page():
    return render_template('index.html')

@app.route("/our_team", methods=['GET'])
def ourTeam():
    return render_template('our_team.html')






# Movie Routes
@app.route('/movies', methods=['POST','GET'])
def movies_page():
    return render_template('movies_2.html', suggestions=get_movie_suggestions())


@app.route('/process_data_movies', methods=['POST'])
def process_data():
    movie = request.form['movie']

    # Call machineLearning.py passing the movie name
    result = movies_machineLearning.process_movie(movie) 

    
    # Convert the result to JSON and return it
    return jsonify(result)








# pass test data from an input field in movies_2.html into a python file named insert_name_here.py using flask. have the python file insert_name_here.py pass the data into a new html file named movie recommendations.html
@app.route('/movie_recommendations', methods=['POST','GET'])
def movie_recommendations_page():
    if request.method == 'POST':
        movie_name = request.form['movie_name']
        print(movie_name)
        #return redirect(url_for('movie_recommendations_page', movie_name=movie_name))
        return render_template('movie_recommendations.html', movie_name=movie_name)
    else:
        return render_template('movie_2.html')







# TV Routes
@app.route('/tv_shows', methods=['GET'])
def tv_shows_page():
    return render_template('tv_shows_2.html', suggestions=get_tv_suggestions())


@app.route('/process_data_tv', methods=['POST'])
def process_data_tv():
    tv_show = request.form['movie']

    # Call machineLearning.py passing the movie name
    result = tv_machineLearning.process_tv(tv_show)

    # Convert the result to JSON and return it
    return jsonify(result)


@app.route('/tv_recommendations', methods=['POST','GET'])
def tv_recommendations_page():
    if request.method == 'POST':
        tv_show_name = request.form['tv_show_name']
        print(tv_show_name)
        #return redirect(url_for('movie_recommendations_page', movie_name=movie_name))
        return render_template('tv_recommendations.html', tv_show_name=tv_show_name)
    else:
        return render_template('tv_shows_2.html')




    
        




if __name__ == '__main__':
    app.run(debug=True)