#Program Entry Point and Tkinter GUI logic
import tkinter as tk 
from tkinter import ttk 
from tkinter import filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from pdb_parser import parse_pdb 
from plotter import plot_molecule

def open_file(): 
	global toolbar
	file_path=filedialog.askopenfilename(filetypes=[('PDB Files', '*.pdb')])
	atoms,bonds=parse_pdb(file_path)
	print(file_path)
	print(atoms,bonds)
	canvas=FigureCanvasTkAgg(plot_molecule(atoms,bonds),master=frame)
	canvas.draw()
	canvas.get_tk_widget().grid(column=0,row=0,sticky='nsew')
	toolbar.destroy()
	toolbar=NavigationToolbar2Tk(canvas,toolbar_frame,pack_toolbar=False)
	toolbar.grid(column=0,row=0)
	toolbar.update()

if __name__=='__main__': 
	atoms,bonds=[],[]
	
	root=tk.Tk()
	root.title('PDB File Visualizer') 
	
	root.columnconfigure(0,weight=1)
	root.rowconfigure(0,weight=1) 
	root.rowconfigure(1,weight=1)
	root.rowconfigure(2,weight=1)
	
	file_frame=tk.Frame(root)
	file_frame.grid(column=0,row=0,sticky='ew')
	
	file_btn=ttk.Button(root,text='Open PDB File', command=open_file)
	file_btn.grid(column=0,row=0,sticky='ew')
	
	frame=tk.Frame(root)
	frame.grid(column=0,row=1,sticky='nsew')
	
	canvas=FigureCanvasTkAgg(plot_molecule(atoms,bonds),master=frame)
	canvas.draw()
	canvas.get_tk_widget().grid(column=0,row=0,sticky='nsew')
	
	toolbar_frame=tk.Frame(root)
	toolbar_frame.grid(column=0,row=2,sticky='nsew')
	
	toolbar=NavigationToolbar2Tk(canvas,toolbar_frame,pack_toolbar=False) 
	toolbar.update()
	
	root.mainloop()







































































