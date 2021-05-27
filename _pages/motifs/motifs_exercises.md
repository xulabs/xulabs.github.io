---
permalink: /motifs/exercises
title: "Network Motifs Exercises"
sidebar:
 nav: "motifs"
---

## Identifying Feed-Forward Loops and More Complex Motifs

**Exercise 1:** Modify the Jupyter notebook provided in the [tutorial on loops](tutorial_loops) to count the number of feed-forward loops in the transcription factor network for *E. coli.*
{: .notice--info}

There are eight types of feed-forward loops based on the eight different ways in which we can label the edges in the network with a "+" or a "-" based on upregulation or downregulation. 

![image-center](../assets/images/ffl_types.png){: .align-center}
The eight types of feed-forward loops.[^ffl]
{: style="text-align: center; font-size: medium;"}

**Exercise 2:** Modify the Jupyter notebook to count the number of loops of each type present in the *E. coli* transcription factor network.
{: .notice--info}

**Exercise 3:** How many feed-forward loops would you expect to see in a random network having the same number of nodes as the *E. coli* transcription factor network? How does this compare to your answers to the previous two questions?
{: .notice--info}

More complex motifs may require more computational power to discover. 

![image-center](../assets/images/s_cerevisiae_tf_network.jpg){: .align-center}
Example of different motifs within the *S. Cerevisiae* network.[^scNetwork]
{: style="text-align: center; font-size: medium;"}

**Exercise 4:** Can you modify our Jupyter Notebook for motif finding to identify circular loops of transcription factor regulation, such as the multi-component loop above?
{: .notice--info}

## Negative Autoregulation

Using the *NAR_comparison_equal.blend* file from the negative [autoregulation tutorial](tutorial_nar_mathematically_controlled), increase the reaction rate of X1 -> X1 + Y1 to 4e4, so that the table should now look like the following:

| Reactants |Products|Forward Rate|
|:--------|:-------:|--------:|
| X1’  | X1’ + Y1’ | 4e5 |
| X2’  | X2’ + Y2’ | 4e2 |
| Y1’  | NULL | 4e2 |
| Y2’  | NULL | 4e2 |
|Y2’ + Y2’|Y2’|4e2|

If we plot this graph, we can see the steady states of Y1 and Y2 are different once again. 

**Exercise 1:** Can you repair the system to find the appropriate reaction rate for X2 -> X2 + Y2 to make the steady states equal once more? Are you able to adjust the reaction Y2 + Y2 -> Y2 as well? Do the reaction rates scale at the same rate?
{: .notice--info}

**Exercise 2:** One way for the cell to apply stronger "brakes" to the simple regulation rate would be to simply increase the degradation rate, rather than implement negative autoregulation. Why do you think that the cell doesn't do this?
{: .notice--info}

## Implementing More Network Motifs
**Exercise 1:** Use the NFSim tutorial implementing the repressilator as a basis to replicate the other network motif tutorials presented in this module.
{: .notice--info}

[Next module: coming soon!](/){: .btn .btn--primary .btn--large}
{: style="font-size: 100%; text-align: center;"}

<!--
* The following section is really good but I have no idea where it goes.

## Engineering a repressilator

In *A Synthetic Oscillatory Network of Transcriptional Regulators* by Elowitz and Leibler[^oscillator], the repressilator model we have simulated in CellBlender was successfully tested in a real E. coli cell (an *in vivo* experiment). Instead of the X, Y, Z molecules we used in our simulation, the authors inserted the genes *TetR*, *LacI*, and *cI*. These genes were set up in the same arrangement as our simulation, however there were key differences in the scale of the model. Our simulation was carried out in a single space with approximately 300 molecules per species. The reactions were carried out on the order of around 600 reactions per time step for 120,000 steps.

![image-center](../assets/images/repressilator_ecoli.png){: .align-center}
The repressilator model used in Elowitz and Leibler's *E. coli* system.
{: style="text-align: center;"}

In contrast, Elowitz and Leibler described a model with a variety of different reaction rates, such as a 0.0005 promoter strength, 20 proteins created per transcript, and a protein half-life of 10 minutes. Interestingly, this scale led to oscillations occurring with a periodicity that spanned different generations of E. coli! Nevertheless, the real E. coli repressilator systems showed clear patterns of oscillations with robustness to interruptions and disturbances. How would our simulations hold up to interruptions, and why is this kind of behavior needed in oscillators?  

![image-center](../assets/images/nf_sim_interrupted_break.PNG){: .align-center}

![image-center](../assets/images/nf_sim_interrupted_long.PNG){: .align-center}

![image-center](../assets/images/nf_sim_interrupted_spike.PNG){: .align-center}
-->

[^ffl]: Image adapted from Mangan, S., & Alon, U. (2003). Structure and function of the feed-forward loop network motif. Proceedings of the National Academy of Sciences of the United States of America, 100(21), 11980–11985. https://doi.org/10.1073/pnas.2133841100

[^oscillator]: Elowitz, M. B. & Leibler, S. A Synthetic Oscillatory Network of Transcriptional Regulators. Nature 403, 335-338 (2000).

[^scNetwork]: Lee, T. I., Rinaldi, N. J., Robert, F., Odom, D. T., Bar-Joseph, Z., Gerber, G. K., … Young, R. A. (2002). Transcriptional regulatory networks in Saccharomyces cerevisiae. Science, 298(5594), 799–804. https://doi.org/10.1126/science.1075090