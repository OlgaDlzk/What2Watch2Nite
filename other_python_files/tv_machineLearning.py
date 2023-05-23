import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import json

# to save the required files
import pickle

# open final vector matrix
file_3 = open('static/etl/pkl/combined_vectors_final.pkl', 'rb')

matrix = pickle.load(file_3)

def process_tv_shows(shows):
    # Perform machine learning operations
    # Process the tv show name and generate the results
    shows = pd.read_csv('static/etl/csv/tv_shows_final.csv')

    # Get the index of the tv show that matches the title/name
    idx = shows.index[shows['name'].str.lower() == show.lower()][0]

    # Get the pairwsie similarity scores of all tv shows with the input tv show
    sim_scores = list(enumerate(
        cosine_similarity(
            matrix,
            matrix[idx])))

    # Sort the tv shows based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the scores of the 6 most similar tv shows
    sim_scores = sim_scores[1:7]

    # Get the tv show indices
    show_indices = [i[0] for i in sim_scores]    

    # Return the top 6 most similar tv shows
    result = shows.iloc[show_indices]

    result_json = result.to_json(orient='records')

    print('-----')
    data = json.loads(result_json)
    # print(len(data))
    # print(data[0]['poster_path'])
    shows_data = []
    for m in data:
        dic = {}
        dic['name'] = m['name']
        dic['overview'] = m['overview']
        dic['poster_path'] = 'https://www.themoviedb.org/t/p/w600_and_h900_bestv2/'+m['poster_path']
        shows_data.append(dic)
    # print(shows_data)

    shows_dict2 = {}
    shows_dict2['num'] = len(shows_data)
    shows_dict2['shows'] = shows_data           

    return shows_dict2
