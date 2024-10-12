import os
import shutil

def organize_files(source_dir, destination_dirs):
    """
    Organizes files in the source directory based on their extensions.

    :param source_dir: The path to the folder with unorganized files.
    :param destination_dirs: A dictionary mapping file extensions to destination folders.
    """
    # Create the destination folders if they do not exist
    for folder in destination_dirs.values():
        os.makedirs(folder, exist_ok=True)

    # Loop through all the files in the source directory
    for file_name in os.listdir(source_dir):
        # Check if it's a file (ignore directories)
        if os.path.isfile(os.path.join(source_dir, file_name)):
            # Get the file extension (e.g., 'pdf', 'jpg')
            file_ext = file_name.split('.')[-1].lower()

            # If the extension matches any in destination_dirs, move the file
            if file_ext in destination_dirs:
                source_path = os.path.join(source_dir, file_name)
                destination_path = os.path.join(destination_dirs[file_ext], file_name)

                # Move the file
                shutil.move(source_path, destination_path)
                print(f'Moved: {file_name} to {destination_dirs[file_ext]}')

    print("File organization completed!")

def main():
    # Get the source directory from the user
    source_dir = input("Enter the path of the folder with unorganized files: ").strip()
    if not os.path.isdir(source_dir):
        print("Invalid source directory. Please try again.")
        return

    # Get destination directories for different file types
    destination_dirs = {
        'pdf': os.path.join(source_dir, 'PDFs'),
        'jpg': os.path.join(source_dir, 'Images'),
        'png': os.path.join(source_dir, 'Images'),
        'docx': os.path.join(source_dir, 'Documents'),
        'txt': os.path.join(source_dir, 'TextFiles')
    }

    # Run the organization function
    organize_files(source_dir, destination_dirs)

if __name__ == "__main__":
    main()
