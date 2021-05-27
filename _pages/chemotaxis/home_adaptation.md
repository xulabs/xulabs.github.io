---
permalink: /chemotaxis/home_senseadap
title: "Methylation Helps Bacteria Adapt to Differing Concentrations"
toc: true
toc_sticky: true
sidebar:
 nav: "chemotaxis"
toc: true
toc_sticky: true
---

## Bacterial tumbling frequencies remain constant despite background attractant concentrations

In the previous lesson, we explored the signal transduction pathway by which *E. coli* can change its tumbling frequency in response to a change in the concentration of an attractant. But the reality of cellular environments is that the concentration of a substance in these environments can vary across several orders of magnitude. The cell therefore needs to detect not *absolute* concentrations of a substance but rather *relative* changes so that it can move in the direction of an attractant (or away from a repellent).

**STOP:** Consider two bacterial cells, both of which are in well-mixed environments with fixed glucose concentrations. The first cell's environment has a glucose concentration of *x*, and the second cell's environment has a glucose concentration of 0.1*x*. Should the default tumbling frequency of the two cells be the same?  What if we drop a sugar cube into both environments?  Should the two cells respond in the same way or in different ways in response to the attractant?
{: .notice--primary}

The ability of *E. coli* to react to *relative* changes in its environment is not  present in our current model of chemotaxis. According to our current model, if a cell is in an environment with high background concentration of an attractant, then the cell will detect a signal and lower its tumbling frequency. If the concentration continues to increase, then it may not be able to lower this frequency any further.

*E. coli* detects relative changes in its concentration via **adaptation** to the signal concentration. If the concentration of attractant remains constant for a period of time, then regardless of the absolute value of the concentration, the cell returns to the same background tumbling frequency. In other words, *E. coli* demonstrates *robustness* to the background concentration of attractant in maintaining its  default tumbling behavior.

In this lesson, we will investigate the biochemical mechanism that *E. coli* uses to achieve such a robust response to environments with different background concentrations. We will then further expand the model we built in the previous lesson to see if this model can replicate the bacterium's adaptive response.

## Bacteria have a "memory" of past concentrations using methylation

Recall from the previous lesson that in the absence of an attractant, CheW and CheA readily bind to an MCP, leading to greater autophosphorylation of CheA, which in turn phosphorylates CheY. The greater the concentration of phosphorylated CheY, the more frequently the bacterium tumbles.

Signal transduction is achieved through phosphorylation, but *E. coli* maintains a "memory" of past environmental concentrations through a chemical process called **methylation**. In this  reaction, a **methyl group** (-CH<sub>3</sub>) is added to an organic molecule; the removal of a methyl group is called **demethylation**.

Every MCP receptor contains four methylation sites, meaning that between zero and four methyl groups can be added to the receptor. On the plasma membrane, many MCPs, CheW, and CheA molecules form an array structure. Methylation reduces the negative charge on the receptors, stabilizing the array and facilitating CheA autophosphorylation. The more sites that are methylated, the higher the autophosphorylation rate of CheA, which means that CheY has a higher phosphorylation rate, and tumbling frequency increases.

We now have two different ways that tumbling frequency can be elevated. First, if the concentration of an attractant is low, then CheW and CheA freely form a complex with the MCP, and the phosphorylation cascade passes phosphoryl groups to CheY, which interacts with the flagella and keeps tumbling frequency high. Second, an increase in MCP methylation can also boost CheA autophosphorylation and lead to an increased tumbling frequency.

Methylation of MCPs is achieved by an additional protein called **CheR**. When bound to MCPs, CheR methylates ligand-bound MCPs faster[^Amin2010][^Terwilliger1986], and so the rate of MCP methylation by CheR is higher if the MCP is bound to a ligand.[^Spiro1997]. Therefore, say that *E. coli* encounters an increase in attractant concentration. Then the lack of a phosphorylation cascade will mean that there is less phosphorylated CheY, and so the tumbling frequency will decrease. However, if the attractant concentration levels off, then the tumbling frequency will flatten, while CheR starts methylating the MCP. Over time, the rising methylation will increase CheA autophosphorylation, bringing back the phosphorylation cascade and raising tumbling frequency back to default levels.

<!--
![image-center](../assets/images/chemotaxis_methylation.png){: .align-center}
<figcaption>The chemotaxis signal-transduction pathway with methylation included. CheA phosphorylates CheB. CheB methylates while CheR demethylates MCP. Blue curve: phosphorylation; grey curve: dephosphorylation; green arrow: methylation. Figure inspired by Parkinson Lab illustrations.[^ParkinsonLab]</figcaption>
-->

<!--
 - MCP + CheR -> MCP-CH<sub>3</sub> + CheR
 - CheA-P + CheB -> CheA + CheB-P
 - CheB-P -> CheB + P
 - MCP-CH<sub>3</sub> + CheB-P -> MCP + CheB-P
-->

Just as the phosphorylation of CheY can be reversed, MCP methylation can be undone as well to prevent methylation from being permanent. In particular, an enzyme called **CheB**, which like CheY is phosphorylated by CheA, demethylates MCPs (as well as autodephosphorylates). The rate of an MCP's demethylation is dependent on the extent to which the MCP is methylated. In other words, the rate of MCP methylation is higher when the MCP is in a low methylation state, and the rate of demethylation is faster when the MCP is in a high methylation state.[^Spiro1997]

The figure below adds CheR and CheB to provide a complete picture of the core pathways influencing chemotaxis. To model these pathways, we will need to add quite a few molecules and reactions to our current model.

![image-center](../assets/images/chemotaxis_wholestory.png){: .align-center}
The chemotaxis signal-transduction pathway with methylation included. CheA phosphorylates CheB, which methylates MCPs while CheR demethylates MCPs. Blue lines denote phosphorylation, grey lines denote dephosphorylation, and the green arrow denotes methylation. Image modified from <a href="http://chemotaxis.biology.utah.edu/Parkinson_Lab/projects/ecolichemotaxis/ecolichemotaxis.html">Parkinson Lab</a>'s illustrations.
{: style="font-size: medium;"}

## Combinatorial explosion and the need for rule-based modeling

Our goal is to expand the BioNetGen model that we built in the previous lesson, and then see if this model can replicate the adaptation behavior of *E. coli* in the presence of a changing attractant concentration. Before incorporating the adaptation mechanisms in our BNG model, we will first describe the reactions that BioNetGen will need.

We begin with considering the MCP complexes. In the [phosphorylation tutorial](tutorial_phos), we identified two components relevant for reactions involving MCPs: a ligand-binding component `l` and a phosphorylation component `Phos`. The adaptation mechanism introduces two additional reactions: methylation of the MCP by CheR, and demethylation of the MCP by CheB.

We also need to include binding and dissociation reactions between the MCP and CheR because under normal conditions, most CheR are bound to MCP complexes.[^Lupas1989] We will therefore introduce two additional components to the MCP molecules in addition to their phosphorylation components: `r` (denoting CheR-binding) and `Meth` (denoting methylation states). In our simulation, we will use three methylation levels (low, medium, and high) because these three states are most involved in the chemotaxis response to attractants.[^Boyd1980]

Imagine for a moment that we were attempting to specify every reaction that could take place in our model. To specify an MCP, we would need to tell the program whether it is bound to a ligand (two possible states), whether it is bound to CheR (two possible states), whether it is phosphorylated (two possible states), and which methylation state it is in (three possible states). Therefore, a given MCP has 2 · 2 · 2 · 3 = 24 total states.

Say that we are simulating the simple reaction of a ligand binding to an MCP, which we originally wrote as *T* + *L* → *TL*. We now need this reaction to include 12 of the 24 states, which are those corresponding to the MCP being unbound to the ligand. Our simple reaction would become 12 different reactions, one for each possible unbound state of the complex molecule *T*. And if the situation were just a little more complex, with the ligand molecule *L* having *n* possible states, then we would have 12*n* reactions. Imagine trying to debug a model in which we had accidentally incorporated a typo when transcribing just one of these reactions!

In other words, as our model grows, with multiple different states for each molecule involved in each reaction, the number of reactions we need to represent the system grows very fast; this phenomenon is called **combinatorial explosion**. Our model of chemotaxis is ultimately relatively straightforward, but combinatorial explosion means that building realistic models of biochemical systems at scale without a simplifying language can be daunting if not impossible.

A major benefit of using a rule-based modeling language provided by BioNetGen is that it circumvents combinatorial explosion by consolidating many reactions into a single rule. For example, when modeling ligand-MCP binding, we can summarize the 12 different reactions with the rule "a free ligand molecule binds to an MCP that is not bound to a ligand molecule." In the BioNetGen language, this rule is represented by the same one-line expression as it was in the previous lesson:

~~~ ruby
LigandReceptor: L(t) + T(l) <-> L(t!1).T(l!1) k_lr_bind, k_lr_dis
~~~

Why is one rule enough? Recall from our discussion of the [Gillespie algorithm](/home_signalpart2#an-overview-of-the-gillespie-algorithm) that the wait time before the next reaction to be sampled depends only on the rate of all relevant reactions in the system. In this particular case, the rate of ligand-MCP binding depends on the total concentration of free ligands and unbound MCPs, but it does not depend on the state that an MCP is in.

In the following tutorial, we will expand our BioNetGen model from the previous tutorial into one that can incorporate CheR binding as well as MCP methylation while avoiding combinatorial explosion. We will then examine whether this model allows us to learn anything about how a bacterium can adapt to changes in the relative concentration of attractant.

[Visit tutorial](tutorial_adap){: .btn .btn--primary .btn--large}
{: style="font-size: 100%; text-align: center;"}

## Bacterial tumbling is resilient to large sudden changes in ligand concentration

In the figures below, we show plots of the concentration of each molecule of interest in our system for a few different cases. In each case, we suddenly change the concentration of the attractant ligand (*l*<sub>0</sub>) and examine how this affects the concentration of phosphorylated CheY (the molecule whose phosphorylation is directly correlated with increased tumbling frequency). The attractant concentration will then level off; because the relative concentration is not changing, will our model reflect the hypothesis that *E. coli* can return to approximately the same steady-state concentration of phosphorylated CheY regardless of the concentration of the ligand?

Below, we show simulation results for some different concentrations of ligand molecules added at the beginning of the simulation. First we add a relatively small amount, setting *l*<sub>0</sub> equal to 10,000. The system returns so quickly to an equilibrium in phosphorylated CheY that it is difficult to think that the attractant has had any effect on tumbling frequency. (Note: time is shown in seconds on the x-axis in the following figures.)

![image-center](../assets/images/chemotaxis_tutorial_oneadd1e4.png){: .align-center}

If instead *l*<sub>0</sub> is equal to 100,000, we obtain the figure below. After a drop in the concentration of phosphorylated CheY, the system returns to equilibrium after a few minutes.

![image-center](../assets/images/chemotaxis_tutorial_oneadd1e5.png){: .align-center}

When we increase *l*<sub>0</sub> by another factor of ten to 1 million, the initial drop is more pronounced, but the system is able to just as quickly return to equilibrium. Note how much higher the concentration of methylated receptors are in this figure compared to the previous figure; however, there are still a significant concentration of receptors with low methylation, indicating that the system may be able to handle a yet bigger jolt.

![image-center](../assets/images/chemotaxis_tutorial_oneadd1e6.png){: .align-center}

When we set *l*<sub>0</sub> equal to 10 million, we give the system this bigger jolt. Once again, the model is resilient to this change in the concentration of the ligand after a few minutes.

![image-center](../assets/images/chemotaxis_tutorial_oneadd1e7.png){: .align-center}

Finally, with *l*<sub>0</sub> equal to 100 million, we see what we might expect: the steepest drop in phosphorylated CheY yet, but a system that is able to return to equilibrium.

![image-center](../assets/images/chemotaxis_tutorial_oneadd1e8.png){: .align-center}

Our model therefore has provided compelling evidence that the *E. coli* chemotaxis system is very robust to changes in its environment. The simulated bacterium can make a very rapid change in response to a sudden change in its environment, but even if this change is significant, the system will return to its default state. This robustness in our simulation has been observed in real bacteria[^Shimizu2005][^Krembel2015], as well as replicated by other computational simulations[^Bray1993].

Aren't bacteria magnificent?

However, our work is not done. We have simulated how a bacterium can adapt to a single sudden change in its environment, but life is about responding to changes all the time. So in the next lesson, we will further examine how our simulated *E. coli* responds in an environment in which the ligand concentration is changing constantly.

[Next lesson](home_gradient){: .btn .btn--primary .btn--large}
{: style="font-size: 100%; text-align: center;"}

## Additional resources

Some resources/reads if you are interested in the chemotaxis biology:
 - Amazing introduction to chemotaxis: Parkinson Lab [website](http://chemotaxis.biology.utah.edu/Parkinson_Lab/projects/ecolichemotaxis/ecolichemotaxis.html).
 - A good overview: by Webre et al. published in 2003. [Available online](https://www.cell.com/current-biology/pdf/S0960-9822(02)01424-0.pdf)
 - Details on chemotaxis pathway and MCPs: review article by Baker et al. published in 2005 [Available online](https://pubmed.ncbi.nlm.nih.gov/16369945/).
 - Details on MCPs: more recent review by Parkinson et al. published in 2015. [Available online](https://www.sciencedirect.com/science/article/abs/pii/S0966842X15000578).
 - Modeling robustness and integral feedback: lecture note by Berg in 2008. [Available online](https://www.weizmann.ac.il/mcb/UriAlon/sites/mcb.UriAlon/files/uploads/lecture_notes_-_robustness_in_bacterial_chemotaxis_.pdf).


[^Munroe]: Randall Munroe. What If? [Available online](https://what-if.xkcd.com/)

[^Pierucci1978]: Pierucci O. 1978. Dimensions of *Escherichia coli* at various growth rates: Model of envelope growth. Journal of Bacteriology 135(2):559-574. [Available online](https://jb.asm.org/content/jb/135/2/559.full.pdf)

[^Sim2017]: Sim M, Koirala S, Picton D, Strahl H, Hoskisson PA, Rao CV, Gillespie CS, Aldridge PD. 2017. Growth rate control of flaggelar assembly in *Escherichia coli* strain RP437. Scientific Reports 7:41189. [Available online](https://www.nature.com/articles/srep41189#:~:text=Escherichia%20coli%20is%20a%20prominent,distributed%20across%20the%20cell%20surface.)

[^Baker2005]: Baker MD, Wolanin PM, Stock JB. 2005. Signal transduction in bacterial chemotaxis. BioEssays 28:9-22. [Available online](https://pubmed.ncbi.nlm.nih.gov/16369945/)

[^Weis1990]: Weis RM, Koshland DE. 1990. Chemotaxis in *Escherichia coli* proceeds efficiently from different initial tumble frequencies. Journal of Bacteriology 172:2. [Available online](https://jb.asm.org/content/jb/172/2/1099.full.pdf)

[^Berg2000]: Berg HC. 2000. Motile behavior of bacteria. Physics today 53(1):24. [Available online](https://physicstoday.scitation.org/doi/pdf/10.1063/1.882934)

[^Achouri2015]: Achouri S, Wright JA, Evans L, Macleod C, Fraser G, Cicuta P, Bryant CE. 2015. The frequency and duration of *Salmonella* macrophage adhesion events determines infection efficiency. Philosophical transactions B 370(1661). [Available online](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4275903/)

[^Turner2016]: Turner L, Ping L, Neubauer M, Berg HC. 2016. Visualizing flagella while tracking bacteria. Biophysical Journal 111(3):630--639.[Available online](https://pubmed.ncbi.nlm.nih.gov/27508446/)

[^Parkinson2015]: Parkinson JS, Hazelbauer, Falke JJ. 2015. Signaling and sensory adaptation in *Escherichia coli* chemoreceptors: 2015 update. [Available online](https://www.sciencedirect.com/science/article/abs/pii/S0966842X15000578)

[^Yang2019]: Yang W, Cassidy CK, Ames P, Diebolder CA, Schulten K, Luthey-Schulten Z, Parkinson JS, Briegel A. 2019. *In situ* confomraitonal changes of the *Escherichia coli* serine chemoreceptor in different signaling states. mBio. [Available online](https://mbio.asm.org/content/10/4/e00973-19/article-info)

[^Saragosti2001]: Saragosti J, Calvez V, Bournaveas, N, Perthame B, Buguin A, Silberzan P. 2001. Directional persistence of chemotactic bacteria in a traveling concentration wave. PNAS. [Available online](https://www.pnas.org/content/pnas/108/39/16235.full.pdf)

[^Hlavacek2003]: Hlavacek WS, Faeder JR, Blinov ML, Perelson AS, Goldsten B. 2003. The complexity of complexes in signal transduction. Biotechnology and Bioengineering 84(7):783-94. [Available online](https://onlinelibrary.wiley.com/doi/abs/10.1002/bit.10842)

[^Hlavacek2006]: Hlavacek WS, Faeder JR, Blinov ML, Posner RG, Hucka M, Fontana W. 2006. Rules for modeling signal-transduction systems. Science Signaling 344:re6. [Available online](https://stke.sciencemag.org/content/2006/344/re6.long)

[^ParkinsonLab]: Parkinson Lab website. [website](http://chemotaxis.biology.utah.edu/Parkinson_Lab/projects/ecolichemotaxis/ecolichemotaxis.html)

[^Spiro1997]: Spiro PA, Parkinson JS, and Othmer H. 1997. A model of excitation and adaptation in bacterial chemotaxis. Biochemistry 94:7263-7268. [Available online](https://www.pnas.org/content/94/14/7263).

[^Bray1993]: Bray D, Bourret RB, Simon MI. 1993. Computer simulation of phosphorylation cascade controlling bacterial chemotaxis. Molecular Biology of the Cell. [Available online](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC300951/)

[^Li2004]: Li M, Hazelbauer GL. 2004. Cellular stoichimetry of the components of the chemotaxis signaling complex. Journal of Bacteriology. [Available online](https://jb.asm.org/content/186/12/3687)

[^Stock1991]: Stock J, Lukat GS. 1991. Intracellular signal transduction networks. Annual Review of Biophysics and Biophysical Chemistry. [Available online](https://www.annualreviews.org/doi/abs/10.1146/annurev.bb.20.060191.000545)

[^Shimizu2005]: Shimizu TS, Delalez N, Pichler K, and Berg HC. 2005. Monitoring bacterial chemotaxis by using bioluminescence resonance energy transfer: absence of feedback from the flagellar motors. PNAS. [Available online](https://www.pnas.org/content/103/7/2093/)

[^Krembel2015]: Krembel A., Colin R., Sourijik V. 2015. Importance of multiple methylation sites in *Escherichia coli* chemotaxis. [Available online](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0145582)

[^Amin2010]: Amin DN, Hazelbauer GL. 2010. Chemoreceptors in signaling complexes: shifted conformation and asymmetric coupling. [Available online](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3010867/)

[^Terwilliger1986]: Terwilliger TC, Wang JY, Koshland DE. 1986. Kinetics of Receptor Modification - the multiply methlated aspartate receptors involved in bacterial chemotaxis. The Journal of Biolobical Chemistry. [Available online](https://www.jbc.org/content/261/23/10814.full.pdf)

[^Chylek2015]: Chylek LA, Harris LA, Tung CS, Faeder JR, Lopez CF, Hlavacek WS. 2015. Rule-based modeling: a computational approach for studying biomolecular site dynamics in cell signaling systems. Wiley Interdiscip Rev Syst Biol Med 6(1):13-36. [Available online](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3947470/)

[^Boyd1980]: Boyd A., and Simon MI. 1980. Multiple electrophoretic forms of methyl-accepting chemotaxis proteins generated by stimulus-elicited methylation in Escherichia coli. Journal of Bacteriology 143(2):809-815. [Available online](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC294367/pdf/jbacter00569-0269.pdf)

[^Lupas1989]: Lupas A., and Stock J. 1989. Phosphorylation of an N-terminal regulatory domain activates the CheB methylesterase in bacterial chemotaxis. J Bio Chem 264(29):17337-42. [Available online](https://pubmed.ncbi.nlm.nih.gov/2677005/)
