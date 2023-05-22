import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.pyplot as plt
import json
# to display images
from skimage import io

# to save the required files
import pickle

# the matrix
file_2 = open('static/etl/pkl/tfidf_matrix.pkl', 'rb')

matrix = pickle.load(file_2)

def process_movie(movie):
    # Perform machine learning operations
    # Process the movie name and generate the resuls
    movies_df = pd.read_csv('static/etl/csv/movie_dataset_final.csv')

    # Get the index of the movie that matches the title
    idx = movies_df.index[movies_df['title'].str.lower() == movie.lower()][0]
    # print('---------')
    # print(idx)
    # print({movies_df.loc[idx, "poster_path"]})
    # show given movie poster
    # try:
    #     a = io.imread(f'https://image.tmdb.org/t/p/w500/{movies_df.loc[idx, "poster_path"]}')
    #     plt.imshow(a)
    #     plt.axis('off')
    #     plt.title(movie)
    #     plt.show()
    # except:pass
    
    # print('Recommendations\n')

    # Get the pairwsie similarity scores of all movies with that movie
    sim_scores = list(enumerate(
        cosine_similarity(
            matrix,
            matrix[idx])))

    # Sort the movies based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the scores of the 10 most similar movies
    sim_scores = sim_scores[1:6]

    # Get the movie indices
    movie_indices = [i[0] for i in sim_scores]

    

    # Return the top 10 most similar movies
    result = movies_df.iloc[movie_indices]

      # show reco. movie posters
    # fig, ax = plt.subplots(2, 4, figsize=(15,15))
    # ax=ax.flatten()
    # for i, j in enumerate(result.poster_path):
    #     try:
    #         ax[i].axis('off')
    #         ax[i].set_title(result.iloc[i].title)
    #         a = io.imread(f'https://image.tmdb.org/t/p/w500/{j}')
    #         ax[i].imshow(a)
    #     except: pass
    # fig.tight_layout()
    # fig.show()

    result_json = result.to_json(orient='records')

    print('-----')
    data = json.loads(result_json)
    # print(len(data))
    # print(data[0]['poster_path'])
    movies_data = []
    for m in data:
        dic = {}
        dic['title'] = m['title']
        dic['overview'] = m['overview']
        dic['poster_path'] = 'https://image.tmdb.org/t/p/w500/'+m['poster_path']
        movies_data.append(dic)
    # print(movies_data)

    movies_dict2 = {}
    movies_dict2['num'] = len(movies_data)
    movies_dict2['movies'] = movies_data

    # for i in movies_data:
    #     movies_dict2.update(i)
        # print(m['title'])
        # print(m['overview'])
        # print(m['poster_path'])
        # print('----')
    # result_json = json.dumps(movies_data, indent = 4) 
    # print(result_json)             

    # result = {'movie': movie, 'recommendations': ['Recommendation 1', 'Recommendation 2', 'Recommendation 3']}
    return movies_dict2