#!/bin/bash

#SBATCH --cpus-per-task=4
#SBATCH --mem-per-cpu=3750
#SBATCH --ntasks=1
#SBATCH -J TESTRUN
#SBATCH -e err.%j
#SBATCH -o out.%j
#SBATCH -t 72:00:00
#SBATCH --gres=gpu:1
#---------------


~/LAMMPS/Executable_LAMMPS/lmp -k on g $SLURM_NTASKS -sf kk -pk kokkos newton on neigh half  -in equilibrate.in -var temp 50 | tee out.log





