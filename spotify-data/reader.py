import os
import json

directory_path = "spotify-data\Spotify Account Data"

for item in os.listdir(directory_path):
    item_path = os.path.join(directory_path, item)
    if os.path.isfile(item_path) and item.startswith('Payments'):

        print(f"opening {item}\n")
        
        with open(item_path, 'r') as file:
            data = json.load(file)
            print(json.dumps(data, indent=4))