import os
import json
from datetime import datetime

def generate_asset_metadata(folder_path):
    asset_metadata = {}
    
    # Iterate over each folder in the specified directory
    for folder_name in os.listdir(folder_path):
        folder_full_path = os.path.join(folder_path, folder_name)
        
        if os.path.isdir(folder_full_path):
            images = []
            
            # Iterate over each file in the folder
            for file_name in os.listdir(folder_full_path):
                if file_name.endswith('.svg'):  # Assuming SVG files
                    image_path = os.path.join(folder_full_path, file_name)
                    image_name = os.path.splitext(file_name)[0]
                    
                    # Create image metadata
                    image_metadata = {
                        'imageUrl': f'/images/{folder_name}/{file_name}',
                        'imageName': image_name,
                        'imageCreatedAt': datetime.now().strftime('%Y-%m-%d'),
                        'tags': []  # Empty tags for manual input
                    }
                    
                    images.append(image_metadata)
            
            # Add folder metadata
            asset_metadata[folder_name] = {
                'categoryName': folder_name.capitalize(),
                'icon': f'/icons/{folder_name}.svg',
                'images': images
            }
    
    return asset_metadata

# Specify the path to the folder containing the images
folder_path = './images'  # Update this path
metadata = generate_asset_metadata(folder_path)

# Write the JSON structure to index.js
with open('index.js', 'w') as js_file:
    js_file.write('export const assetMetadata = ')
    js_file.write(json.dumps(metadata, indent=2))
    js_file.write(';\n\n')