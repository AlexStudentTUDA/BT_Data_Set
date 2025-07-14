#Create the LAMMPS_Submission_INDEX_TIMESTEMP folder full script

#cratetes a Submission_batch_Timestamp folder in /nfshome/okresa/Bachelor_Thesis_Office/Project_Vacancy_Intersetiell_ASE_model/data/LAMMPS_Data/Submited_mini_data_folders/
#moves mini.data folders into Submission_batch_Timestamp folder

import os
import re # To use regular expressions
import datetime
import shutil 

# Define the base directory where folders will be created
base_dir = "/nfshome/okresa/Bachelor_Thesis_Office/Project_Vacancy_Intersetiell_ASE_model/data/LAMMPS_Data"  # Change this to the path you want

# Check if the base directory exists, if not, create it
if not os.path.exists(base_dir):
    os.makedirs(base_dir)

# Find the highest index among existing folders
existing_indexes = []
for folder in os.listdir(base_dir):
    if folder.startswith("LAMMPS_Submision_"):
        # Extract the index from the folder name using regex
        match = re.match(r"LAMMPS_Submision_(\d{3})_\d{2}-\d{2}-\d{4}_\d{2}-\d{2}-\d{2}", folder)
        if match:
            index = int(match.group(1))  # Extracted index from folder name
            existing_indexes.append(index)

# Determine the next available index
index = max(existing_indexes, default=0) + 1

# Now, get the current timestamp
now = datetime.datetime.now()
Timestamp = now.strftime("%d-%m-%Y_%H-%M-%S")

# Final folder name with index and timestamp
folder_name = f"LAMMPS_Submision_{index:03d}_{Timestamp}"
folder_path = os.path.join(base_dir, folder_name)

# Create the new folder
os.makedirs(folder_path)

print(f"Folder created: {folder_path}")

print("Created the LAMMPS_Submission_INDEX_TIMESTEMP folder")

#----------------------------------------------
#copy the folders into the highest indexed directory


# Define the base directories
base_dir = "/nfshome/okresa/Bachelor_Thesis_Office/Project_Vacancy_Intersetiell_ASE_model/data/LAMMPS_Data"
source_dir = "/nfshome/okresa/Bachelor_Thesis_Office/Project_Vacancy_Intersetiell_ASE_model/input/LAMMPS_input/Active_input"

# Function to get the highest index in the target directory
def get_highest_index(base_dir):
    existing_indexes = []
    for folder in os.listdir(base_dir):
        if folder.startswith("LAMMPS_Submision_"):
            # Extract the index from the folder name using regex
            match = re.match(r"LAMMPS_Submision_(\d{3})_\d{2}-\d{2}-\d{4}_\d{2}-\d{2}-\d{2}", folder)
            if match:
                index = int(match.group(1))  # Extracted index from folder name
                existing_indexes.append(index)

    # Return the next available index (highest index + 1)
    return max(existing_indexes, default=0)

# Get the folder with the highest index
highest_index = get_highest_index(base_dir)

# Get the most recent folder (LAMMPS_Submision_{highest_index}_{Timestamp})
target_folder_name = f"LAMMPS_Submision_{highest_index:03d}_"
target_folder_path = None

# Find the target folder
for folder in os.listdir(base_dir):
    if folder.startswith(f"LAMMPS_Submision_{highest_index:03d}_"):
        target_folder_path = os.path.join(base_dir, folder)
        break

# Check if the target folder exists
if target_folder_path:
    print(f"Target folder: {target_folder_path}")
    
    # Copy the content from the source directory (Active_input) to the target folder
    if os.path.exists(source_dir):
        # Iterate through each item in the source directory (Active_input)
        for item in os.listdir(source_dir):
            source_item_path = os.path.join(source_dir, item)
            destination_item_path = os.path.join(target_folder_path, item)
            
            # If it's a directory, copy it
            if os.path.isdir(source_item_path):
                shutil.copytree(source_item_path, destination_item_path)
            else:
                # If it's a file, copy it
                shutil.copy2(source_item_path, destination_item_path)
        
        print(f"All folders from '{source_dir}' have been copied to '{target_folder_path}'.")
    else:
        print(f"Source directory '{source_dir}' does not exist.")
else:
    print(f"Target folder with highest index not found.")




#--------------------------------------------------
#move the 0_ folders into a sub directory and clear Active_input

# Define the base directories
base_dir = "/nfshome/okresa/Bachelor_Thesis_Office/Project_Vacancy_Intersetiell_ASE_model/data/LAMMPS_Data"
source_dir = "/nfshome/okresa/Bachelor_Thesis_Office/Project_Vacancy_Intersetiell_ASE_model/input/LAMMPS_input/Active_input"

# Function to get the highest index in the target directory
def get_highest_index(base_dir):
    existing_indexes = []
    for folder in os.listdir(base_dir):
        if folder.startswith("LAMMPS_Submision_"):
            # Extract the index from the folder name using regex
            match = re.match(r"LAMMPS_Submision_(\d{3})_\d{2}-\d{2}-\d{4}_\d{2}-\d{2}-\d{2}", folder)
            if match:
                index = int(match.group(1))  # Extracted index from folder name
                existing_indexes.append(index)

    # Return the highest index
    return max(existing_indexes, default=0)

# Get the folder with the highest index
highest_index = get_highest_index(base_dir)

# Get the most recent folder (LAMMPS_Submision_{highest_index}_{Timestamp})
target_folder_name = f"LAMMPS_Submision_{highest_index:03d}_"
target_folder_path = None

# Find the target folder
for folder in os.listdir(base_dir):
    if folder.startswith(f"LAMMPS_Submision_{highest_index:03d}_"):
        target_folder_path = os.path.join(base_dir, folder)
        break

# Check if the target folder exists
if target_folder_path:
    print(f"Target folder: {target_folder_path}")
    
    # Create the sub-folder inside the target folder for '0_*' folders
    moved_folders_count = 0  # Keep track of the number of moved folders

    # First, check how many folders starting with '0' are in the source directory
    if os.path.exists(source_dir):
        for item in os.listdir(source_dir):
            source_item_path = os.path.join(source_dir, item)
            
            # If it's a folder and starts with '0', prepare to move it
            if os.path.isdir(source_item_path) and item.startswith("0"):
                moved_folders_count += 1
        
        # Name the sub-folder based on the count of moved folders
        zero_subfolder_name = f"{moved_folders_count}_Submited_mini_data_folders"
        zero_subfolder_path = os.path.join(target_folder_path, zero_subfolder_name)

        if not os.path.exists(zero_subfolder_path):
            os.makedirs(zero_subfolder_path)
            print(f"Created sub-folder: {zero_subfolder_path}")

        # Now move the folders that start with '0' into the new sub-folder
        for item in os.listdir(source_dir):
            source_item_path = os.path.join(source_dir, item)
            destination_item_path = os.path.join(zero_subfolder_path, item)
            
            if os.path.isdir(source_item_path) and item.startswith("0"):
                # Check if the folder already exists, and avoid overwriting
                if os.path.exists(destination_item_path):
                    print(f"Folder '{item}' already exists in the destination. Skipping.")
                else:
                    shutil.move(source_item_path, destination_item_path)
                    print(f"Moved folder '{item}' to '{destination_item_path}'")
        
        print(f"All '0' folders from '{source_dir}' have been moved to '{zero_subfolder_path}'.")

        # Now, delete the original '0_*' folders from the target folder
        for item in os.listdir(target_folder_path):
            source_item_path = os.path.join(target_folder_path, item)
            if os.path.isdir(source_item_path) and item.startswith("0"):
                try:
                    # Delete the folder after moving
                    shutil.rmtree(source_item_path)
                    print(f"Deleted original folder: {source_item_path}")
                except Exception as e:
                    print(f"Error deleting folder {source_item_path}: {e}")
    else:
        print(f"Source directory '{source_dir}' does not exist.")
else:
    print(f"Target folder with highest index not found.")

#Script to Clear the Content of Active_input
# Define the target directories
directories_to_clear = [
    "/nfshome/okresa/Bachelor_Thesis_Office/Project_Vacancy_Intersetiell_ASE_model/input/LAMMPS_input/Active_input/mini_data_Structures",
    "/nfshome/okresa/Bachelor_Thesis_Office/Project_Vacancy_Intersetiell_ASE_model/input/LAMMPS_input/Active_input/POSCAR_Structures"
]

# Function to clear the contents of a directory
def clear_directory(directory):
    if os.path.exists(directory):
        # Iterate over all files and subdirectories in the target directory
        for item in os.listdir(directory):
            item_path = os.path.join(directory, item)
            
            try:
                if os.path.isdir(item_path):
                    # If it's a directory, remove it and all its contents
                    shutil.rmtree(item_path)
                    print(f"Deleted directory: {item_path}")
                else:
                    # If it's a file, delete it
                    os.remove(item_path)
                    print(f"Deleted file: {item_path}")
            except Exception as e:
                print(f"Error deleting {item_path}: {e}")
    else:
        print(f"Directory {directory} does not exist.")

# Clear the content of both directories
for directory in directories_to_clear:
    clear_directory(directory)

print("\nmoved the 0_ folders into a sub directory and cleared Active_input")
print("\nnote that the process in only completed after writing a comment")

#------------------------------------
#Comment the LAMMPS Submission batch



# Define the base directory
base_dir = "/nfshome/okresa/Bachelor_Thesis_Office/Project_Vacancy_Intersetiell_ASE_model/data/LAMMPS_Data"

# Function to get the highest index in the target directory
def get_highest_index(base_dir):
    existing_indexes = []
    for folder in os.listdir(base_dir):
        if folder.startswith("LAMMPS_Submision_"):
            # Extract the index from the folder name using regex
            match = re.match(r"LAMMPS_Submision_(\d{3})_\d{2}-\d{2}-\d{4}_\d{2}-\d{2}-\d{2}", folder)
            if match:
                index = int(match.group(1))  # Extracted index from folder name
                existing_indexes.append(index)

    # Return the highest index
    return max(existing_indexes, default=0)

# Get the folder with the highest index
highest_index = get_highest_index(base_dir)

# Get the current timestamp to append to the comment file
now = datetime.datetime.now()
timestamp = now.strftime("%d-%m-%Y_%H-%M-%S")

# Get the most recent folder (LAMMPS_Submision_{highest_index}_{Timestamp})
target_folder_name = f"LAMMPS_Submision_{highest_index:03d}_"
target_folder_path = None

# Find the target folder
for folder in os.listdir(base_dir):
    if folder.startswith(f"LAMMPS_Submision_{highest_index:03d}_"):
        target_folder_path = os.path.join(base_dir, folder)
        break

# Check if the target folder exists
if target_folder_path:
    print(f"Target folder: {target_folder_path}")

    # Create the "Submission_comment_{index}_{Timestamp}.txt" file inside the target folder
    comment_file_name = f"zz_Submission_comment_{timestamp}.txt"
    comment_file_path = os.path.join(target_folder_path, comment_file_name)

    # Ask the user for a comment to write in the text file
    print("\nPlease enter your comment for the submitted files below.\nWhen you're finished, type 'exit' to stop.")
    comment_lines = []
    while True:
        line = input("Your comment: ")
        if line.lower() == 'exit':
            break
        comment_lines.append(line)
    
    # Write the comment to the file
    with open(comment_file_path, 'w') as f:
        for line in comment_lines:
            f.write(line + '\n')

    print(f"Your comment has been written to '{comment_file_path}'.")

else:
    print(f"Target folder with highest index not found.")

	
