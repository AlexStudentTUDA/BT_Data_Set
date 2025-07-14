# Function to run LAMMPS locally.
import os
import subprocess
from pathlib import Path

# Path to local LAMMPS executable
lmp_path = os.path.expanduser('~/LAMMPS/Executable_LAMMPS/lmp')

# Helper function to run a simulation locally
def run_lammps(input_file, cwd):
    log_file = Path(cwd) / 'out.log'
    with open(log_file, 'w') as out:
        subprocess.run(
            [lmp_path, '-in', input_file, '-var', 'temp', '0'],
            cwd=cwd,
            stdout=out,
            stderr=subprocess.STDOUT
        )

# Loop through folders and run simulations
base_path = Path('/nfshome/okresa/Bachelor_Thesis_Office/Project_Vacancy_Intersetiell_ASE_model/input/LAMMPS_input/Active_input')

for p in base_path.glob('0_basic*/T_*'):
    run_lammps('equilibrate.in', cwd=p)

for p in base_path.glob('0_print*/T_*'):
    run_lammps('equilibrate_print_steps.in', cwd=p)

for p in base_path.glob('0_MD*/T_*'):
    if '0_MD_long' not in str(p):
        run_lammps('equilibrate_MD.in', cwd=p)

for p in base_path.glob('0_MD_long*/T_*'):
    run_lammps('equilibrate_MD_long.in', cwd=p)

print('Confirm Submission')




	
