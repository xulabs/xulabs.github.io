---
permalink: /coronavirus/prody
title: "ProDy"
sidebar: 
 nav: "coronavirus"
toc: true
toc_sticky: true
---

<a href="http://prody.csb.pitt.edu/" target="_blank">ProDy</a> is an open-source Python package that allows users to perform protein structural dynamics analysis. Its flexibility allows users to select specific parts or atoms of the structure for conducting normal mode analysis and structure comparison. Please be sure to have the following installed:

<a href="https://www.python.org/downloads/" target="_blank">Python</a> (2.7, 3.5, or later)

<a href="http://prody.csb.pitt.edu/downloads/" target="_blank">ProDy</a>

<a href="https://numpy.org/install/" target="_blank">NumPy</a>

<a href="https://biopython.org/" target="_blank">Biopython</a>

<a href="https://ipython.org/" target="_blank">IPython</a>

<a href="https://matplotlib.org/" target="_blank">Matplotlib</a>

### Getting Started
It is recommended that you create a workspace for storing created files when using ProDy or storing protein .pdb files. Make sure you are in your workspace before starting up IPython.
~~~ python
ipython --pylab
~~~~~

Import functions and turn interactive mode on (only need to do this once per session).
~~~ python
In[#]: from pylab import *
In[#]: from prody import *
In[#]: ion()
~~~~~


[VMD Tutorial](VMDTutorial){: .btn .btn--primary .btn--x-large}
{: style="font-size: 100%; text-align: center;"}
