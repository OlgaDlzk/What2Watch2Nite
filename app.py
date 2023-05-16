import csv
import os
import sys
import subprocess
import pandas as pd
#from flask import Flask, redirect
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

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
@app.route('/movies', methods=['GET'])
def movies_page():
    return render_template('movies_2.html', suggestions=get_movie_suggestions())



# TV Routes
@app.route('/tv_shows', methods=['GET'])
def tv_shows_page():
    return render_template('tv_shows_2.html', suggestions=get_tv_suggestions())



if __name__ == '__main__':
    app.run(debug=True)