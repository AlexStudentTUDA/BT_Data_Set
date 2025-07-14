#Kommentar zu LAMMPS Submission batch
#Comment the LAMMPS Submission batch

import os
import re
import datetime

# Define the base directory
base_dir = "/nfshome/okresa/Bachelor_Thesis_Office/Project_Vacancy_Intersetiell_ASE_model/data/LAMMPS_Data"

# Function to get the highest index in the target directory
def get_highest_index(base_dir):
    existing_indexes = []
    for folder in os.listdir(base_dir):
        if folder.startswith("LAMMPS_Submision_"):
            # Extract the index from the folder name using regex
            match = re.match(r"LAMMPS_Submision_(\d{3})_\d{2}-\d{2}-\d{4}_\d{2}:\d{2}:\d{2}", folder)
            if match:
                index = int(match.group(1))  # Extracted index from folder name
                existing_indexes.append(index)

    # Return the highest index
    return max(existing_indexes, default=0)

# Get the folder with the highest index
highest_index = get_highest_index(base_dir)

# Get the current timestamp to append to the comment file
now = datetime.datetime.now()
timestamp = now.strftime("%d-%m-%Y_%H:%M:%S")

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



	
