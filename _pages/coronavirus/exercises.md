---
permalink: /coronavirus/exercises
title: "Exercises: Coming Soon!"
sidebar:
 nav: "coronavirus"
toc: true
toc_sticky: true
---

* Good exercise: find centroid of a given shape.

* exercise: compute RMSD.

* Good exercise later: compute Q scores for the protein structure comparison that we performed at the end of part 1.

* Good exercise: compute Qres for very simple proteins

* Exercise based on following excellent observation: In the case of RMSD, I believe that they assign the RMSD of an alignment between a residue and gap to be 0, effectively ignoring it. I believe this is how it is ensured that the two sets have the same number of points (alpha carbons) and also one of the shortcomings of using RMSD. I think for prody, you can set a gap penalty during chain matching,

"Thus, gap-filled alignments focusing on low RMSDs, while accurate and useful for superposition of structures, are sub-optimal for machine learning as the features of many potentially relevant residues are discarded due to a lack of data in those positions. In most cases, positions with over a certain percentage of aligned residues are considered, with gaps replaced by zeros or by the average of the feature values in that position [22]."

* (RMSD with gap. Also included a jupyter notebook of this exercise with the necessary files to the email.) In this exercise, we will see what can happen to RMSD calculations when there is a gap in sequence alignment between two proteins. Let’s use our homology modeling result *robetta4* (single chain of SARS-CoV-2 Spike) and the associated SARS-CoV-2 Spike model *6vxx* from the PDB. 

First, calculate the RMSD between the two models by following the RMSD tutorial and using the chain A to chain A matching (matches[0][0] & matches[0][1]). You should get a RMSD of about 2.5853.

If you followed the tutorial, robetta4 should be under the variable struct1. We will create a new variable, *struct3*, by taking the sequence of *robetta4* and deleting a large selection. We can create the variable by using:

struct3 = struct1.select(‘resid 1 to 400 or resid 601 to 20000’)

We use a large value ‘20000’ to ensure that the rest of the protein is captured. Variable struct3 will represent the robetta4 model that has a gap/deletion at residue 400 to 600 (a 200 residue gap). Now we will repeat the RMSD calculation using struct3 instead of struct1. You should get a RMSD of about 2.1927. Is this what you expected? 

(There are less residues to compare and deviations to consider, which may have attributed to the decreased RMSD score.)



* Why are contact maps and cross correlation maps "symmetric" about the main diagonal?

* Something on identifying a dynamics difference from a contact map or better cross-correlation in similar proteins.

* If you have not already done so, try modeling the SARS-CoV-2 S protein or RBD using SWISS-MODEL, Robetta, or GalaxyWEB using the steps in<a href="tutorial_homology" target="blank">Homology Structure Prediction Tutorial</a>. Then, use ProDy to calculate the RMSD between your models and the PDB entries <a href="http://www.rcsb.org/structure/6VXX" target="blank">6vxx</a> for the S protein and <a href="http://www.rcsb.org/structure/6LZG" target="blank">6lzg</a> for the RBD. Did your models perform better than our models?

* Visualize your best performing model(s) and the corresponding PDB entryl in VMD. If the models are sufficiently similar, try performing a structural alignment using Multiseq and see where in the the structure your predicted models did well.

* Using VMD, model the SARS-CoV-2 S (<a href="http://www.rcsb.org/structure/6VXX" target="blank">6vxx</a>) protein and SARS S (<a href="https://www.rcsb.org/structure/5X58" target="blank">5x58</a>) protein. Create the graphical representation of glycans and compare the number of glycans between the two proteins. Are they any different? Could this possibly be another reason why SARS-CoV-2 is more infectious than SARS?

* In our GNM tutorial, we created the contact map using the threshold of 20Å. Try making the contact map of one of the chains of SARS-CoV-2 S protein [6vxx](http://www.rcsb.org/structure/6VXX) with different thresholds. Do the maps look different?

* In this module, we only used homology modeling for large molecules such as the SARS-CoV-2 S protein and the RBD. It would be interesting to directly compare the accuracy of homology modeling and *ab initio* modeling. Try using one of the three homology modeling softwares to predict the structure of the human hemoglobin subunit ([sequence](../_pages/coronavirus/files/Human_Hemoglobin_subunit_alpha_Seq.txt)). After you get your predicted models, try calculating the RMSD using the PDB entry [1si4](https://www.rcsb.org/structure/1sI4). How do they compare to the RMSD from our *ab inito* (QUARK) models?
