---
type: challenge
event: glacier
name: best_food
category: osint
note: "[[osint]] distance on map"
solved: ✅
---

```python
import requests
import numpy as np
from scipy.optimize import minimize

# Configuration
CITY_NAME = "Graz"  # Change this if you want to test other cities (e.g., "Vienna")
OVERPASS_URL = "http://overpass-api.de/api/interpreter"

# The distances provided in the Rust code (Assumed to be Kilometers)
DISTANCES = {
    "bar": 0.6412652119499,
    "atm": 0.2822972577454,
    "taxi": 0.9572772921063
}

def get_nodes(amenity, city):
    """Fetches lat/lon for all nodes of a specific amenity in the city."""
    query = f"""
    [out:json][timeout:25];
    area["name"="{city}"]->.searchArea;
    node["amenity"="{amenity}"](area.searchArea);
    out body;
    """
    print(f"[*] Querying Overpass for amenity: '{amenity}' in {city}...")
    try:
        response = requests.post(OVERPASS_URL, data={'data': query})
        response.raise_for_status()
        data = response.json()
        
        nodes = []
        for element in data['elements']:
            if 'lat' in element and 'lon' in element:
                nodes.append((element['lat'], element['lon']))
        
        print(f"    Found {len(nodes)} nodes.")
        return nodes
    except Exception as e:
        print(f"    [!] Error querying Overpass: {e}")
        return []

def mean_center(coords):
    """Mimics the Rust mean_center function."""
    if not coords:
        return None
    
    sum_lat = sum(lat for lat, lon in coords)
    sum_lon = sum(lon for lat, lon in coords)
    count = len(coords)
    
    return (sum_lat / count, sum_lon / count)

def haversine_distance(lat1, lon1, lat2, lon2):
    """Calculates distance in Kilometers between two lat/lon points."""
    R = 6371.0  # Earth radius in kilometers
    
    dlat = np.radians(lat2 - lat1)
    dlon = np.radians(lon2 - lon1)
    a = np.sin(dlat / 2)**2 + np.cos(np.radians(lat1)) * np.cos(np.radians(lat2)) * np.sin(dlon / 2)**2
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))
    
    return R * c

def error_function(guess, points, target_distances):
    """
    Calculates the total error between the guessed point's distance to centers
    and the actual target distances.
    """
    lat, lon = guess
    error = 0.0
    for (p_lat, p_lon), target_dist in zip(points, target_distances):
        calc_dist = haversine_distance(lat, lon, p_lat, p_lon)
        # We square the difference to penalize larger errors (Least Squares)
        error += (calc_dist - target_dist) ** 2
    return error

def main():
    centers = []
    radii = []
    amenities = ["bar", "atm", "taxi"]

    # 1. Get Data and Calculate Centers
    for amenity in amenities:
        nodes = get_nodes(amenity, CITY_NAME)
        center = mean_center(nodes)
        
        if center:
            print(f"    -> Mean Center for {amenity}: {center}")
            centers.append(center)
            radii.append(DISTANCES[amenity])
        else:
            print(f"    [!] No data found for {amenity}. Exiting.")
            return

    # 2. Perform Trilateration (Optimization)
    print("\n[*] Calculating intersection (Secret Hideout)...")
    
    # Initial guess: Start at the center of the 'bar' mean
    initial_guess = [centers[0][0], centers[0][1]]
    
    result = minimize(
        error_function, 
        initial_guess, 
        args=(centers, radii),
        method='Nelder-Mead',
        tol=1e-6
    )

    if result.success:
        final_lat, final_lon = result.x
        print(f"\n[+] SUCCESS! Calculated Coordinates:")
        print(f"    Latitude:  {final_lat}")
        print(f"    Longitude: {final_lon}")
        print(f"\n    Google Maps Link: https://www.google.com/maps/search/?api=1&query={final_lat},{final_lon}")
        
        # Verification of distances
        print("\n[?] Verification (Calculated vs Expected Distance):")
        for i, amenity in enumerate(amenities):
            d = haversine_distance(final_lat, final_lon, centers[i][0], centers[i][1])
            diff = d - radii[i]
            print(f"    {amenity}: {d:.5f} km (Target: {radii[i]:.5f} km) | Diff: {diff:.5f}")
    else:
        print("[!] Optimization failed to converge.")

if __name__ == "__main__":
    main()

```
