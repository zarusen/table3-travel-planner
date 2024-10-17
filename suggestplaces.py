import requests

def get_top_5_nearby_attractions(api_key, location, radius=1000, attraction_type='tourist_attraction'):
    """
    Fetch top 5 nearby attractions using Google Places API.
    
    Parameters:
        api_key (str): Your Google Places API key.
        location (str): Latitude and longitude in the format 'lat,lng' (e.g., '40.712776,-74.005974').
        radius (int): Search radius in meters (default: 1000).
        attraction_type (str): Type of place to search for (default: 'tourist_attraction').
    
    Returns:
        list: List of top 5 nearby attractions with their name and address.
    """
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    
    params = {
        'location': location,
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
        return f"Error: {response.status_code}, {response.text}"

# Example usage:
if __name__ == "__main__":
    
    API_KEY = 'AIzaSyCnJAr6S4EV7hV13FvHcfgNMy3uNOwLSmA'
    
    # Latitude and longitude (e.g., New York City)
    location = "28.538336,-81.379234"
    
    # Call the function and print the top 5 results
    top_5_attractions = get_top_5_nearby_attractions(API_KEY, location)
    
    print(f"Here are the top 3 attractions that are close to your location")
    
    for idx, attraction in enumerate(top_5_attractions, start=1):
        print(f"{idx}. Name: {attraction['name']}, Address: {attraction['address']}")

