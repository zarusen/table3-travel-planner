import requests

def get_lat_lng(api_key, city_name):
    """
    Get latitude and longitude for a city using Google Geocoding API.
    
    Parameters:
        api_key (str): Your Google Geocoding API key.
        city_name (str): Name of the city.
    
    Returns:
        tuple: Latitude and longitude of the city.
    """
    geocode_url = "https://maps.googleapis.com/maps/api/geocode/json"
    
    params = {
        'address': city_name,
        'key': api_key
    }
    
    response = requests.get(geocode_url, params=params)
    
    if response.status_code == 200:
        result = response.json().get('results', [])
        if result:
            location = result[0]['geometry']['location']
            return location['lat'], location['lng']
        else:
            print("No results found for the city.")
            return None, None
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return None, None


def get_top_5_nearby_attractions(api_key, lat, lng, radius=1000, attraction_type='tourist_attraction'):
    """
    Fetch top 5 nearby attractions using Google Places API.
    
    Parameters:
        api_key (str): Your Google Places API key.
        lat (float): Latitude of the location.
        lng (float): Longitude of the location.
        radius (int): Search radius in meters (default: 1000).
        attraction_type (str): Type of place to search for (default: 'tourist_attraction').
    
    Returns:
        list: List of top 5 nearby attractions with their name and address.
    """
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    
    params = {
        'location': f'{lat},{lng}',
        'radius': radius,
        'type': attraction_type,
        'key': api_key
    }
    
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        results = response.json().get('results', [])
        top_5_attractions = []
        
        # Slice the results to only get the top 5
        for place in results[:3]:
            name = place.get('name')
            address = place.get('vicinity')
            top_5_attractions.append({
                'name': name,
                'address': address,
            })
        
        return top_5_attractions
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return []


def main():
    # Replace with your actual Google API key
    API_KEY = 'AIzaSyCnJAr6S4EV7hV13FvHcfgNMy3uNOwLSmA'
    
    # Ask the user to enter a city
    city_name = input("Enter the city name: ")
    
    # Get the latitude and longitude of the city
    lat, lng = get_lat_lng(API_KEY, city_name)
    
    if lat and lng:
        print(f"Fetching top 5 attractions near {city_name}...\n")
        
        # Get the top 5 nearby attractions
        top_5_attractions = get_top_5_nearby_attractions(API_KEY, lat, lng)
        
        if top_5_attractions:
            for idx, attraction in enumerate(top_5_attractions, start=1):
                print(f"{idx}. Name: {attraction['name']}, Address: {attraction['address']}")
        else:
            print("No attractions found.")
    else:
        print("Unable to find the city coordinates.")

if __name__ == "__main__":
    main()

