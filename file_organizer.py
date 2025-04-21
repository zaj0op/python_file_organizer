import os
import shutil

# Define the folder to organize and where to store organized files
folder_to_organize = "filepath\\to_organize"

# Define file type categories
file_categories = {
    "Documents": [".pdf", ".docx", ".txt"],
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Music": [".mp3", ".wav"],
    "Videos": [".mp4", ".mov"],
    "Others": []  # For any file types not covered above
}

# Function to organize files
def organize_files(folder):
    for file_name in os.listdir(folder):
        # Skip if it's a directory
        if os.path.isdir(os.path.join(folder, file_name)):
            continue

        # Get file extension
        _, extension = os.path.splitext(file_name)

        # Determine folder based on file type
        moved = False
        for category, extensions in file_categories.items():
            if extension in extensions:
                move_file(file_name, category, folder)
                moved = True
                break
        
        # If file type not found, move to 'Others'
        if not moved:
            move_file(file_name, "Others", folder)

# Helper function to move files to a specified folder
def move_file(file_name, folder_name, root_folder):
    target_folder = os.path.join(root_folder, folder_name)
    os.makedirs(target_folder, exist_ok=True)
    shutil.move(os.path.join(root_folder, file_name), os.path.join(target_folder, file_name))
    print(f"Moved {file_name} to {folder_name}")

# Run the organizer
organize_files(folder_to_organize)