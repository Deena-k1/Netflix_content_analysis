import requests
import csv

BASE_URL = "https://api.themoviedb.org/3"
BEARER_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0NTUxMGM5YjdkMzZmZjEwMDJmZjY3MDQ5MjEwZTJmYiIsInN1YiI6IjY2NTc2NTg0YTUwNjc0NzdiODIxNWNjMiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.jcqL8pWXeu4BhOSgE8TgtsqeNsFHHvIjpB4YMZMHvE8"

headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {BEARER_TOKEN}"
}

def fetch_all_movies(max_pages=500):
    page = 1
    all_movies = []

    while page <= max_pages:
        url = f"{BASE_URL}/movie/popular?language=en-US&page={page}"
        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            print(f"Error fetching page {page}: {response.status_code} - {response.reason}")
            break

        data = response.json()
        all_movies.extend(data['results'])

        print(f"Fetched page {page} with {len(data['results'])} movies.")
        
        if page >= data['total_pages']:
            break

        page += 1

    return all_movies

def fetch_genres():
    url = f"{BASE_URL}/genre/movie/list?language=en-US"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        print("Fetched genres successfully.")
        return response.json()['genres']
    else:
        print(f"Error fetching genres: {response.status_code} - {response.reason}")
        return []

def get_genre_dict():
    genres = fetch_genres()
    genre_dict = {genre['id']: genre['name'] for genre in genres}
    return genre_dict

def enrich_movies_with_genres(movies, genre_dict):
    for movie in movies:
        movie['genre_names'] = [genre_dict.get(genre_id, "Unknown") for genre_id in movie['genre_ids']]
    return movies

def save_to_csv(movies, filename='movies.csv'):
    fieldnames = ['title', 'genre_names']
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for movie in movies:
            writer.writerow({
                'title': movie['title'],
                'genre_names': ', '.join(movie['genre_names'])
            })

if __name__ == '__main__':
    print("Fetching all movies...")
    all_movies = fetch_all_movies(max_pages=500)
    print(f"Fetched {len(all_movies)} movies in total.")

    print("Fetching genres...")
    genre_dict = get_genre_dict()
    print(f"Fetched {len(genre_dict)} genres.")

    print("Enriching movies with genres...")
    enriched_movies = enrich_movies_with_genres(all_movies, genre_dict)

    print("Saving movies to CSV...")
    save_to_csv(enriched_movies)
    print("Data saved to movies.csv")
