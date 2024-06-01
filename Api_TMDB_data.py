
import requests
import csv
'''
We are using the Movies popular endpoint: https://developer.themoviedb.org/reference/movie-popular-list
as the endpoint can retrieve the data of one page at the time, we used this template to be able to iterate
the pages
'''
url_template = 'https://api.themoviedb.org/3/movie/popular?language=en-US&page={page}'

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0NTUxMGM5YjdkMzZmZjEwMDJmZjY3MDQ5MjEwZTJmYiIsInN1YiI6IjY2NTc2NTg0YTUwNjc0NzdiODIxNWNjMiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.jcqL8pWXeu4BhOSgE8TgtsqeNsFHHvIjpB4YMZMHvE8"

}
def main_request(url, headers=headers):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: Received status code {response.status_code} for URL: {url}")
        return None

# Number of pages to retrieve
pages_to_retrieve = 500

all_results = []

print(f"Retrieving pages 1 to {pages_to_retrieve}")

for page in range(1, pages_to_retrieve + 1):
    page_url = url_template.format(page=page)
    data = main_request(page_url, headers=headers)
    if data and 'results' in data:
        filtered_results = [movie for movie in data['results'] if movie['original_language'] == 'en']
        all_results.extend(filtered_results)
        print(f"Data for page {page} retrieved.")
    else:
        print(f"Skipping page {page} due to missing or incorrect data.")

print(f"Total items retrieved: {len(all_results)}")

# Save the filtered results to a CSV file
csv_file = ('movies_API.csv')

with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Write the header
    writer.writerow(['title', 'release_date', 'popularity', 'vote_average', 'genre_ids'])
    # Write the data rows
    for movie in all_results:
        writer.writerow([
            movie['title'],
            movie['release_date'],
            movie['popularity'],
            movie['vote_average'],
            movie['genre_ids']
        ])

print(f"Data saved to {csv_file}")

'''
same must be done for this endpoint to retrieve same info for the series
https://developer.themoviedb.org/reference/tv-series-popular-list
just double check the Keys of the response json file, is not the same
'''

'''
We need and endpoint with the watching time hopefully if that info is anywhere?
'''

'''
we need to print these ones as well to compare the genres ids with these lists
https://developer.themoviedb.org/reference/genre-movie-list
https://developer.themoviedb.org/reference/genre-tv-list
'''

