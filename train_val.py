import pandas as pd
from sklearn.model_selection import train_test_split

# Define the file paths for each category
csv_files = {
    "Topwear": "topwear.csv",
    "Bottomwear": "bottomwear.csv",
    "Footwear": "footwear.csv",
    "Accessories": "accessories.csv",
}

# Define the classification rules for the categories
classification_rules = {
    "Topwear": ["Topwear", "Shirts", "Tshirts", "Sweatshirts", "Jackets"],
    "Bottomwear": ["Bottomwear", "Jeans", "Track Pants", "Shorts", "Skirts"],
    "Footwear": ["Footwear", "Shoes", "Sandals", "Flip Flops"],
    "Accessories": ["Accessories", "Watches", "Bags", "Belts", "Jewellery"],
}

# Function to classify each row based on articleType or subCategory
def classify_row(row, classification_rules):
    for category, keywords in classification_rules.items():
        if row["subCategory"] in keywords or row["articleType"] in keywords:
            return category
    return "Other"

# Function to split and save the data
def split_and_save(csv_file, category_name, classification_rules):
    # Load the data
    data = pd.read_csv(csv_file)

    # Add the 'Category' column based on the classification rules
    data["Category"] = data.apply(classify_row, axis=1, classification_rules=classification_rules)

    # Perform stratified split: 80% for training, 20% for validation
    train_data, val_data = train_test_split(
        data,
        test_size=0.2,            # 20% for validation
        random_state=42,          # Ensures reproducibility
        stratify=data["Category"] # Ensures balanced categories in both sets
    )

    # Save the splits into separate files
    train_data.to_csv(f"train_{category_name}.csv", index=False)
    val_data.to_csv(f"val_{category_name}.csv", index=False)

    print(f"Split for {category_name} complete.")
    print(f"Training data: {len(train_data)} rows, Validation data: {len(val_data)} rows")
    print(f"Training data categories:\n{train_data['Category'].value_counts()}")
    print(f"Validation data categories:\n{val_data['Category'].value_counts()}")

# Loop through each file and perform the splitting
for category, file in csv_files.items():
    split_and_save(file, category, classification_rules)
