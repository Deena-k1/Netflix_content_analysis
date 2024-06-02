import requests
import csv
'''
We are using the Movies popular endpoint: https://developer.themoviedb.org/reference/movie-popular-list
as the endpoint can retrieve the data of one page at the time, we used this template to be able to iterate
the pages
'''
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

tv_url_template= 'https://api.themoviedb.org/3/tv/popular?language=en-US&page={page}'



for page in range(1, pages_to_retrieve + 1):
    page_url = tv_url_template.format(page=page)
    data = main_request(page_url, headers=headers)
    if data and 'results' in data:
        filtered_results = [show for show in data['results'] if show['original_language'] == 'en']
        all_results.extend(filtered_results)
        print(f"Data for page {page} retrieved.")
    else:
        print(f"Skipping page {page} due to missing or incorrect data.")

print(f"Total items retrieved: {len(all_results)}")

# Save the filtered results to a CSV file
csv_file2 = ('tvshows_API.csv')

with open(csv_file2, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Write the header
    writer.writerow(['original_name', 'first_air_date', 'popularity', 'vote_average', 'genre_ids'])
    # Write the data rows
    for show in all_results:
        writer.writerow([
            show['original_name'],
            show['first_air_date'],
            show['popularity'],
            show['vote_average'],
            show['genre_ids']
        ])

print(f"TV Shows Data saved to {csv_file2}")

def get_tv_genres():
    url = "https://api.themoviedb.org/3/genre/tv/list?language=en"
    response = requests.get(url, headers=headers)
    json_response = response.json() 
    
    # save to csv file 
    fields = ['id', 'name']
    filename = 'tvshowgenres_API.csv'
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(json_response['genres'])
      
    if response.status_code == 200:
        print(f"Success: Received status code {response.status_code} for URL: {url}")
        return response.json()
    else:
        print(f"Error: Received status code {response.status_code} for URL: {url}")
        return None