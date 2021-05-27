---
permalink: /chemotaxis/home_walk
title: "Bacterial Runs and Tumbles"
sidebar:
 nav: "chemotaxis"
toc: true
toc_sticky: true
---

## *E. coli* explores its world via a random walk

An *E. coli* cell has between five and twelve flagella distributed on its surface.[^Sim2017] Each flagellum can rotate both clockwise and counter-clockwise. When all of the flagella are rotating counter-clockwise, they form a bundle and propel the cell forward at a speed of about 20 µm per second. This speed may seem small, but it is about ten times the length of the cell per second, analogous to a car traveling at 160 kph (100 mph). When any flagellum rotates clockwise, the flagella become uncoordinated, and the bacterium stops and rotates in place.[^Baker2005]

When we multi-cellular beings examine the bacterium's movement, we see it alternate between periods of "running" in a straight line and then "tumbling" in place (see figure below). Over time, the bacterium takes what appears to be a *random walk* through its environment. Note that this **run and tumble** view of *E. coli* movement is similar to the exploration approach used by the Lost Immortals in the introduction.

![image-center](../assets/images/chemotaxis_intro_runtumble.png){: .align-center}
The run and tumble mechanism of bacterial movement produces a random walk. Image from <a href="http://chemotaxis.biology.utah.edu/Parkinson_Lab/projects/ecolichemotaxis/ecolichemotaxis.html">Parkinson Lab</a>.
{: style="font-size: medium;"}


## Tumbling frequency is constant across species

In the absence of an attractant or repellent, *E. coli* stops to tumble once every 1 to 1.5 seconds.[^Weis1990][^Berg2000] And it is not alone in this behavior; bacteria living in environments with similar resource distributions adopt similar movements. *Salmonella* tumbles once every second[^Achouri2015], *Enterococcus sacchrolyticus* tumbles once every 1.2 seconds, *Bacillus subtilis* tumbles once every 2 seconds[^Turner2016], and *Rhizobia* tumbles once every 1-2 seconds[^Gotz1987]. Researchers have investigated why different bacteria have different tumbling frequencies,[^Rashid2019][^Mitchell2005] but a definitive explanation for the variation in these frequencies has not been proposed.

Bacteria are amazingly diverse. They have evolved for over three billion years to thrive in practically every environment on the planet, including hazardous human-made environments. They manufacture compounds like antibiotics that larger organisms like ourselves cannot make. Some eukaryotes are even completely dependent upon bacteria to perform some critical task for them, from digesting their food, to camouflaging them from predators, to helping them develop organs[^Yong2016].

And yet despite the diversity present within the bacterial kingdom, the variations in bacterial tumbling frequencies are relatively small. Is there some reason why, regardless of the species, a bacterium's tumbling frequency tends to hover at around one tumble every second or two? It is as if there were some invisible force compelling all of these bacteria to tumble with the same frequency.

This question is a fundamental one, and we will return to it at the close of this module after we have learned more about the biochemical basis of chemotaxis and how a bacterium can adjust its behavior in response to a chemical substance. In the process, we will see that despite bacteria being simple organisms, the mechanism they use to implement chemotaxis is far more sophisticated than we might ever imagine.

**STOP:** Say that a bacterium travels 20 µm in a randomly selected direction every second.  After an hour, approximately how far will it have traveled on average?  What if we allow the bacterium to travel for a week? (Hint: recall the Random Walk Theorem from the [prologue](prologue/random-walk).)
{: .notice--primary}

[^Pierucci1978]: Pierucci O. 1978. Dimensions of *Escherichia coli* at various growth rates: Model of envelope growth. Journal of Bacteriology 135(2):559-574. [Available online](https://jb.asm.org/content/jb/135/2/559.full.pdf)

[^Sim2017]: Sim M, Koirala S, Picton D, Strahl H, Hoskisson PA, Rao CV, Gillespie CS, Aldridge PD. 2017. Growth rate control of flagellar assembly in *Escherichia coli* strain RP437. Scientific Reports 7:41189. [Available online](https://www.nature.com/articles/srep41189#:~:text=Escherichia%20coli%20is%20a%20prominent,distributed%20across%20the%20cell%20surface.)

[^Baker2005]: Baker MD, Wolanin PM, Stock JB. 2005. Signal transduction in bacterial chemotaxis. BioEssays 28:9-22. [Available online](https://pubmed.ncbi.nlm.nih.gov/16369945/)

[^Weis1990]: Weis RM, Koshland DE. 1990. Chemotaxis in *Escherichia coli* proceeds efficiently from different initial tumble frequencies. Journal of Bacteriology 172:2. [Available online](https://jb.asm.org/content/jb/172/2/1099.full.pdf)

[^Berg2000]: Berg HC. 2000. Motile behavior of bacteria. Physics today 53(1):24. [Available online](https://physicstoday.scitation.org/doi/pdf/10.1063/1.882934)

[^Achouri2015]: Achouri S, Wright JA, Evans L, Macleod C, Fraser G, Cicuta P, Bryant CE. 2015. The frequency and duration of *Salmonella* macrophage adhesion events determines infection efficiency. Philosophical transactions B 370(1661). [Available online](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4275903/)

[^Turner2016]: Turner L, Ping L, Neubauer M, Berg HC. 2016. Visualizing flagella while tracking bacteria. Biophysical Journal 111(3):630--639.[Available online](https://pubmed.ncbi.nlm.nih.gov/27508446/)

[^Parkinson2015]: Parkinson JS, Hazelbauer, Falke JJ. 2015. Signaling and sensory adaptation in *Escherichia coli* chemoreceptors: 2015 update. [Available online](https://www.sciencedirect.com/science/article/abs/pii/S0966842X15000578)

[^Yang2019]: Yang W, Cassidy CK, Ames P, Diebolder CA, Schulten K, Luthey-Schulten Z, Parkinson JS, Briegel A. 2019. *In situ* confomraitonal changes of the *Escherichia coli* serine chemoreceptor in different signaling states. mBio. [Available online](https://mbio.asm.org/content/10/4/e00973-19/article-info)

[^Saragosti2001]: Saragosti J, Calvez V, Bournaveas, N, Perthame B, Buguin A, Silberzan P. 2001. Directional persistence of chemotactic bacteria in a traveling concentration wave. PNAS. [Available online](https://www.pnas.org/content/pnas/108/39/16235.full.pdf)

[^Gotz1987]: Gotz R and Schmitt R. 1987. *Rhizobium meliloti* swims by unidirectional, intermittent rotation of right-handed flagellar helices. J Bacteriol 169: 3146–3150. [Avaialbe online](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC212363/)

[^Lim2019]: Lim S, Guo XK, Boedicker JQ. 2019. Connecting single-cell properties to collective behavior in multiple wild isolates of the *Enterobacter cloacae* complex. PLoS ONE 14(4): e0214719. [Avaialbe online](https://doi.org/10.1371/journal.pone.0214719)

[^Rashid2019]: Rashid S, Long Z, Singh S, Kohram M, Vashistha H, Navlakha S, Salman H, Oltvai ZH, Bar-Joseph Z. 2019. Adjustment in tumbling rates improves bacterial chemotaxis on obstacle-laden terrains. PNAS 116(24):11770-11775. [Available online](https://www.pnas.org/content/116/24/11770)

[^Mitchell2005]: Mitchell JG, Kogure K. 2005. Bacterial motility: links to the environment and a driving force for microbial physics. FEMS Microbiol Ecol 55(2006):3–16. [Available online](https://academic.oup.com/femsec/article/55/1/3/554107)

[^Yong2016]: Ed Yong. *I Contain Multitudes: The Microbes Within Us and a Grander View of Life*.

[Next lesson](home_signal){: .btn .btn--primary .btn--large}
{: style="font-size: 100%; text-align: center;"}
