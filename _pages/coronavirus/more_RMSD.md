---
permalink: /coronavirus/more_RMSD
title: "Protein Structure Prediction"
sidebar: 
 nav: "coronavirus"
toc: true
toc_sticky: true
---

To use RMSD as a quantitative measure for comparing protein structures, the structures must first be superposed in such a way that the RMSD is minimized.

Back in the tutorial, superposing was accomplished by utilizing the *calcTransformation()* function, which returns the optimal transformation matrix between two structures such that the RMSD is minimized. This transformation matrix is consists of translation vector and rotation matrix, which can be calculated using the Kabsch Algorithm.

The source code for *calcTransformation()* can be found 
<a href="http://prody.csb.pitt.edu/_modules/prody/measure/transform.html#calcTransformation" target="_blank">here</a>.

## How it Works: Kabsch Algorithm (Partial Procrustes Superimposition)

The Kabsch Algorithm is an algorithm that finds the optimal rotation matrix in which the RMSD between two paired sets of points is minimized (the two sets must have the same number of points). In our case, the two sets of points are the 3D coordinate points of the Cα (carbon skeleton) of the two protein structures that we want to compare. The algorithm can be broken down into three major steps: Translation, Covariance, and Singular Value Decomposition.

### Input
The input will be a (N x 3) matrix for each set of points, where N is the number of points per set. The three column represent the 3D coordinate set per N points.

### Translation Step
Each set of points is translated such that their centroid lies on the origin of the coordinate system. This is easily done by subtracting the coordinates of the centroid from the respective point coordinates.

### Covariance Step
The next step is to calculate the cross-covariance matrix. Let H be the cross-covariance matrix, and P and Q be the two translated input matrixes such that for the result of the algorithm, P will be rotated into Q.

<a href="https://www.codecogs.com/eqnedit.php?latex=\large&space;H&space;=&space;P^{T}Q" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\large&space;H&space;=&space;P^{T}Q" title="\large H = P^{T}Q" /></a>

Or in summation notation:

<a href="https://www.codecogs.com/eqnedit.php?latex=\large&space;H_{i,j}&space;=&space;\sum_{N}^{k=1}&space;P_{k,i}&space;Q_{k,j}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\large&space;H_{i,j}&space;=&space;\sum_{N}^{k=1}&space;P_{k,i}&space;Q_{k,j}" title="\large H_{i,j} = \sum_{N}^{k=1} P_{k,i} Q_{k,j}" /></a>

### Singluar Value Decomposition (SVD) Step
It is possible to get the optimal rotation matrix, R, with the formula:

<a href="https://www.codecogs.com/eqnedit.php?latex=\large&space;R&space;=&space;(H^TH)^{\frac{1}{2}}H^{-1}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\large&space;R&space;=&space;(H^TH)^{\frac{1}{2}}H^{-1}" title="\large R = (H^TH)^{\frac{1}{2}}H^{-1}" /></a>

However, this is not always possible and can become quite complicated (e.g. H not having an inverse). Another method is to use singular value decomposition of the covariance matrix. Kabsch algorith utilizes SVD of H to compute R:

<a href="https://www.codecogs.com/eqnedit.php?latex=\large&space;H&space;=&space;VSW^T" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\large&space;H&space;=&space;VSW^T" title="\large H = VSW^T" /></a>

In order to ensure that the rotation matrix is a right-handed coordinate system, the matrix may need to be corrected by calculating the determinant of the dot product of W and V<sup>T</sup>:

<a href="https://www.codecogs.com/eqnedit.php?latex=\large&space;d&space;=&space;sign(det(WV^T))" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\large&space;d&space;=&space;sign(det(WV^T))" title="\large d = sign(det(WV^T))" /></a>

Finally, R can be calculated with the following matrix formula:

<a href="https://www.codecogs.com/eqnedit.php?latex=\large&space;R&space;=&space;W\bigl(\begin{smallmatrix}&space;1&space;&&space;0&space;&&space;0\\&space;0&space;&&space;1&space;&&space;0\\&space;0&space;&&space;0&space;&&space;d&space;\end{smallmatrix}\bigr)&space;V^T" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\large&space;R&space;=&space;W\bigl(\begin{smallmatrix}&space;1&space;&&space;0&space;&&space;0\\&space;0&space;&&space;1&space;&&space;0\\&space;0&space;&&space;0&space;&&space;d&space;\end{smallmatrix}\bigr)&space;V^T" title="\large R = W\bigl(\begin{smallmatrix} 1 & 0 & 0\\ 0 & 1 & 0\\ 0 & 0 & d \end{smallmatrix}\bigr) V^T" /></a>

[Return to main text](accuracy){: .btn .btn--primary .btn--large}
{: style="font-size: 100%; text-align: center;"}
