---
permalink: /chemotaxis/home_exercise
title: "Exercises"
sidebar:
 nav: "chemotaxis"
toc: true
toc_sticky: true
---

## How do *E. coli* respond to repellents?

Just as *E. coli* has receptors that bond to attractant ligands, it has other receptors that can bond to **repellent** ligands.

**Exercise 1:** Based on what we have learned in this module about how *E. coli* and other bacteria act in the presence of an attractant, what do you think that the chemotaxis response is in the presence of a repellent? How do you think that the bacterium adjusts to relative changes in repellent?
{: .notice--info}

**Exercise 2:** In the [phosphorylation tutorial](tutorial_phos), we defined the rate constant for free CheA autophosphorylation `k_T_phos`, and specified that when the receptor complex is bound to an attractant molecule, the autophosphorylation rate constant becomes `0.2 · k_T_phos`. When the receptor complex is bound to a **repellent** molecule, we will change the autophosphorylation rate constant to `5 · k_T_phos`. Adapt the BioNetGen model accordingly, and then run your simulation with `L0 = 5000` and `L0 = 1e5` repellent ligand molecules added at the beginning of the simulation, and run the simulation for 3 seconds. How does the concentration of phosphorylated CheY change? What do you conclude?
{: .notice--info}

## What if there are multiple attractant sources?

The simulations in this chapter became quite complex, but there is one way in which the reality is even more complicated. Not only can *E. coli* sense both repellents and attractants, but it is able to detect *more than one* attractant gradient at the same time.  This has a clear evolutionary purpose in an environment of multiple sparsely populated food sources. In this section, we will explore whether the chemotaxis mechanism allows cells to navigate through more realistic nutrient distributions.

**Exercise 1:**  In reality, *E. coli* has different receptors specific for different types of attractants. Modify your model from the [adaptation tutorial](tutorial_senseadap) to reflect two types of receptor, each specific to its own ligand (call them *A* and *B*). Assume that we have 3500 receptor molecules of each type.\\
 **Hint:** you will not need to have additional molecules in addition to `L` and `T`. Instead, specify additional states for the two molecules that we already have; for example `L(t,Lig~A)` only binds with `T(l,Lig~A)`. Don't forget to update `seed species` as well!
{: .notice--info}

**Exercise 2:** What will happen if after the cell adapts to attractant *A*, molecules of *B* are  suddenly added to the system? Model this scenario by assuming that after the cell adapts to `1e6` molecules of *A*, suddenly `1e6` molecules of *B* are added. Observe the concentration of phosphorylated CheY. Is the cell able to respond to *B* after adapting to the concentration of ligand *A*? Why is the change in CheY phosphorylation different from the scenario in which we release the two different ligands concurrently?\\
 **Hint:** the hint for the previous exercise also applies here.
{: .notice--info}

**Exercise 3:** In the [chemotactic walk tutorial](tutorial_walk), we have a concentration gradient growing exponentially toward the goal (1500, 1500), so that *L(x,y)* = 100 · 10<sup>8 · (1-*d*/*D*)</sup>. In this exercise, we will modify this tutorial to simulate having multiple different goals, presumably from two different ligand types. To do so, include another goal at location (-1500, 1500), and a similar exponential concentration gradient growing from the center to the goal. The new concentration of ligands, [*L*] will be *L(x,y)* = 100 · 10<sup>8 · (1-*d*<sub>1</sub>/*D*<sub>1</sub>)</sup> + 100 · 10<sup>8 · (1-*d*<sub>2</sub>/*D*<sub>2</sub>)</sup>, where *d*<sub>1</sub> is the distance from *(x,y)* to goal1 (1500, 1500), *d*<sub>2</sub> is the distance from *(x,y)* to goal2 (-1500, 1500), and *D*<sub>1</sub> and *D*<sub>2</sub> are the distances from the origin to the two respective goals. Run your simulation with a background tumbling frequency of once every second, and visualize the trajectories of several cells. Are the cells able to find one of the goals? How long does it take them?
{: .notice--info}

## Is the actual tumbling reorientation used by E. coli smarter than our model?

Earlier in this module, we said that when *E. coli* tumbles, the degree of reorientation is actually not uniformly random from 0° to 360°. With background ligand concentration, the degree of reorientation approximately follows a normal distribution with mean of 68° (or equivalently, 1.19π) and standard deviation of 36° (equivalently, 0.63π). Recent research suggests that when the cell is moving up the gradient, the degree of reorientation is smaller [^Saragosti2011]. Although currently we don't have definitive measurements for the smaller angle of reorientation when moving up the gradient, let's specify it is 0.1 π smaller. Before actually implementing, what do you predict this reorientation strategy would change the chemotaxis responses? Do you think it brings some evolutionary advantages?

**Exercise:** Please modify your model from [chemotactic walk tutorial](tutorial_walk) to change the random uniform sampling to this "smarter" sampling. Please quantitatively compare the performance for the chemotactic walk strategy, and this smarter strategy by calculating the mean and standard deviation of each cell's distance to the goal for 500 cells with `time_exp = [0.2, 0.5, 1.0, 2.0, 5.0]`. How much faster can the cells find the goal? Why faster?
{: .notice--info}

## Can't get enough BioNetGen?

As we have seen in this module, BioNetGen is very good at simulating systems that involve a large number of species and particles but can be summarized with a small set of rules. Polymerization reactions offer another good example of such a system.

**Exercise 1:** Imagine you were to implement a BioNetGen simulation for a hypothetical reaction system. What do you need to know about the system before implementing? What do you need to define in your program?
{: .notice--info}

**Polymerization** is the process by which **monomer** molecules combine into chains called **polymers**. Biological polymers are everywhere, from DNA (formed of monomer nucleotides) to proteins (formed of monomer amino acids) to lipids (formed of monomer fatty acids). For another example, polyvinyl chloride (PVC) is formed from many vinyl monomers.

We would like to simulate the polymerization of copies of a monomer *A* to form polymer *AAAAAA*..., where the length of the polymer is allowed to vary. To do so, we will write our reaction as *A*<sub><em>m</em></sub> + *A*<sub><em>n</em></sub> -> *A*<sub><em>m</em>+<em>n</em></sub>, where here *A*<sub>m</sub> denotes a polymer consisting of *m* copies of *A*. Using classical reaction rules, this would require an infinite number of reactions; will BioNetGen come to our rescue?

There are two sites on the monomer *A* that are involved in a polymerization reaction: the "head" and the "tail". We need the head on one monomer and the tail on another to be free for these two monomers to bind. The following BioNetGen model is inspired by the [BLBR model in official BioNetGen tutorials](https://github.com/RuleWorld/BNGTutorial/blob/master/CBNGL/BLBR.bngl).

Open a new `.bngl` file and save it as `polymers.bngl`. We will have only one molecule type: `A(h,t)`; the `h` and `t` indicating the "head" and "tail" binding sites, respectively. We will need to represent four reaction rules:

1. initializing the series of polymerization reactions: two unbound `A` forms an initial **dimer**, or two monomers joined together;
2. adding an unbound `A` to the "tail" of an existing polymer;
3. adding an existing polymer to the "tail" of an unbound `A`; and
4. adding an existing polymer to the "tail" of another polymer.

To select any species that is bound at a component, use the notation `!+`; for example, `A(h!+,t)` will select any `A` bound at "head", whether it is bound in a chain of one or one million monomers.

We will assume that all forward and reverse rates for each reaction occur at the same rate. For simplicity, we will set all forward and reverse reaction rates to be equal to 0.01.

What will our distribution of polymer lengths be? We will initialize our simulation with 1000 unbound *A* monomers and observe the formation of polymer chains of a few different lengths (1, 2, 3, 5, 10, and 20).  To do so, we select the pattern of containing *n* copies of *A* with the notation `A == x`. `Species` instead of `Molecules` is required for selecting polymer patterns.

~~~ ruby

begin seed species
	A(h,t) 1000
end seed species

begin observables
	Species A1 A==1
	Species A2 A==2
	Species A3 A==3
	Species A5 A==5
	Species A10 A==10
	Species A20 A==20
	Species ALong A>=30
end observables
~~~

For this model, we will try an alternative to the Gillespie (SSA) algorithm called **network-free simulation**. This approach is similar to the Gillespie algorithm, but instead of simulating transitions between states of the whole *system*, it tracks individual *particles*. In this polymerization model, the possible number of reactions is much higher than we had in chemotaxis models - we can have two polymers of any length reacting at any step, which slows down the Gillespie algorithm. In this case, we actually do not have very many particles compared to the (infinite) number of possible reactions, and so tracking each particle will be much faster for this model.

After building the model, run your simulation with the following command (note that we do not need the `generate_network()` command):

~~~ ruby
simulate({method=>"nf", t_end=>100, n_steps=>1000})
~~~

**Exercise 2:**What happens to the concentration of shorter polymers? What about the longer polymers? Try adjusting the lengths of the polymers that we are interested in. What happens if we also tweak the reaction rates so that bonding is a little more likely than dissociation? What if dissociation is more likely? Does this reflect what you would guess?
{: .notice--info}


[^Saragosti2011]: Saragosti J, Calvez V, Bournaveas, N, Perthame B, Buguin A, Silberzan P. 2011. Directional persistence of chemotactic bacteria in a traveling concentration wave. PNAS. [Available online](https://www.pnas.org/content/pnas/108/39/16235.full.pdf)

[^Saragosti2012]: Saragosti J., Siberzan P., Buguin A. 2012. Modeling *E. coli* tumbles by rotational diffusion. Implications for chemotaxis. PLoS One 7(4):e35412. [available online](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3329434/).

[^Berg1972]: Berg HC, Brown DA. 1972. Chemotaxis in Escherichia coli analysed by three-dimensional tracking. Nature. [Available online](https://www.nature.com/articles/239500a0)

[^Baker2005]: Baker MD, Wolanin PM, Stock JB. 2005. Signal transduction in bacterial chemotaxis. BioEssays 28:9-22. [Available online](https://pubmed.ncbi.nlm.nih.gov/16369945/)


[Next module](../coronavirus/home){: .btn .btn--primary .btn--large}
{: style="font-size: 100%; text-align: center;"}
