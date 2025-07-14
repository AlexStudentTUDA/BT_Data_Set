import os
import shutil
import numpy as np
from ase.io import read, write

script_dir = os.path.dirname(os.path.abspath(__file__))
poscar_file = os.path.join(script_dir,'POSCAR')
cryst = read(poscar_file, format="vasp")

# Create a bulk and remove a sphere

supercell = cryst*(30,30,20)
#center of the cell
coc = supercell.get_cell()[0]/2+supercell.get_cell()[1]/2+supercell.get_cell()[2]/2
print(coc)
radius_1=50.0
del_coord = []
for i in range(0,len(supercell.get_positions())):
	pos = supercell.get_positions()[i]
	if np.linalg.norm(coc-pos)<radius_1-1:
                del_coord.append(i)

for s in reversed(sorted(del_coord)):
      del supercell[s]
write("POSCAR_Rest",supercell,format="vasp")
print(len(list(supercell.symbols)))

#Create a sphere
seed = cryst*(30,30,20)
radius_2=49.2
del_coord = []
for i in range(0,len(seed.get_positions())):
	pos = seed.get_positions()[i]
	if np.linalg.norm(coc-pos)>radius_2-1:
		del_coord.append(i)

for s in reversed(sorted(del_coord)):
      del seed[s]
seed.wrap()
seed.rotate(22.5, 'z',center=coc)
write("POSCAR_Sphere",seed,format="vasp")

'''

# Read the POSCAR files and assemple the final structure

poscar_file = os.path.join(script_dir,'POSCAR_Sphere')
seed = read(poscar_file, format="vasp")
print(len(list(seed.symbols)))

poscar_file = os.path.join(script_dir,'POSCAR_Rest')
supercell = read(poscar_file, format="vasp")

supercell = supercell + seed
supercell.wrap()
print(len(list(supercell.symbols)))

write("POSCAR_Seed",supercell,format="vasp")
write("mini.data", supercell, format="lammps-data", specorder=['Ga', 'Cu', 'Ag', 'Se','Zn', 'Ni', 'Pd', 'As'])
'''
