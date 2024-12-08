import os
import shutil
import pandas as pd

# Define the CSV files (train and validation) for each category
csv_files = {
    "Topwear": {"train": "train_Topwear.csv", "val": "val_Topwear.csv"},
    "Bottomwear": {"train": "train_Bottomwear.csv", "val": "val_Bottomwear.csv"},
    "Footwear": {"train": "train_Footwear.csv", "val": "val_Footwear.csv"},
    "Accessories": {"train": "train_Accessories.csv", "val": "val_Accessories.csv"},
}

# Define the base directory where the categorized images are located
base_image_dir = 'categorized_images'

# Function to move images into corresponding train/val folders
def move_images(csv_file, category, set_type):
    # Load the CSV file (train or validation data)
    data = pd.read_csv(csv_file)
    
    # Assuming each row has an 'id' column that corresponds to the image file name (without extension)
    image_ids = data['id'].tolist()  # Modify this if the column name is different
    
    # Define the source and destination directories
    source_dir = os.path.join(base_image_dir, category)  # Source images are in 'Topwear', 'Bottomwear', etc.
    target_dir = os.path.join(base_image_dir, f"{set_type}_{category}")  # Target is 'train_Topwear', 'val_Topwear', etc.

    # Create the target directory if it doesn't exist
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    # Move the images corresponding to the current set (train/val)
    for image_id in image_ids:
        image_file = f"{image_id}.jpg"  # Assuming the image file has a '.jpg' extension (adjust as needed)
        source_path = os.path.join(source_dir, image_file)
        target_path = os.path.join(target_dir, image_file)

        # Check if the image exists in the source directory and move it
        if os.path.exists(source_path):
            shutil.move(source_path, target_path)
            print(f"Moved {image_file} to {target_dir}")
        else:
            print(f"Image {image_file} not found in {source_dir}.")

# Loop through each category and its corresponding train/val CSV files
for category, files in csv_files.items():
    # Move images for training set
    move_images(files["train"], category, "train")
    
    # Move images for validation set
    move_images(files["val"], category, "val")
