# pdb_visualizer
A 3D renderer/visualizer of .pdb files. 
## Features 
-Native file selection 

-3D representation of all ATOM/HETATM's as well as inferred bonds between points based on euclidean distance 

-Zooming, panning, and rotating features (similar to matplotlib) 
## Installation 
```bash
git clone https://github.com/joshjthompson/pdb_visualizer.git
cd pdb_visualizer
pip install -r requirements.txt
```
## Usage 
-Run main within the repo directory (python main.py) 

-You must use the file selector to load your desired .pdb file. It must be .pdb 

-Once the file is selected, the 3D rendering will load in. If it is a large macromolecule (>10000 ATOM), it will take a few seconds to load in and might run slower. 

-Rotating the plot can be done by clicking and dragging across the molecule itself 

-In the toolbar, you can find several functions such as zooming, panning, and returning to the original view. You have to manually deselect the zooming/panning options when you are finished using them in order to rotate the plot again. 

-To load a different file, navigate and choose it like you did with the first file. All previous plots are not saved unless you've saved an image using the function in the toolbar. 
## Dependencies 
-Tkinter

-Matplotlib

-SciPy 

-NumPy

-Biopython

All dependencies can be installed using the requirement.txt file (see installation commands above) 
## Examples/Images 
