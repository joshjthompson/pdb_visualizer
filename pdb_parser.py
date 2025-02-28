#Handles .pdb file parsing using BioPython (Bio.PDB)
from Bio.PDB import PDBParser
import numpy as np
from scipy.spatial import KDTree

bond_thresholds={
	('C','C'): 1.54,
	('C','H'): 1.09, ('H','C'): 1.09, 
	('C','O'): 1.43, ('O','C'): 1.43, 
	('C','N'): 1.47, ('N','C'): 1.47, 
	('N','H'): 1.01, ('H','N'): 1.01, 
	('O','H'): 0.96, ('H','O'): 0.96, 
	('S','S'): 2.05, 
	('S','C'): 1.81, ('C','S'): 1.81, 
	('P','O'): 1.61, ('O','P'): 1.61, 
	('FE','S'): 2.3, ('S','FE'): 2.3, 
	('MG','O'): 2.1, ('O','MG'): 2.1 
}

def euclidean_distance(coord1,coord2): 
	return np.linalg.norm(np.array(coord1)-np.array(coord2))

def parse_pdb(file_path): 
	parser=PDBParser(QUIET=True) 
	structure=parser.get_structure('my_molecule',file_path)
	
	atoms=[]
	bonds=[]
	
	for model in structure: 
		for chain in model: 
			for residue in chain: 
				for atom in residue: 
					if residue.id[0]==' ': 
						atoms.append({
							'element': atom.element, 
							'coord': atom.coord.tolist(), 
							'chain': chain.id, 
							'residue': residue.get_resname()
						})
	
	atom_positions=np.array([atom['coord'] for atom in atoms])
	
	tree =KDTree(atom_positions)
	max_bond_distance=max(bond_thresholds.values())
	neighbor_pairs=tree.query_pairs(max_bond_distance) 
	
	for i,j in neighbor_pairs: 
		atom1,atom2=atoms[i],atoms[j]
		element1,element2=atom1['element'],atom2['element'] 
		distance=euclidean_distance(atom1['coord'],atom2['coord']) 
		if (element1,element2) in bond_thresholds and distance<=bond_thresholds[(element1,element2)]: 
			bonds.append((i,j))
	
	return atoms,bonds






















































































