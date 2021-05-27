---
permalink: /motifs/conclusion
title: "Conclusion: The Importance of Robustness in Biological Oscillations"
sidebar:
 nav: "motifs"
toc: true
toc_sticky: true
---

## The need for robustness in biological oscillators

Nothing exemplifies the need for robustness in biological systems better than oscillators. If your heart skips a beat when you are watching a horror movie, it should be able to return quickly to its natural rhythm. When you hold your breath to dive underwater, you shouldn't hyperventilate when you return to the surface. And regardless of what functions your cells perform or what disturbances they find in their environment, they should be able to maintain a normal cell cycle.

An excellent illustration of the robustness of the circadian clock is the body's ability to handle jet lag. There is no apparent reason why humans would have evolved to be resilient to flying halfway around the world. And yet our circadian clock is so resilient that after a few days of fatigue and crankiness, we return to a normal daily cycle.

In the previous lesson, we saw that the repressilator will oscillate even in a noisy environment. This behavior leads us to wonder about the extent to which the repressilator is robust. Much like the circadian clock responding to jet lag, we wonder how quickly the repressilator can respond to the jolt of a sudden disturbance in the concentrations of its particles.

## A coarse-grained model for the repressilator

We have noted that a benefit of using a reaction-diffusion particle model to study network motifs is the inclusion of built-in noise to ensure a measure of robustness. However, as we saw in the [prologue](prologue) with our work on Turing patterns, a downside of a particle-based model is that tracking the movements of many particles leads to a slow simulation that does not scale well given more particles or reactions.

Although our model is ultimately interested in molecular interactions, the conclusions we have made throughout this chapter are only based on the *concentrations* of these particles. Therefore, we might imagine developing a coarser-grained version of our model that allows us to make faster conclusions about particle concentrations without keeping track of the diffusion of individual particles.

In the prologue, we introduced a cellular automaton for simplifying the study of Turing patterns because the model at hand was dependent upon the *spatial* organization of particles because particles were present at different concentration across the grid and were diffusing at different rates. In this case, we will implement an even simpler model because we can assume that the concentrations of particles are *uniform*.

For example, say that we are modeling a degradation reaction. If we start with 10,000 *X* particles, then after a single time step, we will simply multiply the number of *X* particles by (1-*r*), where *r* is a parameter related to the rate of the degradation reaction.

As for a repression reaction like *X* + *Y* → *X*, we can update the concentration of *Y* particles by subtracting some factor times the current concentration of *Y* particles. This factor should be directly related to the current concentrations of both *X* and *Y*.

We will focus on the technical details behind such a coarse-grained "particle-free" model in the next module. In the meantime, we provide a tutorial below showing how to build a particle-free simulation replicating the repressilator motif. As part of this tutorial, we will make a major disturbance to the concentration of one of the particles and see how long the disturbance lasts and whether the particle concentrations resume their oscillations.

[Visit tutorial](tutorial_perturb){: .btn .btn--primary .btn--large}
{: style="font-size: 100%; text-align: center;"}

## The repressilator is robust to disturbance

In the figure below, we show a plot of concentrations of each particle in our particle-free simulation of the repressilator, with one caveat.  Midway through the simulation, we greatly increase the concentration of *Y*.

![image-center](../assets/images/nf_sim_interrupted.PNG){: .align-center}
Adding a significant number of *Y* particles to our simulation produces little ultimate disturbance to the concentrations of the three particles, which return to normal oscillations within a single cycle.
{: style="font-size: medium;"}

Because of the spike in the concentration of *Y*, the reaction *Y* + *Z* → *Y* suppresses the concentration of *Z* for longer than usual, and so the concentration of *X* is free to increase for longer than normal. As a result, the next peak in the concentration of *X* is higher than normal.

We might hypothesize that this process would continue, with a tall peak in the concentration of *Z*. However, the peak in the concentration of *Z* is no taller than normal, and the next peak shows a normal concentration of *X*. In other words, the system has very quickly absorbed the blow of an increase in concentration of *Y* and returned to normal within one cycle.

Even with a much larger jolt to the concentration of *Y*, we observe the concentrations of the three particles return to normal oscillations very quickly (figure below).

![image-center](../assets/images/nf_sim_interrupted_spike.PNG){: .align-center}

The repressilator is not the only network motif that leads to oscillations of particle concentrations, but robustness to disturbance is a shared feature of all these motifs. This having been said, the repressilator is particularly successful at stabilizing. And although there have been some attempts to study what makes oscillators robust, the process remains difficult to describe. By characterizing the number and type of interactions within the oscillator model, it has been shown that at least five reactions are typically needed to build a very robust oscillator[^repress].

The robustness of the repressilator also implies a bigger picture moral in biological modeling. If an underlying biological system demonstrates robustness to change, then any model of that system should also be able to withstand this change. Conversely, we should be wary of a model of a robust system that does not display this robustness.

We have seen that even very simple network motifs can have a powerful effect on a cell's ability to implement elegant behavior. In the next module, we will encounter a much more involved biochemical process, with far more molecules and reactions, that is used by bacteria to cleverly (and robustly) explore their environment. In fact, we will have so many particles and so many reactions that we will need to completely rethink how we set up our model. We hope that you will join us!

In the meantime, check out the exercises below to continue developing your understanding of how transcription factor network motifs have evolved.

[Visit exercises](exercises){: .btn .btn--primary .btn--large}
{: style="font-size: 100%; text-align: center;"}

[^ffl]: Image adapted from Mangan, S., & Alon, U. (2003). Structure and function of the feed-forward loop network motif. Proceedings of the National Academy of Sciences of the United States of America, 100(21), 11980–11985. https://doi.org/10.1073/pnas.2133841100

[^oscillator]: Elowitz, M. B. & Leibler, S. A Synthetic Oscillatory Network of Transcriptional Regulators. Nature 403, 335-338 (2000).

[^repress]: Castillo-Hair, S. M., Villota, E. R., & Coronado, A. M. (2015). Design principles for robust oscillatory behavior. Systems and Synthetic Biology, 9(3), 125–133. https://doi.org/10.1007/s11693-015-9178-6
