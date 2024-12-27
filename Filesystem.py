import os
import shutil

# Define categories and file extensions
FILE_TYPES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg'],
    'Videos': ['.mp4', '.mov', '.avi', '.mkv', '.flv'],
    'Documents': ['.pdf', '.docx', '.doc', '.txt', '.pptx', '.xlsx'],
    'Music': ['.mp3', '.wav', '.aac', '.flac'],
    'Archives': ['.zip', '.rar', '.tar', '.gz', '.7z'],
    'Programs': ['.exe', '.msi']
}

# Function to organize files
def organize_files(directory):
    if not os.path.exists(directory):
        print(f"The directory {directory} does not exist.")
        return

    # Create folders if they don't exist
    for category in FILE_TYPES.keys():
        folder_path = os.path.join(directory, category)
        os.makedirs(folder_path, exist_ok=True)

    # Move files to corresponding folders
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Move file to appropriate folder
        moved = False
        for category, extensions in FILE_TYPES.items():
            if any(filename.lower().endswith(ext) for ext in extensions):
                shutil.move(file_path, os.path.join(directory, category, filename))
                moved = True
                break

        if not moved:
            # Move uncategorized files to "Others"
            other_folder = os.path.join(directory, 'Others')
            os.makedirs(other_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(other_folder, filename))

    print("Files organized successfully!")

# Main execution
if __name__ == "__main__":
    folder_to_organize = input("Enter the folder path to organize: ").strip()
    organize_files(folder_to_organize)
