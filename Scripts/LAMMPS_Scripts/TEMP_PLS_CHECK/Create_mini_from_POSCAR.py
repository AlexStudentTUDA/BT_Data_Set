from ase.io import read, write

atoms = read("POSCAR")
atoms.wrap()
write("mini.data",atoms,format="lammps-data",specorder=['Ga','Cu','Ag','Se'])

# yaml to yace
# run to command line
# pace_yaml2yace output_potential.yaml

