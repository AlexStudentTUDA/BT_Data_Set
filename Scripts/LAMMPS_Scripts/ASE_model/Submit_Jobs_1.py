import os
import subprocess
from pathlib import Path
from shutil import copy2

# Function to submit job to the cluster
#original:
#for p in Path('.').glob('Ga*/T_*'):
#    subprocess.run(['sbatch', 'submit-lammps-ml_GPU_Version.sh'], cwd=p)

#v1 (old layout)
#for p in Path('/nfshome/okresa/Bachelor_Thesis_Office/Project_Vacancy_Intersetiell_ASE_model/input/LAMMPS_input/Active_input_1').glob('*rep.data/T_*'):
    #subprocess.run(['sbatch', 'submit-lammps-ml_GPU_Version.sh'], cwd=p)
for p in Path('/nfshome/okresa/Bachelor_Thesis_Office/Project_Vacancy_Intersetiell_ASE_model/input/LAMMPS_input/Active_input_1').glob('0_basic*/T_*'):
    subprocess.run(['sbatch', 'submit-lammps-ml_GPU_Version.sh'], cwd=p)
for p in Path('/nfshome/okresa/Bachelor_Thesis_Office/Project_Vacancy_Intersetiell_ASE_model/input/LAMMPS_input/Active_input_1').glob('0_print*/T_*'):
    subprocess.run(['sbatch', 'submit-lammps-ml_print_steps_GPU_Version.sh'], cwd=p)
for p in Path('/nfshome/okresa/Bachelor_Thesis_Office/Project_Vacancy_Intersetiell_ASE_model/input/LAMMPS_input/Active_input_1').glob('0_MD*/T_*'):
    if '0_MD_long' not in str(p):
        subprocess.run(['sbatch', 'submit-lammps-ml_MD_GPU_Version.sh'], cwd=p)
for p in Path('/nfshome/okresa/Bachelor_Thesis_Office/Project_Vacancy_Intersetiell_ASE_model/input/LAMMPS_input/Active_input_1').glob('0_MD_long*/T_*'):
    subprocess.run(['sbatch', 'submit-lammps-ml_MD_long_GPU_Version.sh'], cwd=p)

#v2 problematic
"""
for p in Path('/nfshome/okresa/Bachelor_Thesis_Office/Project_Vacancy_Intersetiell_ASE_model/input/LAMMPS_input/Active_input_1').glob('*mini.data/T_*'):
    subprocess.run(['sbatch', 'submit-lammps-ml_MD_GPU_Version.sh'], cwd=p)
    subprocess.run(['sbatch', 'submit-lammps-ml_print_steps_GPU_Version.sh'], cwd=p)
    subprocess.run(['sbatch', 'submit-lammps-ml_MD_GPU_Version.sh'], cwd=p)

print('Errors can be ignored')
"""



print('Confirm Submission')


	
