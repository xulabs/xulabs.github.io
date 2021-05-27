---
permalink: /chemotaxis/home_signal
title: "Signaling and Ligand-Receptor Dynamics"
sidebar:
 nav: "chemotaxis"
toc: true
toc_sticky: true
---

## Cells can detect signals via bonding to receptor proteins

Chemotaxis is one example of many ways in which an organism must be able to perceive a change in its environment and react accordingly. This response is governed by a process called **signal transduction**, in which a cell identifies a stimulus outside the cell and then transmits this stimulus into the cell in order to effect a response.

Although we did not focus on the details at that time, we have already seen an example of signal transduction when we discussed the activation of transcription factors in the [previous module](motifs/transcription). When a certain type of molecule's extracellular concentration increases, **receptor proteins** on the outside of the cell have more frequent bonding with these molecules and are therefore able to detect changes in molecular concentration. This "signal" is then "transduced" via a series of internal chemical processes that changes a transcription factor into an active state.

In the case of chemotaxis, *E. coli* has receptor proteins that detect attractants such as glucose by binding to and forming a complex with these attractant **ligands**. The cell also contains receptors to detect repellents, but in this module, we will focus primarily on attractants.

In this lesson, we will discuss how the bacterium is able to detect this molecular signal; in the next lesson, we focus on how the bacterium can convert the detected signal into an internal sequence of reactions that lead to a change in movement. See the figure below for a high-level overview of this process.

![image-center](../assets/images/chemotaxis_signal.png){: .align-center}
An overview of the signaling pathway of chemotaxis. The red circles represent attractant ligands(L). When ligands bind to receptors, this signal is transduced via a series of enzymes, and it finally influences the rotation direction of a flagellum. We will discuss how this response is achieved in a later lesson.
{: style="font-size: medium;"}


## Modeling ligand-receptor dynamics

Although *E. coli* has different types of surface receptors that can sense a variety of different attractant/repellent ligands in its environment, we will focus on how to model the binding of a single type of receptor to a single type of attractant ligand.

The chemical reactions that we have considered earlier in this course are **irreversible**, meaning they can only proceed in one direction. For example, in the prologue's reaction-diffusion model for [Turing patterns](prologue/animals), we had the reaction *A* + 2*B* → 3*B*, which we conceptualized as two predators eating a prey and reproducing. But we did not have the reverse reaction 3*B* → *A* + 2*B*.

To model ligand-receptor dynamics, we will use a **reversible** reaction that proceeds continuously in both directions at possibly different rates. If a ligand collides with a receptor, then there is some probability that the two molecules will bond into a complex. But at the same time, in any unit of time, there is also some probability that a bound receptor-ligand complex will **dissociate** into two separate molecules. In a future module, we will discuss the biochemical details underlying what makes two molecules more or less likely to bond, but for now, we assert that the more suited a receptor is to a ligand, the higher the bonding rate and the lower the dissociation rate.

Why should ligand-receptor bonding be reversible? First, surface receptors are typically complicated molecules, and it would be costly to an organism if it needed to keep manufacturing surface receptors rather than sometimes releasing bound ligands. Second, if complexes did not dissociate, then a brief increase in ligand concentration would be detected by an organism indefinitely. We will say more about how the cell responds to a *changing* concentration of ligand soon.

For now, we will start building a model of ligand-receptor dynamics. We denote the receptor molecule by *T*, the ligand molecule by *L*, and the bound complex as *TL*. We have the **forward reaction** *T* + *L* → *TL*, which takes place at some rate *k*<sub>bind</sub>, and the **reverse reaction** *TL* → *T* + *L*, which takes place at some rate *k*<sub>dissociate</sub>. If we start with a free floating supply of *T* and *L* molecules, what will happen?

*TL* will initially be formed quickly at the expense of the free-floating *T* and *L* molecules; the reverse reaction will not occur because of the lack of *TL* complexes. As the concentration of *TL* grows and the concentrations of  *T* and *L* decrease, the rate of increase in *TL* will slow. Eventually, the number of *TL* complexes being formed by the forward reaction will balance the number of *TL* complexes being split apart by the reverse reaction. At this point, called a **steady state** or **equilibrium**, the concentration of all particles will stabilize.

## Calculation of steady state concentration in a reversible ligand-receptor reaction

In fact, we can calculate the steady state concentrations of *T* and *L* for our reversible reaction by hand.  Suppose that we begin with initial concentrations of *T* and *L* that are represented by *t*<sub>0</sub> and *l*<sub>0</sub>, respectively. Let [*L*], [*T*], and [*LT*] denote the concentrations of the three molecule types. And assume that the reaction rate constants *k*<sub>bind</sub> and *k*<sub>dissociate</sub> are fixed.

Our goal is to find the steady state concentration of *LT*. When this occurs, we know that the rate of production of *LT* is equal to the rate of its dissociation; in other words, we know that

*k*<sub>bind</sub> · [*L*] · [*T*] = *k*<sub>dissociate</sub> · [*LT*].

We also know that by the law of conservation of mass, the concentrations of *L* and *T* molecules are always constant across the system. In particular, the number of these particles is equal to their initial concentrations. That is, at any time point, we have that

[*L*] + [*LT*] = *l*<sub>0</sub>

and that

[*T*] + [*LT*] = *t*<sub>0</sub>.

Solving these equations for [*L*] and [*T*] yields the following two equations:

[*L*] = *l*<sub>0</sub> - [*LT*]<br>
[*T*] = *t*<sub>0</sub> - [*LT*]

We will now substitute the expressions on the right for [*L*] and [*T*] into our original steady state equation:

*k*<sub>bind</sub> · (*l*<sub>0</sub> - [*LT*]) · (*t*<sub>0</sub> - [*LT*]) = *k*<sub>dissociate</sub> · [*LT*]

Expanding the left side of this equation gives us the following updated equation:

*k*<sub>bind</sub> · [*LT*]<sup>2</sup> - (*k*<sub>bind</sub> · *l*<sub>0</sub> + *k*<sub>bind</sub> · *t*<sub>0</sub>) · [*LT*] +  = *k*<sub>dissociate</sub> · [*LT*] + *k*<sub>bind</sub> · *l*<sub>0</sub> · *t*<sub>0</sub>

Finally, we subtract the right side of this equation from both sides:

*k*<sub>bind</sub> · [*LT*]<sup>2</sup> - (*k*<sub>bind</sub> · *l*<sub>0</sub> + *k*<sub>bind</sub> · *t*<sub>0</sub> + *k*<sub>dissociate</sub>) · [*LT*] + *k*<sub>bind</sub> · *l*<sub>0</sub> · *t*<sub>0</sub> = 0

This equation may look daunting, but most of its components are constants. In fact, the only unknown is [*LT*], which makes this a quadratic equation, or an equation of the form *a* · *x*<sup>2</sup> + *b* · *x* + *c* = 0 for constants *a*, *b*, and *c* and a single unknown *x*. For this quadratic equation, we have the constants *a* = *k*<sub>bind</sub>, *b* = - (*k*<sub>bind</sub> · *l*<sub>0</sub> + *k*<sub>bind</sub> · *t*<sub>0</sub> + *k*<sub>dissociate</sub>), and *c* = *k*<sub>bind</sub> · *l*<sub>0</sub> · *t*<sub>0</sub>.

The quadratic formula --- which you may have thought you would never use again --- tells us that the equation *a* · *x*<sup>2</sup> + *b* · *x* + *c* = 0  has solutions for *x* given by the following equation:

$$x = \dfrac{-b \pm \sqrt{b^2 - 4 \cdot a \cdot c}}{2 \cdot a}$$

**STOP**: Use the quadratic formula to solve for [*LT*] in our previous equation and find the steady state concentration of *LT*. How can we use this solution to find the steady state concentrations of *L* and *T* as well?
{: .notice--primary}

Now that we have reduced the computation of the steady state concentration of *LT* to the solution of a quadratic equation, let's compute this steady state concentration for a sample collection of parameters. We will then change the parameters and see how the steady state concentration changes.

Say that we are given the following parameter values (the units of these parameters are not important for this toy example):
* *k*<sub>bind</sub> = 2;
* *k*<sub>dissociate</sub> = 5;
* *l*<sub>0</sub> = 50;
* *t*<sub>0</sub> = 50.

Substituting these values into the quadratic equation, we obtain the following:

* *a* = *k*<sub>bind</sub> = 2
* *b* = - (*k*<sub>bind</sub> · *l*<sub>0</sub> + *k*<sub>bind</sub> · *t*<sub>0</sub> + *k*<sub>dissociate</sub>) = -205
* *c* = *k*<sub>bind</sub> · *l*<sub>0</sub> · *t*<sub>0</sub> = 5000

That is, we are solving the equation 2 · [*LT*]<sup>2</sup> - 205 · [*LT*] + 5000 = 0. Using the quadratic formula to solve for [*LT*] gives

$$[LT] = \dfrac{205 \pm \sqrt{205^2 - 4 \cdot 2 \cdot 5000}}{2 \cdot 2} = 51.25 \pm 11.25$$.

It would seem that there are *two* solutions: 51.25 + 11.25 = 62.5 and 51.25 - 11.25 = 40. However, because *l*<sub>0</sub> and *t*<sub>0</sub>, the respective initial concentrations of *L* and *T*, are both equal to 50, we cannot have that the steady state concentration of *LT* is 62.5; as a result, it must be 40.

Now that we know the steady state concentration of *LT*, we can recover the values of [*L*] and [*T*] too:

[*L*] = *l*<sub>0</sub> - [*LT*] = 10<br>
[*T*] = *t*<sub>0</sub> - [*LT*] = 10

What if the forward reaction were slower? We would imagine that the equilibrium concentration of *LT* would decrease, since the reverse reaction will occur faster than the forward reaction. For example, if we change *k* to 1, then we obtain the following adjusted parameter values:

* *a* = *k*<sub>bind</sub> = 1

* *b* = - (*k*<sub>bind</sub> · *l*<sub>0</sub> + *k*<sub>bind</sub> · *t*<sub>0</sub> + *k*<sub>dissociate</sub>) = -105

* *c* = *k*<sub>bind</sub> · *l*<sub>0</sub> · *t*<sub>0</sub> = 2500

In this case, if we solve for [*LT*], we obtain [*LT*] = 36.492; the steady state concentration has decreased as anticipated.

**STOP**: What do you think will happen to the steady state concentration of *LT* if the initial concentration (*l*<sub>0</sub>) increases or decreases? What if the dissociation rate (*k*<sub>dissociate</sub>) increases or decreases?  Confirm your prediction by changing the parameters above and solving the quadratic formula for [*LT*].
{: .notice--primary}

## Steady state ligand-receptor concentrations for an experimentally verified example

Let's use our formula to show how we could determine the steady state concentration of bound receptor-ligand complexes using values obtained from experimental results. We will model an *E. coli* cell with 7,000 receptor molecules in an environment containing 10,000 ligand molecules. The experimentally verified bonding rate is *k*<sub>bind</sub> = 0.0146((molecules/µm<sup>3</sup>)<sup>-1</sup>)s<sup>-1</sup>, and the dissociation rate constant is *k*<sub>dissociate</sub> = 35s<sup>-1</sup>.[^Li2004][^Spiro1997][^Stock1991]

As an aside, we note that if you find the above units confusing, you are not alone. To clarify these units, consider that the concentration of a particle will be measured in (molecules/µm<sup>3</sup>), or number of molecules per unit volume. So when we multiply the bonding rate by the concentrations of *L* and *T* particles, then the units become

((molecules/µm<sup>3</sup>)<sup>-1</sup>)s<sup>-1</sup> · (molecules/µm<sup>3</sup>) · (molecules/µm<sup>3</sup>) = (molecules/µm<sup>3</sup>)s<sup>-1</sup>

That is, the resulting units are in molecules/µm<sup>3</sup> per second, which corresponds to the rate at which the concentration of *LT* complexes is increasing.

On the other hand, when *LT* complexes dissociate, we multiply the dissociation constant by the units of *LT* concentration and obtain the same units as before:

(s<sup>-1</sup>) · (molecules/µm<sup>3</sup>)  = (molecules/µm<sup>3</sup>)s<sup>-1</sup>.

For these parameters, we obtain the following constants *a*, *b*, *c* in the quadratic equation:

* *a* = *k*<sub>bind</sub> = 0.0146
* *b* = - (*k*<sub>bind</sub> · *l*<sub>0</sub> + *k*<sub>bind</sub> · *t*<sub>0</sub> + *k*<sub>dissociate</sub>) = -283.2
* *c* = *k*<sub>bind</sub> · *l*<sub>0</sub> · *t*<sub>0</sub> = 1022000

When we solve for [*LT*] in the quadratic equation, we obtain [*LT*] = 4793. Now that we have this value along with *l*<sub>0</sub> and *t*<sub>0</sub>, we can solve for [*L*] and [*T*] as well:

[*L*] = *l*<sub>0</sub> - [*LT*] = 5207<br>
[*T*] = *t*<sub>0</sub> - [*LT*] = 2207


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

[Next lesson](home_signalpart2){: .btn .btn--primary .btn--large}
{: style="font-size: 100%; text-align: center;"}


<!--
## Extra extra

BNG supports simulation with Ordinary Differential Equation (ODE) and with Stochastic Simulation Algorithm (SSA, also called Gillespie algorithm). The method is passed in as argument `method=>"ode"` or `method=>"ssa"`.
 - ODE: When simulating a system, we need to define how the system evolves through time. In *continuous* simulation of chemical reactions, the state of the system can be reported given any point in time. The reactions rules specify the rate of change for concentration of the involved species, and they are differential equations. For example, *d[L]/dt=k<sub>dissociate</sub>[L.T] - k<sub>bind</sub>[L][T]*.[^Schwartz14]
 - SSA: When simulating the change of the system through time, we define states of the system. Transition can happen between states that differ by one reaction event. We track the *discrete* amount of each reactants and simulate the system via transition of the states[^Schwartz17]. For example, the state can transit from [#L=100, #T=50, #L.T=0] to [#L=99, #T=49, #L.T=1], with probability determined both by reaction rate *k<sub>bind</sub>* and the the number of ways to choose the L and T molecules.[^Schwartz17] For using SSA, the measurement of abundance of molecules should actually be number of molecule instead of concentration.

Remove the ODE results
![image-center](../assets/images/chemotaxis_tutorial4.png){: .align-center}
Concentration plot for ligand-receptor dynamics with ODE simulation. The concentrations reach a steady state at the end of the simulation.
{: style="font-size: medium;"}
-->
