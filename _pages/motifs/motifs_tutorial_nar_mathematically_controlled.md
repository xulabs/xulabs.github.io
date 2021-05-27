---
permalink: /motifs/tutorial_nar_mathematically_controlled
title: "Software Tutorial: Ensuring a mathematically controlled simulation for comparing simple regulation to negative autoregulation"
sidebar:
 nav: "motifs"
toc: true
toc_sticky: true
---

In this tutorial, we will use CellBlender to adapt our simulation from the [tutorial](tutorial_nar) on negative autoregulation into a mathematically controlled simulation.

First, open the file `NAR_comparison.blend` from the negative autoregulation tutorial and save a copy of the file as `NAR_comparison_equal.blend`. You may also download the completed tutorial files <a href="../tutorials/NAR_compare_equal.blend" download="NAR_compare_equal.blend">here</a>.

Now go to `CellBlender > Reactions` to scale up the simple regulation reaction in the negative autoregulation simulation as follows: for the reaction `X2’ -> X2’ + Y2’`,  change the forward rate from `4e2` to `4e3`.

Next go to `CellBlender > Run Simulation` and ensure that the following options are selected:

![image-center](../assets/images/motifs_norm7.png){: .align-center}

1. Set the number of iterations to `20000`.
2. Ensure the time step is set as `1e-6`.
3. Click `Export & Run`.

Click on `CellBlender > Reload Visualization Data`. You have the option of watching the animation within the Blender window by clicking the play button at the bottom of the screen.

![image-center](../assets/images/motifs_norm8.png){: .align-center}

Now go back to `CellBlender > Plot Output Settings` and scroll to the bottom to click `Plot`; this should produce a plot. How does your plot

![image-center](../assets/images/motifs_norm9.png){: .align-center}

Save your file before returning to the main text, where we will interpret the plot produced to see if we were able to obtain a mathematically controlled simulation and then interpret the result of this simulation from an evolutionary perspective.

[Return to main text](nar#an-evolutionary-basis-for-negative-autoregulation){: .btn .btn--primary .btn--large}
{: style="font-size: 100%; text-align: center;"}
