import os
import shutil
import pandas as pd

# Paths to the CSV files and the images folder
csv_files = {
    "Topwear": "topwear.csv",
    "Bottomwear": "bottomwear.csv",
    "Footwear": "footwear.csv",
    "Accessories": "accessories.csv",
}
images_folder = "images"  # Replace with the path to your images folder
output_folder = "categorized_images"  # Folder to save categorized images

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Process each category
for category, csv_file in csv_files.items():
    # Read the CSV file
    data = pd.read_csv(csv_file)
    
    # Get the list of IDs
    ids = set(data["id"].astype(str))  # Convert to string for matching filenames
    
    # Create a folder for the category
    category_folder = os.path.join(output_folder, category)
    os.makedirs(category_folder, exist_ok=True)
    
    # Move images to the category folder
    for image_file in os.listdir(images_folder):
        image_id, ext = os.path.splitext(image_file)  # Extract ID from filename
        if image_id in ids:  # Check if the ID matches
            src = os.path.join(images_folder, image_file)
            dest = os.path.join(category_folder, image_file)
            shutil.copy(src, dest)  # Use shutil.move(src, dest) to move instead of copy

print("Images have been categorized into respective folders!")
