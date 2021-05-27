import numpy as np
import sys
import os
import matplotlib.pyplot as plt
import colorspace

model_path = sys.argv[1] #name of the .bngl model
model_name = sys.argv[2]
target = sys.argv[3]     #The name of the molecule to plot
vals = sys.argv[4:]      #Rates, also name of the folders

#Define the colors to use
colors = colorspace.qualitative_hcl(h=[0, 300.], c = 60, l = 70, pallete = "dynamic")(len(vals))


def load_data(val):
	file_path = os.path.join(model_path, val, model_name + ".gdat")
	with open(file_path) as f:
		first_line = f.readline() #Read the first line
	cols = first_line.split()[1:] #Get the col names (species names)

	ind = 0
	while cols[ind] != target:
		ind += 1                  #Get col number of target molecule

	data = np.loadtxt(file_path)  #Load the file
	time = data[:, 0]             #Time points
	concentration = data[:, ind]  #Concentrations

	return time, concentration


def plot(val, time, concentration, ax, i):
	legend = "rate: " + str(val)
	ax.plot(time, concentration, label = legend, color = colors[i])
	ax.legend()

	return


def main():
	fig, ax = plt.subplots(1, 1)
	for i in range(len(vals)):
		val = vals[i]
		time, concentration = load_data(val)
		plot(val, time, concentration, ax, i)

	plt.xlabel("time")
	plt.ylabel("concentration (#molecules)")
	plt.title("Active CheY vs time")
	ax.minorticks_on()
	ax.grid(b = True, which = 'minor', axis = 'both', color = 'lightgrey', linewidth = 0.5, linestyle = ':')
	ax.grid(b = True, which = 'major', axis = 'both', color = 'grey', linewidth = 0.8 , linestyle = ':')

	plt.show()



if __name__=='__main__':
	main()
