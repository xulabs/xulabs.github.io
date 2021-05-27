---
permalink: /prologue/random-walk
title: "An Introduction to Random Walks"
sidebar:
 nav: "prologue"
 nav: "prologue"
toc: true
toc_sticky: true
---

## The wanderlust of a single particle

We have mentioned that our experience of the world is often influenced by the random interactions of objects that we cannot see. Our goal is to see how randomness can help us understand how zebras get their stripes, and to this end, we will consider a simpler phenomenon by observing the movement of a single particle taking a **random walk** in a two-dimensional plane. At each step, the particle moves a single unit in a randomly chosen direction.

**STOP**: After *n* steps, how far do you think the particle will have traveled (as the crow flies) from its starting point?
{: .notice--primary}

Let's generate an animation of a particle following a random walk. The video below shows a randomly walking particle, shown in red, taking 1000 steps.

<center>
<iframe width="640" height="360" src="../assets/random_walk_1.mp4" frameborder="0" allowfullscreen></iframe>
</center>

The distance that the particle wanders from its starting point may surprise you. And yet the astute scientist would point out that this is just a single particle; perhaps the typical particle would be much more of a homebody.

The particle's movements are random, but the *average-case* behavior of the particle can be predicted, as the following theorem indicates. For mathematics lovers, we explain why this theorem is true in an optional bonus section at the bottom of this page.

**Random Walk Theorem:** After *n* steps of unit length in a random walk, a particle will on average find itself a distance of approximately $$\sqrt{n}$$ from its origin.

## From one particle to many

The Random Walk Theorem does not say that after *n* steps a particle will be exactly $$\sqrt{n}$$ from the origin, any more than we would expect that in flipping a coin 2,000 times the coin will come up heads exactly 1,000 times. Yet the statement about the particle's average behavior is powerful. If we animate the action of many independent particles following random walks, then we will see that although some particles hug their starting point and some wind up far away, most particles steadily move outward as the simulation continues.

<center>
<iframe width="640" height="360" src="../assets/random_walk_200.mp4" frameborder="0" allowfullscreen></iframe>
</center>

If you are interested in seeing how to build this random walk simulation as an introduction to the software that we will soon be using for biological modeling, then please visit the following software tutorial. This tutorial uses **CellBlender**, an add-on to the popular open graphics software program **Blender**, that allows us to create and visualize biological models.

We have designed this course so that you can appreciate the key ideas behind the biological models that we build without following software tutorials. But we also provide these tutorials so that you can explore the modeling software that we have used to generate our conclusions. If you find this software helpful, perhaps you can even use this software in your own work!

[Visit tutorial](tutorial-random-walk){: .btn .btn--primary .btn--large}
{: style="font-size: 100%; text-align: center;"}

## Brownian motion: big numbers in small spaces

Our experience of the world confirms what we see in the animations produced by CellBlender. The seemingly random movements of particles suspended in a medium via **Brownian motion** will cause those particles to move away from their starting point, even if the concentration of these particles is uniform. We understand, for example, that an infected COVID-19 patient can infect many others in an enclosed space in a short time frame. To take a less macabre example, we also know that when a cake is baking in the oven at home, we will not need to wait long for wonderful smells to waft outward from the kitchen.

Why should a scientist care about random walks? Later in this course, we will see that the random walk model is at the core of a simple but powerful approach that bacteria like *E. coli* use to explore their environment in the hunt for food. In the next lesson, we will see that mimicking the random movements of particles will be important for building a biological model in which we allow particles to move naturally and interact when they collide.

Before continuing, we point you to a beautiful animation illustrating just how far a single randomly moving particle can travel in a relatively small amount of time. This animation, which shows a simulation of the path taken by a glucose molecule as the result of Brownian motion, starts at 6:10 of the following excellent instructional video developed by the late Joel Stiles.

<center>
<iframe width="640" height="360" src="https://www.youtube-nocookie.com/embed/KQgydF-fXvc?start=370" frameborder="0" allowfullscreen></iframe>
</center>

[Next lesson](animals){: .btn .btn--primary .btn--large}
{: style="font-size: 100%; text-align: center;"}

## (Optional) A proof of the Random Walk Theorem

The Random Walk Theorem states that the average distance that a randomly walking particle will find itself from its starting point after taking *n* steps of unit length is $$\sqrt{n}$$. Below, we provide a justification for why this is true for interested learners who are familiar with probability.

Let <b>x<sub><i>i</i></sub></b> denote the random variable corresponding to the vector of the particle's *i*-th step.  The distance *d* traveled by the particle can be represented by the sum of all the <b>x<sub><i>i</i></sub></b>,

$$d = \mathbf{x_1} + \mathbf{x_2} + \cdots + \mathbf{x_n} \,.$$

We will show that the expected value of <i>d</i><sup>2</sup> is equal to *n*. First note that

$$d^2 = (\mathbf{x_1} + \mathbf{x_2} + \cdots + \mathbf{x_n}) \cdot (\mathbf{x_1} + \mathbf{x_2} + \cdots + \mathbf{x_n})\,.$$

After expansion, we obtain

$$
\begin{align*}
d^2 = ~ & \mathbf{x_1} \cdot (\mathbf{x_1} + \mathbf{x_2} + \cdots + \mathbf{x_n})\\
+ & \mathbf{x_2} \cdot (\mathbf{x_1} + \mathbf{x_2} + \cdots + \mathbf{x_n})\\
+ & \cdots\\
+ & \mathbf{x_n} \cdot (\mathbf{x_1} + \mathbf{x_2} + \cdots + \mathbf{x_n}) \,.
\end{align*}
$$

Finally, we rearrange this equation so that the terms $$\mathbf{x_1} \cdot \mathbf{x_1}$$, $$\mathbf{x_2} \cdot \mathbf{x_2}$$, and so on occur first, and the remaining terms appear last. This allows us to write <i>d</i><sup>2</sup> as follows.

$$d^2 = \sum_{i=1}^n (\mathbf{x_i} \cdot \mathbf{x_i}) + \sum_{i \neq j} (\mathbf{x_i} \cdot \mathbf{x_j})\, .$$

The right side of this equation is the sum of <i>n</i><sup>2</sup> dot products.  When we take the expectation of both sides, we can apply a fundamental theorem called the "linearity of expectation", which states that for any two random variables $$x$$ and $$y$$, the expectation of their sum $$\mathbb{E}(x + y)$$ is equal to the sum of the corresponding expectations $$\mathbb{E}(x) + \mathbb{E}(y)$$:

$$\mathbb{E}(d^2) = \sum_{i=1}^n \mathbb{E}(\mathbf{x_i} \cdot \mathbf{x_i}) + \sum_{i \neq j} \mathbb{E}(\mathbf{x_i} \cdot \mathbf{x_j})\, .$$

For any *i*, $$\mathbf{x_i} \cdot \mathbf{x_i}$$ is just the length of the vector $$x_i$$, which is equal to 1.  On the other hand, the expected value of the dot product of any two random unit vectors is zero.  Therefore, the right side of the above equation can be simplified to give the equation

$$\mathbb{E}(d^2) = \sum_{i=1}^n 1 + \sum_{i \neq j} 0 = n + 0 = n\, ,$$

which is what we set out to prove.

A couple of notes before we continue. First, we did not use anything about the random walk being two-dimensional in this proof; therefore, it holds whether our particle is walking in two, three, or any number of dimensions.

Second, we technically did not show that the expected value of $$d$$ is $$\sqrt{n}$$, but rather that the expected value of $$d^2$$ is $$n$$. It is not true that $$\mathbb{E}(d)$$ is equal to $$\sqrt{n}$$, but rather that as $$n$$ grows, $$\mathbb{E}(d)$$ grows like $$c \cdot \sqrt{n}$$ for some constant factor $$c$$. A proof is beyond the scope of this course, but it can be shown that as $$n$$ goes off to infinity, $$\mathbb{E}(d)$$ tends toward $$\sqrt{(2/\pi)} \cdot \sqrt{n}$$. Who knew that the mathematics of random walks could be so complicated!
