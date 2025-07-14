import os
import shutil
import numpy as np
from ase.io import read, write

script_dir = os.path.dirname(os.path.abspath(__file__))
poscar_file = os.path.join(script_dir,'POSCAR')
cryst = read(poscar_file, format="vasp")
print(cryst.get_cell())
supercell = cryst*(8,8,8)
print(len(list(supercell.symbols)))
#Ag_number = Number_Atoms.count('Ag')
#Cu_number = Number_Atoms.count('Cu')
#print(supercell.get_cell())
coc = supercell.get_cell()[0]/2+supercell.get_cell()[1]/2+supercell.get_cell()[2]/2
print(coc)
radius=15.0#supercell.cell.cellpar()[0]/2.5
print(radius)


del_coord = []
for i in range(0,len(supercell.get_positions())):
	pos = supercell.get_positions()[i]
	if np.linalg.norm(coc-pos)<radius-1:
                #print(pos)
                del_coord.append(i)
		#print(pos)

for s in reversed(sorted(del_coord)):
      #print(supercell[s])
      del supercell[s]

print(len(list(supercell.symbols)))


seed = cryst*(8,8,8)
print(len(list(seed.symbols)))
#seed.translate(coc)
#seed.wrap()
#seed.rotate(90, 'z')

del_coord = []
for i in range(0,len(seed.get_positions())):
	pos = seed.get_positions()[i]
	
	if np.linalg.norm(coc-pos)>radius-1:
		del_coord.append(i)
		#print(pos)
print(len(del_coord))
for s in reversed(sorted(del_coord)):
      #print(supercell[s])
      del seed[s]
seed.wrap()
seed.rotate(22.5, 'z',center=coc)
print(len(list(seed.symbols)))

supercell = supercell + seed
supercell.wrap()
print(len(list(supercell.symbols)))

write("POSCAR_Seed",supercell,format="vasp")
write("mini.data", supercell, format="lammps-data", specorder=['Ga', 'Cu', 'Ag', 'Se'])


'''
seed.wrap()
seed.rotate('x','y')
coc = seed.get_cell()[0]/2+seed.get_cell()[1]+seed.get_cell()[2]
del_coord = []
for i in range(0,len(seed.get_positions())):
	pos = seed.get_positions()[i]
	
	if np.linalg.norm(pos-coc)<radius:
		del_coord.append(i)

seed.translate(-coc+coords)
supercell.extend(seed)

write("POSCAR_Seed",supercell,format="vasp")

'''
