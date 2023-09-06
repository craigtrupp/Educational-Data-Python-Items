## Sort The dictionary by key value in Desc (Top to Bottom Type Order)

# >>> mratings
# [{'name': 'Baby Mama', 'rating': 64}, {'name': 'The Five-Year Engagement', 'rating': 63}, {'name': 'Bachelorette', 'rating': 56}, {'name': 'The Heat', 'rating': 65}, {'name': 'Date Night', 'rating': 67}, {'name': 'Sherlock Holmes: A Game Of Shadows', 'rating': 60}, {'name': 'Yahşi Batı', 'rating': 0}, {'name': 'Eyyvah Eyvah', 'rating': 0}, {'name': 'Pirates Of The Caribbean: On Stranger Tides', 'rating': 32}, {'name': 'Prince Of Persia: The Sands Of Time', 'rating': 36}]
# >>> mratings_srted = sorted(mratings, key=lambda i: i['rating'], reverse=True)
# >>> mratings_srted
# [{'name': 'Date Night', 'rating': 67}, {'name': 'The Heat', 'rating': 65}, {'name': 'Baby Mama', 'rating': 64}, {'name': 'The Five-Year Engagement', 'rating': 63}, {'name': 'Sherlock Holmes: A Game Of Shadows', 'rating': 60}, {'name': 'Bachelorette', 'rating': 56}, {'name': 'Prince Of Persia: The Sands Of Time', 'rating': 36}, {'name': 'Pirates Of The Caribbean: On Stranger Tides', 'rating': 32}, {'name': 'Yahşi Batı', 'rating': 0}, {'name': 'Eyyvah Eyvah', 'rating': 0}]


import requests_with_caching as rwc
import json

def get_movies_from_tastedive(strg):
    params = {'q': str(strg), 'type': 'movies', 'limit':5}
    resp = rwc.get('https://tastedive.com/api/similar', params = params)
    #print(resp.url)
    resp_j = resp.json()
    #print(resp_j['Similar']['Results'])
    return resp_j

def extract_movie_titles(mv_dict):
    return [x['Name'] for x in mv_dict['Similar']['Results']]

def get_related_titles(mv_list):
    comb_list = []
    for movie in mv_list:
        movies_dict = get_movies_from_tastedive(str(movie))
        movie_titles = extract_movie_titles(movies_dict)
        for mt in movie_titles:
            comb_list.append(mt)
    return list(set(comb_list))

def get_movie_data(mv_strg):
    base_url = 'http://www.omdbapi.com/'
    params = {'t': str(mv_strg), 'r': 'json'}
    resp = rwc.get(base_url, params)
    return resp.json()

def get_movie_rating(mv_dict):
    for rating_source in mv_dict['Ratings']:
        if rating_source['Source'] != 'Rotten Tomatoes':
            continue
        elif rating_source['Source'] == 'Rotten Tomatoes':
            value_str = rating_source['Value'][:-1] # slice to remove percent sign at end of string (which is the value type)
            value_int = int(value_str)
            return value_int
    return 0


def get_sorted_recommendations(mv_list):
    ## We want to return a list of the sorted recomendations by their rating
    sorted_dict_lst = []
    related_titles = get_related_titles(mv_list)
    # get the data/rating
    for movie in related_titles:
        movie_dct = get_movie_data(movie)
        rating = get_movie_rating(movie_dct)
        sorted_dict_lst.append({'name':movie, 'rating': rating})
    sorted_dict_lst = sorted(sorted_dict_lst, key=lambda i: (i['rating'], i['name']), reverse=True)
    print(sorted_dict_lst)
    return [x['name'] for x in sorted_dict_lst]

# Define a function get_sorted_recommendations. 
# It takes a list of movie titles as an input. 
# It returns a sorted list of related movie titles as output, up to five related movies for each input movie title. 
# The movies should be sorted in descending order by their Rotten Tomatoes rating, as returned by the get_movie_rating function. 
# Break ties in reverse alphabetic order, so that ‘Yahşi Batı’ comes before ‘Eyyvah Eyvah’.
# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages

print(get_sorted_recommendations(["Bridesmaids", "Sherlock Holmes"]))


## Output from above
# [{'name': 'Date Night', 'rating': 67}, {'name': 'The Heat', 'rating': 65}, {'name': 'Baby Mama', 'rating': 64}, {'name': 'The Five-Year Engagement', 'rating': 63}, {'name': 'Sherlock Holmes: A Game Of Shadows', 'rating': 60}, {'name': 'Bachelorette', 'rating': 56}, {'name': 'Prince Of Persia: The Sands Of Time', 'rating': 36}, {'name': 'Pirates Of The Caribbean: On Stranger Tides', 'rating': 32}, {'name': 'Yahşi Batı', 'rating': 0}, {'name': 'Eyyvah Eyvah', 'rating': 0}]
# ['Date Night', 'The Heat', 'Baby Mama', 'The Five-Year Engagement', 'Sherlock Holmes: A Game Of Shadows', 'Bachelorette', 'Prince Of Persia: The Sands Of Time', 'Pirates Of The Caribbean: On Stranger Tides', 'Yahşi Batı', 'Eyyvah Eyvah']

# [{'name': 'Date Night', 'rating': 67}, {'name': 'The Heat', 'rating': 65}, {'name': 'Baby Mama', 'rating': 64}, {'name': 'The Five-Year Engagement', 'rating': 63}, {'name': 'Sherlock Holmes: A Game Of Shadows', 'rating': 60}, {'name': 'Bachelorette', 'rating': 56}, {'name': 'Prince Of Persia: The Sands Of Time', 'rating': 36}, {'name': 'Pirates Of The Caribbean: On Stranger Tides', 'rating': 32}, {'name': 'Yahşi Batı', 'rating': 0}, {'name': 'Eyyvah Eyvah', 'rating': 0}]

