---
permalink: /coronavirus/tutorial_glycans
title: "Visualizing Glycans"
sidebar: 
 nav: "coronavirus"
toc: true
toc_sticky: true
---

Here, we will show how to visualize glycans in VMD. Be sure to have installed VMD and know how to load molecules into the program. If you need a refresher, go to the <a href="tutorial_multiseq" target="_blank">VMD and Multiseq Tutorial</a>. In the <a href="tutorial_visualization" target="_blank">Visualizing Regions and Residues Tutorial</a>, we went over how to change the visualizations of molecules and proteins in VMD. Please visit that tutorial first if you have not done so already.

We will use the PDB entry of the SARS-CoV-2 Spike protein, <a href="https://www.rcsb.org/structure/6VYB" target="_blank">6vyb</a>.

First, download and load 6vyb into VMD and go to *Graphics>Representations*. For VMD, there is no specific keyword to select glycans. A workaround is to use the keywords: "not protein and not water". To recreate the basic VMD visualizations of the glycans in the module, use the following representations. (For the protein chains, use *Glass3* for *Material*).

![image-center](../assets/images/GlycanImage1.png){: .align-center}
{: style="font-size: medium;"}

The end result should look like this:

![image-center](../assets/images/GlycanImage2.png){: .align-center}
{: style="font-size: medium;"}

In the visualization you just created, the three chains in the S protein are in dark green, dark orange, and dark yellow. The presumed glycans are shown in red. Notice how they are all over the S protein! You may have noticed that one of the chains appear to be different in that part of it is sticking out from the rest of the protein. This is because this the PDB entry 6vyb contains the structure of the SARS-CoV-2 S protein in its open conformation. Let's return to the main text to see what that means.

[Return to main text](glycans){: .btn .btn--primary .btn--large}
{: style="font-size: 100%; text-align: center;"}
