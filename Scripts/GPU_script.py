import os
import shutil
import subprocess

# Current working directory
current_directory = os.getcwd()

# Get a list of all directories in the current directory
all_folders = [name for name in os.listdir(current_directory) if os.path.isdir(os.path.join(current_directory, name))]

# Iterate through each folder
for folder_name in all_folders:
    # Check if the folder contains .vasp files
    folder_path = os.path.join(current_directory, folder_name)
    vasp_files = [filename for filename in os.listdir(folder_path) if filename.endswith('.vasp')]

    if vasp_files:
        print(f"Processing folder: {folder_name}")

        # Change directory to the folder
        os.chdir(folder_path)

        # Execute the script (assuming it's in the folder)
        script_path = os.path.join(folder_path, 'submit-lammps-ml_GPU_Version.sh')
        subprocess.run(['sbatch', 'submit-lammps-ml_GPU_Version.sh'])
