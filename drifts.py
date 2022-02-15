from pandas import read_csv, DataFrame
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import FormatStrFormatter
from tqdm import tqdm, trange # for progress bar

def get_absorbance(wavenumber, temperature):
	absorbance = data_set[lambda data_set: np.abs(data_set['cm-1'] - wavenumber) < 1e-3][str(int(temperature))]
	absorbance = float(absorbance)
	return absorbance

if __name__ == "__main__":
	print("======Shin, Dongjae, POSTECH, shindj91@postech.ac.kr======")
	path = './drifts_data.csv'

	print("reading csv file ...")
	data_set = read_csv(path, header=1)  
	print("reading csv file loaded!")
	
	wavenumber = np.array(list(data_set.loc[:, 'cm-1']))
	temperature = np.array(list([float(i) for i in data_set.columns[1:]]))
	
	Absorbance = np.zeros((len(wavenumber),len(temperature)))
	print("making absorbance array ...")
	for i in tqdm(range(len(wavenumber))):
		for j in range(len(temperature)):
			Absorbance[i][j] = get_absorbance(wavenumber[i], temperature[j])
	print("absorbance array made!")
	
	# Absorbance = get_absorbance(wavenumber, temperature)
	temperature, wavenumber = np.meshgrid(temperature, wavenumber)
	
	plt.rcParams["mathtext.default"] = "regular" # non-italic math fonts
	plt.rcParams["font.family"] = "sans-serif"
	plt.rcParams["font.size"] = 22
	
	# plt.rcParams["font.family"] = "sans-serif"
	borderwidth = 1.25
	linewidth = 1.25
	
	print("drawing figure ...")
	# Set overall size of figure
	fig = plt.figure(figsize=(10.6,10.5))
	# ax = fig.gca(projection='3d')
	ax = fig.add_subplot(111)
	#ax.set_xlim(left=-50.0, right=100.0)
	#ax.set_ylim(bottom=-75.0, top=25.0)
	
	plane2 = ax.contourf(wavenumber, temperature, Absorbance, 
	                   cmap="magma", alpha=1.0, levels=100,
	                   antialiased=False,)
	
	ax.set_ylabel('Temperature $(^oC)$')
	ax.set_xlabel('Wavenumber $(cm^{-1})$')
	plt.xticks()
	plt.yticks()
	
	for axis in ['top','bottom','left','right']:
		ax.spines[axis].set_linewidth(borderwidth)
	
	# Colorbar
	cbar = fig.colorbar(plane2, orientation='horizontal',
	                    pad=0.10)
	                    # ticks=np.linspace(0.5,4.5,5),
	
	majorFormatter = FormatStrFormatter('%4.3f')
	cbar.ax.xaxis.set_major_formatter(majorFormatter)

	cbar.outline.set_linewidth(borderwidth)
	cbar.set_label('Absorbance (a.u.)', labelpad=5)
	cbar.ax.tick_params(width=borderwidth, labelsize=20)
	fig.tight_layout()

	print("writing png file ...")
	plt.savefig(fname='./output.png', dpi=300)
	print("png file written!")
	print("showing the result ...")
	plt.show()
	print("end of code.")