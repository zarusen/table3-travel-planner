import requests

def load_api_key(file_path):
    with open('api-key.txt', 'r') as file:
        return file.read().strip() #Read and get rid of whitespace

def get_restaurants(location):
    api_key = load_api_key('api-key.txt')
    #api_key ='AIzaSyA4witeIUyn2Zu9cnEodZw698Y7qcgUquk'
    query = f"restaurants in {location}"  # Modify query to focus on restaurants
    url = f"https://maps.googleapis.com/maps/api/place/textsearch/json?query={query}&key={api_key}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
        restaurants = response.json().get('results', [])[:5]  # Get the top 5 restaurants
        
        if not restaurants:
            print("No restaurants found.")
            return
        
        print("Top 5 Restaurants in "+location_query+":")
        for restaurant in restaurants:
            name = restaurant.get('name')
            address = restaurant.get('formatted_address')
            print("Location: "+f"{name}, {address}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    location_query = input("Enter a location (e.g., 'San Francisco'): ")
    get_restaurants(location_query)
