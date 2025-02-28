#Handles 3D plotting/visualization. Uses Axes3D from Matplotlib (mpl_toolkits.mplot3d) 
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D 

def plot_molecule(atoms,bonds): 
	fig=plt.figure(figsize=(5,3))
	ax=fig.add_subplot(111,projection='3d')

	ax.set_xlabel('X') 
	ax.set_ylabel('Y') 
	ax.set_zlabel('Z') 
	
	for atom in atoms[::int(len(atoms)/250)+1]: 
		x,y,z=atom['coord'] 
		element=atom['element']
		ax.scatter(x,y,z,color=get_color(element),s=5,alpha=.4)
	
	for bond in bonds: 
		atom1,atom2=bond
		xs=[atoms[atom1]['coord'][0],atoms[atom2]['coord'][0]]
		ys=[atoms[atom1]['coord'][1],atoms[atom2]['coord'][1]]
		zs=[atoms[atom1]['coord'][2],atoms[atom2]['coord'][2]]
		ax.plot(xs,ys,zs,color='black',alpha=.6,lw=.5)
	
	ax.set_axis_off()
	ax.grid(False)
	ax.set_position([0,0,1,1])
	fig.patch.set_facecolor('dimgrey')
		
	return fig

def get_color(element): 
	colors={
		'C':'gray', 
		'H':'white', 
		'O':'red', 
		'N':'blue', 
		'S':'yellow', 
		'P':'orange'
	}
	return colors.get(element,'purple')













































































