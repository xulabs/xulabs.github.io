---
permalink: /chemotaxis/tutorial_tumbling_frequencies
title: "Software Tutorial: Comparing different chemotaxis default tumbling frequencies"
sidebar:
 nav: "chemotaxis"
toc: true
toc_sticky: true
---

In this tutorial, we will run a comparison of the chemotactic random walk over a variety of different background tumbling frequencies. Are some frequencies better than others at helping the bacterium reach the goal?

## Qualitative comparison of different background tumbling frequencies

First, we will use <a href="../downloads/downloadable/chemotaxis_walk.ipynb" download="chemotaxis_walk.ipynb">chemotaxis_walk.ipynb</a> from our [modified random walk tutorial](tutorial_walk) to compare the trajectories of a few cells for different tumbling frequencies.

Specifically, we will run our simulation for three cells over a time period of 800 seconds. We simulate each cell multiple times using a variety of different tumbling frequencies. (We use average tumbling frequencies of 0.1, 0.2, 0.5, 1.0, 2.0, 5.0, and 10.0 seconds.) This will give us a rough idea of what the trajectories look like.

~~~ python
duration = 800   #seconds, duration of the simulation
num_cells = 3
origin_to_center = euclidean_distance(start, ligand_center) #Update the global constant
run_time_expected_all = [0.5, 1.0, 5.0]
paths = np.zeros((len(run_time_expected_all), num_cells, duration + 1, 2))

for i in range(len(run_time_expected_all)):
    run_time_expected = run_time_expected_all[i]
    paths[i] = simulate_chemotaxis(num_cells, duration, run_time_expected)
~~~

As we did previously, we then plot the trajectories.

~~~ python

conc_matrix = np.zeros((3500, 3500))
for i in range(3500):
    for j in range(3500):
        conc_matrix[i][j] = math.log(calc_concentration([i - 500, j - 500]))

mycolor = [[256, 256, 256], [256, 255, 254], [256, 253, 250], [256, 250, 240], [255, 236, 209], [255, 218, 185], [251, 196, 171], [248, 173, 157], [244, 151, 142], [240, 128, 128]] #from coolors：）
for i in mycolor:
    for j in range(len(i)):
        i[j] *= (1/256)
cmap_color = colors.LinearSegmentedColormap.from_list('my_list', mycolor)


for freq_i in range(len(run_time_expected_all)):
    fig, ax = plt.subplots(1, figsize = (8, 8))
    ax.imshow(conc_matrix.T, cmap=cmap_color, interpolation='nearest', extent = [-500, 3000, -500, 3000], origin = 'lower')

    #Plot simulation results
    time_frac = 1.0 / duration
    #Time progress: dark -> colorful
    for t in range(duration):
        ax.plot(paths[freq_i,0,t,0], paths[freq_i,0,t,1], 'o', markersize = 1, color = (0.2 * time_frac * t, 0.85 * time_frac * t, 0.8 * time_frac * t))
        ax.plot(paths[freq_i,1,t,0], paths[freq_i,1,t,1], 'o', markersize = 1, color = (0.85 * time_frac * t, 0.2 * time_frac * t, 0.9 * time_frac * t))
        ax.plot(paths[freq_i,2,t,0], paths[freq_i,2,t,1], 'o', markersize = 1, color = (0.4 * time_frac * t, 0.85 * time_frac * t, 0.1 * time_frac * t))
    ax.plot(start[0], start[1], 'ko', markersize = 8)
    ax.plot(1500, 1500, 'bX', markersize = 8)
    for i in range(num_cells):
        ax.plot(paths[freq_i,i,-1,0], paths[freq_i,i,-1,1], 'ro', markersize = 8)

    ax.set_title("Background tumbling freq:\n tumble every {} s".format(run_time_expected_all[freq_i]), x = 0.5, y = 0.9, fontsize = 12)
    ax.set_xlim(-500, 3000)
    ax.set_ylim(-500, 3000)
    ax.set_xlabel("poisiton in μm")
    ax.set_ylabel("poisiton in μm")

plt.show()
~~~

**STOP:** Run the code blocks for simulating the random walks and plotting the outcome. Are the cells moving up the gradient? How do the shapes of the trajectories differ for different tumbling frequencies? What value of the average tumbling frequency do you think is best?
{: .notice--primary}

## Comparing tumbling frequencies over many cells

We will now scale up our simulation to `num_cells` = 500 cells. To rigorously compare the results of the simulation for different default tumbling frequencies,  we will calculate the average distance to the center at each time step for each tumbling frequency that we use.

~~~ python
#Run simulation for 500 cells with different background tumbling frequencies, Plot average distance to highest concentration point
duration = 1500   #seconds, duration of the simulation
#num_cells = 500
num_cells = 300
run_time_expected_all = [0.1, 0.2, 0.5, 1.0, 2.0, 5.0, 10.0]
origin_to_center = euclidean_distance(start, ligand_center) #Update the global constant

all_distance = np.zeros((len(time_exp), num_cells, duration)) #Initialize to store results

paths = np.zeros((len(run_time_expected_all), num_cells, duration + 1, 2))

for i in range(len(run_time_expected_all)):
    run_time_expected = run_time_expected_all[i]
    paths[i] = simulate_chemotaxis(num_cells, duration, run_time_expected)

for freq_i in range(len(run_time_expected_all)):
    for c in range(num_cells):
        for t in range(duration):
            pos = paths[freq_i, c, t]
            dist = euclidean_distance(ligand_center, pos)
            all_distance[freq_i, c, t] = dist

all_dist_avg = np.mean(all_distance, axis = 1)
all_dist_std = np.std(all_distance, axis = 1)
print(all_dist_avg[0][-10:])
~~~

We then plot the average distance to the goal over time for each frequency, where each tumbling frequency is assigned a different color.

~~~ python
#Below are all for plotting purposes
#Define the colors to use
colors1 = colorspace.qualitative_hcl(h=[0, 300.], c = 60, l = 70, pallete = "dynamic")(len(time_exp))

xs = np.arange(0, duration)

fig, ax = plt.subplots(1, figsize = (10, 8))

for freq_i in range(len(time_exp)):
    mu, sig = all_dist_avg[freq_i], all_dist_std[freq_i]
    ax.plot(xs, mu, lw=2, label="tumble every {} second".format(run_time_expected_all[freq_i]), color=colors1[freq_i])
    ax.fill_between(xs, mu + sig, mu - sig, color = colors1[freq_i], alpha=0.1)

ax.set_title("Average distance to highest concentration")
ax.set_xlabel('time (s)')
ax.set_ylabel('distance to center (µm)')
ax.legend(loc='lower left', ncol = 1)

ax.grid()
~~~

**STOP:** Run the code blocks we have provided, simulating the random walks and plotting the average distance to the goal over time for each tumbling frequency. Is there any difference in the performance of the search algorithm for different tumbling frequencies? For each frequency, how long does it take the cell to "reach" the goal? And can we conclude that one tumbling frequency is better than the others?
{: .notice--primary}

As we return to the main text, we interpret the results of this final tutorial. It turns out that there are significant differences in our chemotaxis algorithm's ability to find (and remain at) the goal for differing default tumbling frequencies. It hopefully will not surprise you to learn that the frequency that evolution has bestowed upon *E. coli* turns out to be optimal.

[Return to main text](home_conclusion#why-is-bacterial-background-tumbling-frequency-constant-across-species){: .btn .btn--primary .btn--large}
{: style="font-size: 100%; text-align: center;"}
