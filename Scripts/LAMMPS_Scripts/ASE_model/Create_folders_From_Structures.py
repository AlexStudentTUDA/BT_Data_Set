import subprocess
import os
import numpy as np
from pyace import *
from ase.io import read
import os
import gzip
import shutil
import numpy as np
import matplotlib.pyplot as plt

# Source directory where POSCAR files are located
source_directory = '/nfshome/karanikv/TEST_Potential/Sigma3/LAMMPS_Sigma3/Structures'

# Get a list of POSCAR files
data_files = [filename for filename in os.listdir(source_directory) if filename.endswith('.data')]

# Destination directory where you want to create the folders
destination_directory = '/nfshome/karanikv/TEST_Potential/Sigma3/LAMMPS_Sigma3'  # Use the current working directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# List of additional files to copy (from the main directory)
additional_files = [
    "equilibrate.in",
    "submit-lammps-ml_GPU_Version.sh",
]

Temperatures = [50]

# Loop through each POSCAR file
for data_file in data_files:
    Data = os.path.join(source_directory, f"{data_file}")
    print(Data)
    # Check if the POSCAR file exists in the source directory
    source_path = os.path.join(source_directory, data_file)
    if not os.path.exists(source_path):
       print(f"Error: '{poscar_file}' not found in '{source_directory}'. Skipping...")
       continue  # Skip to the next iteration

    folder_name = f"{data_file}" # Extract folder name
    folder_path = os.path.join(destination_directory, folder_name)

    # Create the folder if it doesn't exist
    os.makedirs(folder_path, exist_ok=True)

    # Loop through each temperature
    for Temperature in Temperatures:
        temp_folder = os.path.join(folder_path, f'T_{Temperature}')

        # Create a subfolder for the current temperature
        os.makedirs(temp_folder, exist_ok=True)

        # Copy the POSCAR file to the subfolder
        source_path = os.path.join(source_directory, data_file)
        destination_path = os.path.join(temp_folder, 'mini.data')
        shutil.copy(source_path, destination_path)

        # Copy additional files from the main directory to the subfolder with temperature-specific variations
        for file_name in additional_files:
            source_file_path = os.path.join(script_dir, file_name)  # Use the full path to the additional files
            dest_file_path = os.path.join(temp_folder, file_name)
            shutil.copy(source_file_path, dest_file_path)
        
        print(f"Copied {data_file} to {temp_folder}")

    print(f"Processed {data_file}")

print("Copying and script execution completed.")











