---
permalink: /motifs/finding
title: "Using Randomness to Verify Network Motifs"
sidebar:
 nav: "motifs"
toc: true
toc_sticky: true
---

## The loop: the simplest network motif

In the previous lesson, we introduced the transcription factor network, in which a protein *X* is connected to a protein *Y* if *X* is a transcription factor that regulates the production of *Y*. We also saw that in the *E. coli* transcription factor network, there seemed to be a large number of loops, or edges connecting *X* to *X* that correspond to the autoregulation of *X*.

In the introduction, we briefly introduced the notion of a network motif, or a structure occurring often throughout a network. In the remainder of this module, we discuss how to identify network motifs as well as explain why they occur so often in a network. And we will start our work by studying the loop.

## Using randomness to determine statistical significance

We first need to argue rigorously that a loop is indeed a motif within a transcription factor network. To do so, we will apply a paradigm that occurs throughout computational biology (and science in general) when determining whether an observation is significant. We will compare our observation against a  *randomly generated* database --- the power of randomness strikes again!

A seminal biological example of this paradigm is the search tool [BLAST](https://blast.ncbi.nlm.nih.gov/Blast.cgi), which allows researchers to compare a query against a database (e.g., comparing the DNA sequence of a newly sequenced gene against a collection of many known proteins). Once BLAST finds a "hit" in which the query occurs with slight modifications within the database, it asks, "What is the *probability* that we would find a hit of the same quality of the query against a randomly generated 'decoy' database?" If this probability is low, then we can feel confident that the hit is statistically significant.

**STOP:** How can we apply this paradigm to determine whether a transcription factor network contains a significant number of loops?
{: .notice--primary}

## Comparing a real transcription factor network against a random network

To determine whether the number of loops in the transcription factor network of *E. coli* is significant, we will compare the number of loops that we find in this network against the expected number of loops we would find in a randomly generated network. If the number of loops in the real network is much higher than the number of loops in the random network, then we have strong evidence that there is some selective force causing a loop to be a network motif.

There are multiple ways to generate a random network, but we will use an approach developed by Edgar Gilbert in 1959[^Gilbert]. Given an integer *n* and a probability *p* (between 0 and 1), we first form *n* nodes; then, for every possible pair of nodes *X* and *Y*, we connect *X* to *Y* via a directed edge with probability *p*.

**STOP:** What should *n* and *p* be if we are generating a random network to compare against the *E. coli* transcription factor network?
{: .notice--primary}

The full *E. coli* transcription factor network contains thousands of genes, most of which are not transcription factors. As a result, the approach described above may form a random network that connects non-transcription factors to other nodes, which we should avoid.

Instead, we will focus on the network comprising only *E. coli* transcription factors that regulate each other. This network has 197 nodes and 477 edges, and so we will begin by forming a random network with *n* = 197 nodes.

We then select *p* to ensure that our random network will on average have 477 edges. To do so, we note that there are *n*<sup>2</sup> pairs of nodes that could have an edge connecting them (*n* choices for the starting node and *n* for the ending node). If we were to set *p* equal to 1/*n*<sup>2</sup>, then we would expect on average only to see a single edge in the random network. We therefore scale this value by 477 and set *p* equal to 477/*n*<sup>2</sup> so that we will see, on average, 477 edges in our random network.

We are now ready to build a random network and compare it against the real transcription factor network. The link below will take you to a short tutorial that includes a Jupyter notebook running this comparison and demonstrating that the number of loops in the *E. coli* transcription factor network is significant. You may also feel free to skip ahead to the section below, which discusses the results of this tutorial.

[Visit tutorial](tutorial_loops){: .btn .btn--primary .btn--large}
{: style="font-size: 100%; text-align: center;"}

## The negative autoregulation motif

In a random network containing *n* nodes, the probability that a given edge is a loop is 1/*n*. Therefore, if the network has *e* edges, then we would on average see *e*/*n* loops in the network.

In our case, *n* is 197, and *e* is 477; therefore, on average, we will only see approximately 2.42 loops in a random network.  Yet the real *E. coli* network contains 130 loops!

Furthermore, in a random network, we would expect about half of the edges to correspond to upregulation, and the other half to correspond to downregulation. But if you followed the tutorial linked in the previous section, then you know that of the 130 loops in the *E. coli* network, 35 correspond to upregulation and 95 correspond to downregulation.

So, not only is autoregulation an important feature of transcription factors, but these transcription factors tend to *negatively* autoregulate. Why in the world would organisms have evolved autoregulation only to *slow* their own transcription? In the next lesson, we will begin to unravel the mystery.

[Next lesson](nar){: .btn .btn--primary .btn--large}
{: style="font-size: 100%; text-align: center;"}

[^Gilbert]: Gilbert, E.N. (1959). "Random Graphs". Annals of Mathematical Statistics. 30 (4): 1141–1144. doi:10.1214/aoms/1177706098.
