# Function to run LAMMPS locally.
import os
import subprocess
import time
from pathlib import Path
import psutil
import re

# Path to local LAMMPS executable
lmp_path = Path('~/LAMMPS/Executable_LAMMPS/lmp').expanduser()

if not lmp_path.exists():
    raise FileNotFoundError(f"LAMMPS executable not found at {lmp_path}")

def is_lammps_running():
    for proc in psutil.process_iter(attrs=['name', 'cmdline']):
        try:
            if 'lmp' in proc.info['name'] or any('lmp' in cmd for cmd in proc.info['cmdline']):
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return False

def extract_temp_from_submit_script(folder_path):
    for file in folder_path.glob("submit-lammps-ml_*_GPU_Version.sh"):
        try:
            content = file.read_text()
            match = re.search(r'-var\s+temp\s+(\d+)', content)
            if match:
                return match.group(1)
        except Exception as e:
            raise RuntimeError(f"Error reading {file}: {e}")
    return None  # No match found

def run_lammps_queued(input_file, cwd):
    cwd = Path(cwd)
    log_file = cwd / 'out.log'
    input_path = cwd / input_file

    if log_file.exists():
        print(f'[SKIP] {cwd} — out.log already exists.')
        return

    if not input_path.exists():
        raise FileNotFoundError(f"[ERROR] Input file not found: {input_path}")

    print(f'[WAIT] Queueing: {cwd}')
    while is_lammps_running():
        print('[INFO] LAMMPS already running. Waiting 10 seconds...')
        time.sleep(10)

    # Get temperature from script or folder name
    temp_val = extract_temp_from_submit_script(cwd)
    if not temp_val:
        folder_name = cwd.name
        if folder_name.startswith('T_') and folder_name[2:].isdigit():
            temp_val = folder_name[2:]
        else:
            raise ValueError(f"[ERROR] Cannot extract temperature from script or folder name: {cwd}")

    print(f'[RUN] {cwd} | Input: {input_file} | Temp: {temp_val}')

    try:
        with open(log_file, 'w') as out:
            subprocess.run(
                [str(lmp_path), '-in', input_file, '-var', 'temp', temp_val],
                cwd=cwd,
                stdout=out,
                stderr=subprocess.STDOUT,
                check=True  # Raises exception if LAMMPS fails
            )
    except subprocess.CalledProcessError as e:
        print(f'[ERROR] LAMMPS failed in {cwd} — check input file or output')
        log_file.unlink(missing_ok=True)  # Delete partial log
        raise e

    print(f'[DONE] Finished: {cwd}\n')

# Root path
base_path = Path('/nfshome/okresa/Bachelor_Thesis_Office/Project_Vacancy_Intersetiell_ASE_model/input/LAMMPS_input/Active_input')

# Execution
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




	
