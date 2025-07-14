import os
import subprocess
from pathlib import Path
from shutil import copy2

# Function to submit job to the cluster
#original:
#for p in Path('.').glob('Ga*/T_*'):
#    subprocess.run(['sbatch', 'submit-lammps-ml_GPU_Version.sh'], cwd=p)

print('pls tell me if this shit works')

#for p in Path('/nfshome/okresa/LAMMPS/LAMMPS_Workspace/Sigma9_repetitions_1_2_4').glob('_*rep_*/T_*'):
for p in Path('/nfshome/okresa/LAMMPS/LAMMPS_Workspace/Sigma9_repetitions_1_2_4').glob('_*rep_*/T_*'):
    subprocess.run(['sbatch', 'submit-lammps-ml_GPU_Version.sh'], cwd=p)



	
