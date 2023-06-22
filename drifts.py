from glob import glob
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

def get_paths(identifier="*.csv"):
	filenames = glob(identifier)
	paths = [None for i in range(len(filenames))] # initialization of paths list

	for i in range(len(filenames)):
  		split_names = filenames[i][:-4].split('_')
  
  		paths[i] = [filenames[i], # 0: path
  					'{}_{}_{}_{}'.format(split_names[0], split_names[1], 
  										 split_names[2], split_names[3]), # 1: title
		            float(split_names[4]), # 2: max_intensity
		            float(split_names[5]), # 3: fig_ratio
                    float(split_names[6]), # 4: font_size
                    float(split_names[7])] # 5: dpi
	return paths

if __name__ == "__main__":
	print("======Shin, Dongjae, POSTECH, shindj91@postech.ac.kr======")

	# Detecting csv files
	paths = get_paths()
	print("reading csv files ...")
	print("following csv files were detected:")
	for i in range(len(paths)): print(i+1,": ", paths[i][0])

	# Iterate for the whole csv files
	for iter, path in enumerate(paths):
		plt.rcParams["mathtext.default"] = "regular" # non-italic math fonts
		plt.rcParams["font.family"] = "sans-serif"
		plt.rcParams["font.size"] = path[4] # 22
		plt.rcParams['xtick.major.pad']='8'
		plt.rcParams['ytick.major.pad']='8'

	  	# Reading each csv file
		data_set = read_csv(path[0], header=1)
		data_set = data_set.dropna(axis=0) # drop the rows with NaN

		# Extracting x, y axes
		wavenumber = np.array(list(data_set.loc[:, 'cm-1']))
		time = np.array(list([float(i) for i in data_set.columns[1:]]))

		# Making array with absorbance values
		Absorbance = np.zeros((len(wavenumber),len(time)))
		for i in tqdm(range(len(wavenumber))):
			for j in range(len(time)):
				Absorbance[i][j] = get_absorbance(wavenumber[i], time[j])

	    # Construct meshgrid for contourf
		time, wavenumber = np.meshgrid(time, wavenumber)

		borderwidth = 1.25
		linewidth = 1.25

		# Set overall size of figure
		print("drawing figure ... ({:d}/{:d})".format(iter+1,len(paths)))
		fig = plt.figure(figsize=(10.5*path[3],10.5))
		ax = fig.add_subplot(111)
		ax.set_xlim(left=wavenumber.max(), right=wavenumber.min())
		# ax.set_ylim(bottom=20.0, top=90.0)

		levels = np.linspace(0.0, path[2], 45) # instead of vmin, vmax
		# levels = 35
		plane2 = ax.contourf(wavenumber, time, Absorbance,
			                 cmap="inferno", alpha=1.0, levels=levels,
			                 antialiased=False,
			                 extend='both') # extend: {'neither', 'both', 'min', 'max'}

		ax.set_ylabel('Time $(min)$')
		ax.set_xlabel('Wavenumber $(cm^{-1})$')
		plt.xticks()
		plt.yticks()

		for axis in ['top','bottom','left','right']:
			ax.spines[axis].set_linewidth(borderwidth)

		# Colorbar
		cbar = fig.colorbar(plane2, orientation='horizontal',
	                      	pad=0.10)
		                    # ticks=np.linspace(0.5,4.5,5),

		majorFormatter = FormatStrFormatter('%.2f')
		cbar.ax.xaxis.set_major_formatter(majorFormatter)

		cbar.outline.set_linewidth(borderwidth)
		cbar.set_label('Absorbance (a.u.)', labelpad=5)
		cbar.ax.tick_params(width=borderwidth, labelsize=path[4])

		fig.tight_layout()
		plt.title(path[1], pad=12)
		plt.savefig(fname='./output_{}.png'.format(path[1]), dpi=path[5])
		print("png file written!")
	print("end of code.")