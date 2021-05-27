---
permalink: /chemotaxis/tutorial_walk
title: "Chemotactic random walk"
sidebar:
 nav: "chemotaxis"
toc: true
toc_sticky: true
---

In this page, we will:
 - Simulate *E. coli* chemotaxis at a cellular level
 - Compare performance of chemotactic walk vs. standard random walk
 - Compare performances of different default tumbling frequencies.

## Simulation files and dependencies

Please download the simulation and visualization here: <a href="../downloads/downloadable/chemotaxis_compare.ipynb" download="chemotaxis_compare.ipynb">chemotaxis_compare.ipynb</a>. Detailed explanation of the model and each functions can be found in the file too.

Please make sure the following dependencies are installed:

| Installation Link | Version | Check install/version |
|:------|:-----:|------:|
| [Python3](https://www.python.org/downloads/)  |3.6+ |`python --version` |
| [Jupyter Notebook](https://jupyter.org/index.html) | 4.4.0+ | `jupyter --version` |
| [Numpy](https://numpy.org/install/) | 1.14.5+ | `pip list | grep numpy` |
| [Matplotlib](https://matplotlib.org/users/installing.html) | 3.0+ | `pip list | grep matplotlib` |
| [Colorspace](https://python-colorspace.readthedocs.io/en/latest/installation.html) or with [pip](https://pypi.org/project/colorspace/)| any | `pip list | grep colorspace`|

## Modeling chemotactic walk at a cellular level

Our model will be based on observations from BNG simulation and *E. coli* biology.

Ingredients and simplifying assumptions of the model:
 - Run. The background average duration of each run (`time_exp`) is a variable of interest. When the cell senses concentration change, the cell changes the expected run duration (`exp_run_time`). The duration of each run follows an exponential distribution with mean = `exp_run_time`.
 - Tumble. The duration of cell tumble follows an exponential distribution with mean 0.1s[^Saragosti2012]. When it tumbles, we assume it only changes the orientation for the next run but doesn't move in space. The degree of reorientation follows uniform distribution from 0° to 360°.
 - Response. As we've seen in the BNG model, the cell can respond to the gradient change within 0.5 seconds. In this model, we allow cells to re-measure the concentration after it runs for 0.5 seconds.
 - Gradient. We model an exponential gradient centered at [1500, 1500] with a concentration of 10<sup>10</sup>. All cells start at [0, 0], which has a concentration of 10<sup>2</sup>. The receptors saturate at a concentration of 10<sup>10</sup>.
 - Performance. The closer to the center of the gradient the better.

What's different between this more advanced model and the [earlier model](tutorial_purerandom) using a standard random walk strategy is we decide the run duration before tumbling based on current vs. past concentrations.

We will start from our previous model and only modify on including this ability.

## Updating run time before tumbling based on concentrations

In our standard random walk model, we sampled each run duration from an exponential distribution with mean `run_time_expected`. This time, we will include the concentrations into our sampling.

The updated run durations adjusted with concentration changes follow an exponential distribution with mean of `run_time_expected_adj_conc`. When no gradient is present, `run_time_expected_adj_conc` = `run_time_expected`. When there is a change in ligand concentration, `run_time_expected_adj_conc` changes accordingly. The change is calculated as `(curr_conc - past_conc) / past_conc` to normalize for the exponential gradient. We model this response with `run_time_expected_adj_conc` = `run_time_expected` + 10 * `change`.

~~~ python
# Calculate the wait time for next tumbling event
# Input: current concentration (float), past concentration (float), position (array [x, y]), expected run time (float)
# Return: duration of current run (float)
def run_duration(curr_conc, past_conc, position, run_time_expected):

    curr_conc = min(curr_conc, saturation_conc) #Can't detect higher concentration if receptors saturates
    past_conc = min(past_conc, saturation_conc)
    change = (curr_conc - past_conc) / past_conc #proportion change in concentration, float
    run_time_expected_adj_conc = run_time_expected * (1 + 10 * change) #adjust based on concentration change, float

    if run_time_expected_adj_conc < 0.000001:
        run_time_expected_adj_conc = 0.000001 #positive wait times
    elif run_time_expected_adj_conc > 4 * run_time_expected:
        run_time_expected_adj_conc = 4 * run_time_expected     #the decrease to tumbling frequency is only to a certain extent
    #Sample the duration of current run from exponential distribution, mean=run_time_expected_adj_conc
    curr_run_time = np.random.exponential(run_time_expected_adj_conc)

    return curr_run_time
~~~

For each cell, simulate through time as the following procedure:

while `t` < duration:
 - Assess the current concentration
 - Update current run duration `curr_run_time`
 - If `curr_run_time` < 0.5s:
        1. run for `curr_run_time` second along current direction
        2. Sample the duration of tumble `tumble_time` and the resulted direction
        3. increment t by `curr_run_time` and `tumble_time`
 - If `curr_run_time` > 0.5s:
        1. run for 0.5s along current direction
        2. increment `t` by 0.5s (and then the cell will re-assess the new concentration, and decide the duration of next run)

We need to modify our code in the following way:
 - Add concentration calculation before each run.
 - Replace our sampler for run duration with calling the `run_duration` function
 - Check the conditions with the sampled duration; only tumble after run if `curr_run_time` < 0.5s

~~~ python
# This function performs simulation
# Input: number of cells to simulate (int), how many seconds (int), the expected run time before tumble (float)
# Return: the simulated trajectories paths: array of shape (num_cells, duration+1, 2)
def simulate_chemotaxis(num_cells, duration, run_time_expected):

    #Takes the shape (num_cells, duration+1, 2)
    #any point [x,y] on the simulated trajectories can be accessed via paths[cell, time]
    paths = np.zeros((num_cells, duration + 1, 2))

    for rep in range(num_cells):
        # Initialize simulation
        t = 0 #record the time elapse
        curr_position = np.array(start) #start at [0, 0]
        past_conc = calc_concentration(start) #Initialize concentration
        projection_h, projection_v, tumble_time = tumble_move() #Initialize direction randomly

        while t < duration:
            curr_conc = calc_concentration(curr_position)

            curr_run_time = run_duration(curr_conc, past_conc, curr_position, run_time_expected) #get run duration, float

            # if run time (r) is within the step (s), run for r second and then tumble
            if curr_run_time < response_time:
                #displacement on either direction is calculated as the projection * speed * time
                #update current position by summing old position and displacement
                curr_position = curr_position + np.array([projection_h, projection_v]) * speed * curr_run_time
                projection_h, projection_v, tumble_time = tumble_move() #tumble
                t += (curr_run_time + tumble_time) #increment time

            # if r > s, run for r; then it will be in the next iteration
            else:
                #displacement on either direction is calculated as the projection * speed * time
                #update current position by summing old position and displacement
                curr_position = curr_position + np.array([projection_h, projection_v]) * speed * response_time
                t += response_time #no tumble here

            #record position approximate for integer number of second
            curr_sec = int(t)
            if curr_sec <= duration:
                #fill values from last time point to current time point
                paths[rep, curr_sec] = curr_position.copy()
                past_conc = curr_conc

    return paths
~~~

## Compare performance of the two strategies

Please download the simulation and visualization here: <a href="../downloads/downloadable/chemotaxis_compare.ipynb" download="chemotaxis_compare.ipynb">chemotaxis_compre.ipynb</a>.

To compare the performance of the two strategies, we visualize the trajectories of simulation with 3 cells and compare the performance using simulation with 500 cells for each strategy.

**Qualitative comparison**. Run the code for Part2: Visualizing trajectories. The background color indicates concentration: white -> red = low -> high; black dot are starting points; red dots are the points they reached at the end of the simulation; colored points represents trajectories (one color one cell): dark -> bright color = older -> newer time points; blue cross indicates the goal.

We will simulate 3 cells for 800 seconds for each of the strategies.

~~~ python
#Run simulation for 3 cells for each strategy, plot paths
duration = 800   #seconds, duration of the simulation
num_cells = 3
origin_to_center = euclidean_distance(start, ligand_center) #Update the global constant
run_time_expected = 1.0

paths_rand = simulate_std_random(num_cells, duration, run_time_expected)
paths_che = simulate_chemotaxis(num_cells, duration, run_time_expected)
paths = np.array([paths_rand, paths_che])
~~~

The plotting is similar as before, except that this time, we will have two subplots, one for pure random walk and another for chemotactic random walk, initialized with `plt.subplots(1, 2)`. We will plot the simulation results for each strategy.

~~~ python
#Below are all for plotting purposes
methods = ["Pure random walk", "Chemotactic random walk"]
fig, ax = plt.subplots(1, 2, figsize = (16, 8)) #1*2 subplots, size 16*8

#First set color map
mycolor = [[256, 256, 256], [256, 255, 254], [256, 253, 250], [256, 250, 240], [255, 236, 209], [255, 218, 185], [251, 196, 171], [248, 173, 157], [244, 151, 142], [240, 128, 128]] #from coolors：）
for i in mycolor:
    for j in range(len(i)):
        i[j] *= (1/256)
cmap_color = colors.LinearSegmentedColormap.from_list('my_list', mycolor) #Linearly segment these colors to create a continuous color map

#Store the concentrations for each integer position in a matrix
conc_matrix = np.zeros((4000, 4000)) #we will display from [-1000, -1000] to [3000, 3000]
for i in range(4000):
    for j in range(4000):
        conc_matrix[i][j] = math.log(calc_concentration([i - 1000, j - 1000]))

#Repeat for the two strategies
for m in range(2):
    #Simulate the gradient distribution, plot as a heatmap
    ax[m].imshow(conc_matrix.T, cmap=cmap_color, interpolation='nearest', extent = [-1000, 3000, -1000, 3000], origin = 'lower')

    #Plot simulation results
    time_frac = 1.0 / duration
    #Plot the trajectories. Time progress: dark -> colorful
    for t in range(duration):
        ax[m].plot(paths[m,0,t,0], paths[m,0,t,1], 'o', markersize = 1, color = (0.2 * time_frac * t, 0.85 * time_frac * t, 0.8 * time_frac * t))
        ax[m].plot(paths[m,1,t,0], paths[m,1,t,1], 'o', markersize = 1, color = (0.85 * time_frac * t, 0.2 * time_frac * t, 0.9 * time_frac * t))
        ax[m].plot(paths[m,2,t,0], paths[m,2,t,1], 'o', markersize = 1, color = (0.4 * time_frac * t, 0.85 * time_frac * t, 0.1 * time_frac * t))
    ax[m].plot(start[0], start[1], 'ko', markersize = 8) #Mark the starting point [0, 0]
    for i in range(num_cells):
        ax[m].plot(paths[m,i,-1,0], paths[m,i,-1,1], 'ro', markersize = 8) #Mark the terminal points for each cell
    ax[m].plot(1500, 1500, 'bX', markersize = 8) #Mark the highest concentration point [1500, 1500]

    ax[m].set_title("{}\n Average tumble every 1 s".format(methods[m]), x = 0.5, y = 0.87)
    ax[m].set_xlim(-1000, 3000)
    ax[m].set_ylim(-1000, 3000)
    ax[m].set_xlabel("poisiton in μm")
    ax[m].set_ylabel("poisiton in μm")

fig.tight_layout()

plt.show()
~~~

Which strategy allows the cell to travel towards the higher concentration?

Are we ready to conclude which default tumbling frequencies are the best?

**Quantitative comparsion**. Because of the high variations due to randomness, trajectories for 3 cells is not convincing enough. To verify your hypothesis on which strategy is better, let's simulate 500 cells for 1500 seconds for each strategy. Run the two code for Part3: Comparing performances. Each colored line indicates a strategy, plotting average distances for the 500 cells; the shaded area is standard deviation; the grey dashed line is where concentration reaches 1e8.

Like we did above, we run simulations for each strategies.

~~~ python
#Run simulation for 3 cells with different background tumbling frequencies, Plot paths

duration = 1500   #seconds, duration of the simulation
num_cells = 500
origin_to_center = euclidean_distance(start, ligand_center) #Update the global constant
run_time_expected = 1.0

paths_rand = simulate_std_random(num_cells, duration, run_time_expected)
paths_che = simulate_chemotaxis(num_cells, duration, run_time_expected)
paths = np.array([paths_rand, paths_che])

all_distance = np.zeros((2, num_cells, duration)) #Initialize to store results: methods, number, duration

for m in range(2): #two methods
    for c in range(num_cells): #each cell
        for t in range(duration): #every time point
            pos = paths[m, c, t]
            dist = euclidean_distance(ligand_center, pos)
            all_distance[m, c, t] = dist

all_dist_avg = np.mean(all_distance, axis = 1) #Calculate average over cells, array of shape (2,duration,)
all_dist_std = np.std(all_distance, axis = 1) #Calculate the standard deviation, array of shape (2,duration,)
~~~

And then plotting the average distance to center vs. time like in the [previous tutorial](tutorial_purerandom).
~~~ python
#Below are all for plotting purposes
#Define the colors to use
colors1 = colorspace.qualitative_hcl(h=[0, 200.], c = 60, l = 70, pallete = "dynamic")(2)

xs = np.arange(0, duration) #Set the x-axis for plot: time points. Array of integers of shape (duration,)

fig, ax = plt.subplots(1, figsize = (10, 8)) #Initialize the plot with 1*1 subplot of size 10*8

for m in range(2):
    #Get the result for this strategy
    mu, sig = all_dist_avg[m], all_dist_std[m]
    #Plot average distance vs. time
    ax.plot(xs, mu, lw=2, label="{}".format(methods[m]), color=colors1[m])
    #Fill in average +/- one standard deviation vs. time
    ax.fill_between(xs, mu + sig, mu - sig, color = colors1[m], alpha=0.15)

ax.set_title("Average distance to highest concentration")
ax.set_xlabel('time (s)')
ax.set_ylabel('distance to center (µm)')
ax.hlines(0, 0, duration, colors='gray', linestyles='dashed', label='concentration 10^8')
ax.legend(loc='upper right', ncol = 2, fontsize = 15)

ax.grid()
~~~

Which strategy is more efficient?

[Return to main text](home_conclusion#comparing-the-effectiveness-of-our-two-random-walk-strategies){: .btn .btn--primary .btn--large}
{: style="font-size: 100%; text-align: center;"}



[^Saragosti2012]: Saragosti J., Siberzan P., Buguin A. 2012. Modeling *E. coli* tumbles by rotational diffusion. Implications for chemotaxis. PLoS One 7(4):e35412. [available online](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3329434/).

[^Berg1972]: Berg HC, Brown DA. 1972. Chemotaxis in Escherichia coli analysed by three-dimensional tracking. Nature. [Available online](https://www.nature.com/articles/239500a0)

[^Baker2005]: Baker MD, Wolanin PM, Stock JB. 2005. Signal transduction in bacterial chemotaxis. BioEssays 28:9-22. [Available online](https://pubmed.ncbi.nlm.nih.gov/16369945/)
