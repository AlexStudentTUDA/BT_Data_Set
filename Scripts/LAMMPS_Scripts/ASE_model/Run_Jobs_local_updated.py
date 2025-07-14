# Function to run LAMMPS locally UPDATE included queue.
import os
import subprocess
import time
from pathlib import Path
import psutil  # Make sure this is installed (pip install psutil)

# Path to local LAMMPS executable
lmp_path = os.path.expanduser('~/LAMMPS/Executable_LAMMPS/lmp')

# Check if a LAMMPS process is currently running
def is_lammps_running():
    for proc in psutil.process_iter(attrs=['name', 'cmdline']):
        try:
            if 'lmp' in proc.info['name'] or any('lmp' in cmd for cmd in proc.info['cmdline']):
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return False

# Helper function to run a simulation locally
def run_lammps_queued(input_file, cwd):
    log_file = Path(cwd) / 'out.log'
    if log_file.exists():
        print(f'Skipping {cwd} — out.log already exists.')
        return

    print(f'Waiting to run: {cwd}')
    while is_lammps_running():
        print('LAMMPS is already running. Waiting 10 seconds...')
        time.sleep(10)

    print(f'Running: {cwd}')
    
    # Extract temperature from folder name
    folder_name = Path(cwd).name
    if folder_name.startswith('T_'):
        temp_val = folder_name[2:]
    else:
        raise ValueError(f"Cannot extract temperature from folder name: {folder_name}")

    with open(log_file, 'w') as out:
        subprocess.run(
            [lmp_path, '-in', input_file, '-var', 'temp', temp_val],
            cwd=cwd,
            stdout=out,
            stderr=subprocess.STDOUT
        )
    print(f'Finished: {cwd}\n')

# Root folder for input cases
base_path = Path('/nfshome/okresa/Bachelor_Thesis_Office/Project_Vacancy_Intersetiell_ASE_model/input/LAMMPS_input/Active_input')

# Queued run for each case
for p in base_path.glob('0_basic*/T_*'):
    run_lammps_queued('equilibrate.in', cwd=p)

for p in base_path.glob('0_print*/T_*'):
    run_lammps_queued('equilibrate_print_steps.in', cwd=p)

for p in base_path.glob('0_MD*/T_*'):
    if '0_MD_long' not in str(p):
        run_lammps_queued('equilibrate_MD.in', cwd=p)

for p in base_path.glob('0_MD_long*/T_*'):
    run_lammps_queued('equilibrate_MD_long.in', cwd=p)

print('All simulations queued and run sequentially.')




	
