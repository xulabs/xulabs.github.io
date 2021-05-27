---
permalink: /coronavirus/VMDTutorial
title: "VMD Tutorial"
sidebar: 
 nav: "coronavirus"
toc: true
toc_sticky: true
---

This is a short tutorial on how to use VMD to visualize molecules and perform some basic analysis. Before you start, make sure to have downloaded and installed <a href="https://www.ks.uiuc.edu/Development/Download/download.cgi?PackageName=VMD" target="_blank">VMD</a>.

### Loading Molecules

These steps will be on how to load molecules into VMD. We will use the example of 6vw1.

Download the protein structure of <a href="https://www.rcsb.org/structure/6vw1" target="_blank">6vw1</a> from the protein data bank. 

<img src="../_pages/coronavirus/files/Ridge%20Tutorial/Ridge0.png">

Next we can launch VMD and load the molecule into the program. In *VMD Main*, go to *File>New Molecule*. Click on *Browse*, select the molecule (6vw1.pdb) and click *Load*. 

<img src="../_pages/coronavirus/files/Ridge%20Tutorial/Ridge1.png">
<img src="../_pages/coronavirus/files/Ridge%20Tutorial/Ridge2.png">

The molecule should now be listed in *VMD Main* as well as the visualization in the *OpenGL Display*.

<img src="../_pages/coronavirus/files/Ridge%20Tutorial/Ridge3.png">

<hr>

**Section to be moved**

#### Glycans

For VMD, there is no specific keyword to select glycans. A workaround is to use the keywords: "not protein and not water". To recreate the basic VMD visualizations from the module of the open-state (<a href="https://www.rcsb.org/structure/6VYB" target="_blank">6vyb</a>) of SARS-CoV-2 Spike, use the following representations. (For the protein chains, use *Glass3* for *Material*).

<img src="../_pages/coronavirus/files/GlycanImage1.png">

The end result should look like this:

<img src="../_pages/coronavirus/files/GlycanImage2.png">

<hr>

<details>
 <summary>Visualization Exercise</summary>
 Try to recreate the visualization of Hotspot31 for SARS-CoV-2 (same molecule as the tutorial). The important residues and their corresponding colors are listed on the left.

 <img src="../_pages/coronavirus/files/Hotspot31.png">
</details>

<hr>

