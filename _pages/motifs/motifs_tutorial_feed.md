---
permalink: /motifs/tutorial_feed
title: "Software Tutorial: Implementing the Feed-Forward Loop Motif"
sidebar:
 nav: "motifs"
toc: true
toc_sticky: true
---

In this tutorial, we will use CellBlender to run a (mathematically controlled) comparison of simple regulation against regulation via the type-1 incoherent feed-forward loop that we saw in the main text.

Load your `CellBlender_Tutorial_Template.blend` file from the [Random Walk Tutorial](.../prologue/tutorial-random-walk). Save your file as `ffl.blend`. You may also download the completed tutorial file <a href=".../tutorials/incoher_ffl.blend" download="incoher_ffl.blend">here</a>.

Go to `CellBlender > Molecules` and create the following molecules:

![image-center](../assets/images/motifs_norm1.png){: .align-center}

1. Click on the `+` button.
2. Select a color (such as white).
3. Name the molecule `X1`.
4. Select the molecule type as `Surface Molecule`.
5. Add a diffusion constant of `1e-6`.
6. Up the scale factor to `5` (click and type “5” or use the arrows).

Repeat the above steps to make sure that the following molecules are entered with the appropriate parameters.

| Molecule Name | Molecule Type|Diffusion Constant| Scale Factor|
|:--------|:-------:|--------:|--------:|--------:|
| X1  | Surface  | 1e-6  | 5|
| Z1  | Surface  | 1e-6  | 1|
| X2  | Surface  | 1e-6  | 5|
| Y2  | Surface  | 1e-6  | 1|
| Z2  | Surface  | 1e-6  | 1|

Now go to `CellBlender > Molecule Placement` to set the following release sites for our molecules:

![image-center](../assets/images/motifs_norm3.png){: .align-center}

1. Click on the `+` button.
2. Select or type in the molecule `X1`.
3. Type in the name of the Object/Region `Plane`.
4. Set the Quantity to Release as `300`.

Repeat the above steps to make sure all of the following molecule release sites are entered.

| Molecule Name | Object/Region|Quantity to Release|
|:--------|:-------:|--------:|
| X1  | Plane | 300 |
| X2  | Plane | 300 |

Next go to `CellBlender > Reactions` to create the following reactions:

![image-center](../assets/images/motifs_norm4.png){: .align-center}

1. Click on the `+` button.
2. Under reactants, type `X1’` (note the apostrophe).
3. Under products, type `X1’ + Z1’`.
4. Set the forward rate as `4e2`.

Repeat the above steps for the following reactions.

| Reactants |Products|Forward Rate|
|:--------|:-------:|--------:|
| X1’  | X1’ + Z1’ | 4e2 |
| Z1’  | NULL | 4e2 |
| X2’  | X2’ + Y2’ | 2e2 |
| X2’  | X2’ + Z2’ | 4e3 |
|Y2’ + Z2’| Y2’|4e2|
| Y2’  | NULL | 4e2 |
| Z2’  | NULL | 4e2 |

Go to `CellBlender > Plot Output Settings` to set up a plot as follows:

![image-center](../assets/images/motifs_norm6.png){: .align-center}

1. Click on the `+` button.
2. Set the molecule name as `Z1`.
3. Ensure `World` is selected.
4. Ensure `Java Plotter` is selected.
5. Ensure `One Page, Multiple Plots` is selected.
6. Ensure `Molecule Colors` is selected.

Repeat the above steps to ensure that we plot all of the following molecules.

| Molecule Name|Selected Region|
|:--------|:-------:|
| Z1| World|
| Z2| World|

We are now ready to run our simulation. Go to `CellBlender > Run Simulation` and select the following options:

![image-center](../assets/images/motifs_norm7.png){: .align-center}

1. Set the number of iterations to `12000`.
2. Ensure the time step is set as `1e-6`.
3. Click `Export & Run`.

Once the simulation has run, we can visualize our data with `CellBlender > Reload Visualization Data`.

![image-center](../assets/images/motifs_norm8.png){: .align-center}

If you like, you can watch the animation within the Blender window by clicking the play button at the bottom of the screen.

Now go back to `CellBlender > Plot Output Settings` and scroll to the bottom to click “Plot”. This will produce a plot of the amount of *Z* under simple regulation compared to the amount of *Z* for the feed-forward loop. Is it what you expected?

![image-center](../assets/images/motifs_norm9.png){: .align-center}

Save your file, and then use the link below to return to the main text, where we will interpret the outcome of our simulation.

[Return to main text](feed#why-feedforward-loops-speed-up-response-times){: .btn .btn--primary .btn--large}
{: style="font-size: 100%; text-align: center;"}
