import pandas as pd

# Load the dataset with error handling for problematic rows
file_path = 'styles.csv'  # Replace with your dataset path
try:
    data = pd.read_csv(file_path, on_bad_lines='skip', encoding='utf-8')  # Skip problematic lines
except Exception as e:
    print(f"Error loading file: {e}")
    exit()

# Define the classification rules for the four categories
classification_rules = {
    "Topwear": ["Topwear", "Shirts", "Tshirts", "Sweatshirts", "Jackets"],
    "Bottomwear": ["Bottomwear", "Jeans", "Track Pants", "Shorts", "Skirts"],
    "Footwear": ["Footwear", "Shoes", "Sandals", "Flip Flops"],
    "Accessories": ["Accessories", "Watches", "Bags", "Belts", "Jewellery"],
}

# Function to classify each row based on subCategory and articleType
def classify_row(row):
    for category, keywords in classification_rules.items():
        if row["subCategory"] in keywords or row["articleType"] in keywords:
            return category
    return "Other"

# Apply the classification function to the dataset
data["Category"] = data.apply(classify_row, axis=1)

# Split and save the dataset for each category
output_paths = {
    "Topwear": "topwear.csv",
    "Bottomwear": "bottomwear.csv",
    "Footwear": "footwear.csv",
    "Accessories": "accessories.csv"
}

for category, path in output_paths.items():
    # Create a copy of the filtered data
    filtered_data = data[data["Category"] == category].copy()
    filtered_data.drop(columns=["Category"], inplace=True)  # Remove the Category column
    filtered_data.to_csv(path, index=False)
