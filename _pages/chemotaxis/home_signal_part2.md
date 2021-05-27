---
permalink: /chemotaxis/home_signalpart2
title: "Stochastic simulation of multiple chemical reactions in a well mixed environment"
sidebar:
 nav: "chemotaxis"
toc: true
toc_sticky: true
---

## Verifying a theoretical steady state concentration via stochastic simulation

In the [previous module](motifs), we saw that we could avoid keeping track of the positions of individual diffusing particles in a simulation if we assume that these particles are *well-mixed*, i.e., uniformly distributed throughout their environment. The *E. coli* cell is so small that we will assume that the concentration of any particle in its immediate surroundings is uniform. Therefore, as a proof of concept, let us see if a well-mixed simulation replicates the steady state concentrations of particles that we just found.

Even though we can calculate steady state concentrations by hand, we will find a particle-free simulation useful for two reasons. First, this simulation will give us snapshots of the concentrations of particles in the system over multiple time points and allow us to see how quickly the concentrations reach equilibrium. Second, we will soon expand our model of chemotaxis to have many particles and reactions that depend on each other, and direct mathematical analysis of the system like what we have done in the previous lesson will not just be tedious; it will quickly become impossible as the number of particles and reactions grows.

The difficulty at hand is comparable to the famed "*n*-body problem" in physics. Predicting the motions of two celestial objects interacting due to gravity can be done exactly, but there is no known such solution once we add more bodies to the system.

Our particle-free model will apply an approach called **Gillespie's Stochastic Simulation Algorithm**, which is often called the **Gillespie algorithm** or just **SSA** for short. Before we explain how this algorithm works, we take a short detour to provide some needed probabilistic context.

## The Poisson and exponential distributions

Say that you own a store and have noticed that on average, there are *λ* customers entering your store in a single hour. Let *X* denote the number of customers that enter the store in the next hour; *X* is an example of a **random variable** because it may change based on random chance. If we assume that customers are independent actors and that two customers cannot arrive at the exact same time, then *X* follows a distribution called a **Poisson distribution**; it can be shown that for a Poisson distribution, the probability that exactly *n* customers arrive in the next hour is

$$\mathrm{Pr}(X = n) = \dfrac{\lambda^n e^{-\lambda}}{n!}\,.$$

A derivation of this formula is beyond the scope of our work here, but if you are interested in one, please consider [this post](https://medium.com/@andrew.chamberlain/deriving-the-poisson-distribution-from-the-binomial-distribution-840cc1668239) by Andrew Chamberlain.

Furthermore, the probability of observing exactly *n* customers in *t* hours where *t* is an arbitrary positive number is

$$\dfrac{(\lambda t)^n e^{-\lambda t}}{n!}\,.$$

We can also ask how long we will typically have to wait for the next customer to arrive. Specifically, what are the chances that this customer will arrive after *t* hours? If we let *T* be the random variable corresponding to the wait time on the next customer, then the probability of *T* being at least *t* is the probability of seeing zero customers in *t* hours:

$$\mathrm{Pr}(T > t) = \mathrm{Pr}(X = 0) = \dfrac{(\lambda t)^0 e^{-\lambda t}}{0!} = e^{-\lambda t}\,.$$

In other words, the probability $$\mathrm{Pr}(T > t)$$ decays exponentially over time as *t* increases. For this reason, the random variable *T* is said to follow an **exponential distribution.** It can be shown that the mean value of the exponential distribution (i.e., the average amount of time we will need to wait for the next event to occur) is 1/λ.

**STOP**: What is the probability Pr(*T* < *t*)?
{: .notice--primary}

## An overview of the Gillespie algorithm

The engine of the Gillespie algorithm runs on a single question: given a well-mixed environment of particles and a reaction involving those particles taking place at some average rate, how long should we expect to wait before this reaction occurs somewhere in the environment?

This is the same question we asked in the previous section; we have simply replaced customers entering a store with chemical reactions. Therefore, an exponential distribution can be used to model the "wait time" between individual reactions. The more reactions we have, and the faster these reactions occur, the larger the value of λ, meaning that we typically do not have to wait very long for the next reaction.

Numerical methods exist that allow us to generate a random number simulating the wait time of an exponential distribution. By repeatedly sampling from the exponential distribution, we obtain a collection of varying wait times between consecutive occurrences of the reaction.

Once a wait time is selected, we must determine the reaction to which this event corresponds. If the rates of the reactions are all equal, then this is an easy problem; we simply choose one of the reactions with equal probability. But if the rates of these reactions are different, then we should choose one of the reactions via a probability that is *weighted* in direct proportion to the rate of the reaction; that is, the larger the rate of the reaction, the more likely that this reaction corresponds to the current event.[^Schwartz17]

We will illustrate the Gillespie algorithm by returning to our ongoing example, in which we are modeling the forward and reverse reactions of ligand-receptor binding and dissociation, respectively. First, a wait time is chosen according to an exponential distribution with mean value 1/(*k*<sub>bind</sub> + *k*<sub>dissociate</sub>); that is, λ is equal to the sum of reaction rates *k*<sub>bind</sub> + *k*<sub>dissociate</sub>. The probability that the event corresponds to a binding reaction is given by

Pr(*L* + *T* → *LT*) = *k*<sub>bind</sub>/(*k*<sub>bind</sub> + *k*<sub>dissociate</sub>)

and the probability that the event corresponds to a dissociation reaction is

Pr(*LT* → *L* + *T*) = *k*<sub>dissociate</sub>/(*k*<sub>bind</sub> + *k*<sub>dissociate</sub>)

**STOP**: Verify that these two probabilities sum to 1.
{: .notice--primary}

The process of selecting a reaction is visualized in the figure below.

![image-center](../assets/images/chemotaxis_visualizessa.png){: .align-center}
A visualization of a single reaction event used by the Gillespie algorithm for ligand-receptor binding/dissociation. Red circles represent ligands (*L*), and orange wedges represent receptors (*T*). The wait time for the next reaction is drawn from an exponential distribution with mean 1/(*k*<sub>bind</sub> + *k*<sub>dissociate</sub>). The probability of this event corresponding to a binding or dissociation reaction is proportional to the rate of the respective reaction.
{: style="font-size: medium;"}

## Specifying ligand-receptor binding with a single BioNetGen rule

Throughout this module, we will employ <a href="http://bionetgen.org/" target="_blank">BioNetGen</a> to build particle-free simulations of chemotaxis applying the Gillespie algorithm.

We will have two molecules corresponding to the ligand and receptor `L` and `T` that we call `L(t)` and `T(l)`, respectively. The `(t)` specifies that molecule `L` contains a binding site with `T`, and the `(l)` specifies a component binding to `L`. We will use these components later when specifying reactions. We do not have to use `t` and `l` for this purpose, but it will make our model easier to understand.

BioNetGen reaction rules are written similarly to chemical equations. The left side of the rule includes the reactants, which are followed by a unidirectional or bidirectional arrow, indicating the direction of the reaction, and the right side of the rule includes the products. After the reaction we indicate the rate constant of reaction; if the reaction is bi-directional, then we separate the forward and backward reaction rate constants with a comma.

For example, to code up the bi-directional reaction `A + B <-> C` with forward rate `k1` and reverse rate `k2`, we would write `A + B <-> C k1, k2`.

Our model consists of a single bidirectional reaction and will have only a single rule. The left side of this rule will be `L(t) + T(l)`; by specifying `L(t)` and `T(l)`, we indicate to BioNetGen that we are only interested in *unbound* ligand and receptor molecules. If we had wanted to select any ligand molecule, then we would have simply written `L + T`.

On the right side of the rule, we will have `L(t!1).T(l!1)`, which indicates the formation of the intermediate. In BioNetGen, `!` indicates formation of a bond; and a unique character specifies the possible location of this bond. In our case, we use the character `1`, so that the bond is represented by `!1`. The symbol `.` is used to indicate that the two molecules are joined into a complex.

Since the reaction is bidirectional, we will use `k_lr_bind` and `k_lr_dis` to denote the rates of the forward and reverse reactions, respectively. (We will specify values for these parameters later.)

As a result, this reaction is shown below. We name our rule specifying the ligand-receptor reaction `LR`.

~~~ ruby
LR: L(t) + T(l) <-> L(t!1).T(l!1) k_lr_bind, k_lr_dis
~~~

The following tutorial shows how to implement this rule in BioNetGen and use the Gillespie algorithm to determine the equilibrium of a reversible ligand-receptor binding reaction.

[Visit tutorial](tutorial_lr){: .btn .btn--primary .btn--large}
{: style="font-size: 100%; text-align: center;"}

## Does a simulation confirm our steady state calculations?

We previously showed a worked example in which a system with 10,000 free ligand molecules and 7,000 free receptor molecules produced the following steady state concentrations using bonding rates of *k*<sub>bind</sub> = 0.0146((molecules/µm<sup>3</sup>)<sup>-1</sup>)s<sup>-1</sup> and *k*<sub>dissociate</sub> = 35s<sup>-1</sup>.

* [*LT*] = 4793
* [*L*] = 5207
* [*T*] = 2207

The BioNetGen model covered in the previous tutorial uses the same number of initial molecules and the same reaction rates. The system evolves via the Gillespie algorithm, and we track the concentration of free ligand molecules, ligand molecules bound to receptor molecules, and free receptor molecules over time. Our goal is to see whether the concentrations reach a steady-state, and whether the steady-state matches our calculation.

The figure below demonstrates that the Gillespie algorithm quickly converges to the same values as the ones that we obtained by hand in the last lesson. As a result, we can see the power of using a particle-free stochastic simulator to quickly obtain a result without needing to perform any mathematical calculations.

![image-center](../assets/images/chemotaxis_tutorial4_ssa.png){: .align-center}
A concentration plot over time for ligand-receptor dynamics via a BioNetGen simulation employing the Gillespie algorithm. The concentrations reach a steady state at the end of the simulation that matches the concentrations identified by hand.
{: style="font-size: medium;"}

Yet this simple ligand-receptor model is just the beginning of our study of chemotaxis. In the next section, we will delve into the complex biochemical details of chemotaxis. Furthermore, we will see that the Gillespie algorithm for stochastic simulations will scale easily as our model of this system grows more complex.

[^Munroe]: Randall Munroe. What If? [Available online](https://what-if.xkcd.com/)

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

[^Hlavacek2003]: Hlavacek WS, Faeder JR, Blinov ML, Perelson AS, Goldsten B. 2003. The complexity of complexes in signal transduction. Biotechnology and Bioengineering 84(7):783-94. [Available online](https://onlinelibrary.wiley.com/doi/abs/10.1002/bit.10842)

[^Hlavacek2006]: Hlavacek WS, Faeder JR, Blinov ML, Posner RG, Hucka M, Fontana W. 2006. Rules for modeling signal-transduction systems. Science Signaling 344:re6. [Available online](https://stke.sciencemag.org/content/2006/344/re6.long)

[^ParkinsonLab]: Parkinson Lab website. [website](http://chemotaxis.biology.utah.edu/Parkinson_Lab/projects/ecolichemotaxis/ecolichemotaxis.html)

[^Schwartz14]: Schwartz R. Biological Modeling and Simulaton: A Survey of Practical Models, Algorithms, and Numerical Methods. Chapter 14.1.

[^Schwartz17]: Schwartz R. Biological Modeling and Simulaton: A Survey of Practical Models, Algorithms, and Numerical Methods. Chapter 17.2.

[^Li2004]: Li M, Hazelbauer GL. 2004. Cellular stoichimetry of the components of the chemotaxis signaling complex. Journal of Bacteriology. [Available online](https://jb.asm.org/content/186/12/3687)

[^Stock1991]: Stock J, Lukat GS. 1991. Intracellular signal transduction networks. Annual Review of Biophysics and Biophysical Chemistry. [Available online](https://www.annualreviews.org/doi/abs/10.1146/annurev.bb.20.060191.000545)

[^Spiro1997]: Spiro PA, Parkinson JS, and Othmer H. 1997. A model of excitation and adaptation in bacterial chemotaxis. Biochemistry 94:7263-7268. [Available online](https://www.pnas.org/content/94/14/7263).

[Next lesson](home_biochem){: .btn .btn--primary .btn--large}
{: style="font-size: 100%; text-align: center;"}
