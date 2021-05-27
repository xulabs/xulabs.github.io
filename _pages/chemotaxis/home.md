---
permalink: /chemotaxis/home
title: "Introduction: Lost Immortals and Chemotaxis"
sidebar:
 nav: "chemotaxis"
---

<span style="font-size:larger;">by Shuanger Li and Phillip Compeau</span>

The book *What If?*[^Munroe], by Randall Munroe, compiles a collection of crazy scientific hypotheticals, paired with thorough discussions of what might happen if these situations occurred. Here is an example, called "Lost Immortals".

> If two immortal people were placed on opposite sides of an uninhabited Earth-like planet, how long would it take them to find each other? 100,000 years? 1,000,000 years?

One could imagine many ideas for how the immortals might find each other. For example, they could avoid the interiors of continents by moving to the coastlines. If they are allowed to discuss how to find each other in advance, then they could just agree to meet at the planet's North Pole --- assuming that the planet lacks polar bears.

But Munroe provides a solution to Lost Immortals that is both sophisticated and elegant. His proposed approach is quoted below.

> If you have no information, walk at random, leaving a trail of stone markers, each one pointing to the next. For every day that you walk, rest for three. Periodically mark the date alongside the cairn. It doesn’t matter how you do this, as long as it’s consistent. You could chisel the number of days into a rock, or lay out rocks to plot the number.
>
> If you come across a trail that’s newer than any you’ve seen before, start following it as fast as you can. If you lose the trail and can’t recover it, resume leaving your own trail.
>
> You don’t have to come across the other player’s current location; you simply have to come across a location where they’ve been. You can still chase one another in circles, but as long as you move more quickly when you’re following a trail than when you’re leaving one, you’ll find each other in a matter of years or decades.
>
> And if your partner isn’t cooperating—perhaps they’re just sitting where they started and waiting for you—then you’ll get to see some neat stuff.

You may be wondering what Lost Immortals has to do with biological modeling. In the previous two modules, we have already seen the power of randomness to provide answers to practical questions. Lost Immortals offers another benefit of randomness in the form of a **randomized algorithm**, or a method that employs randomness to solve a problem.

In fact, Munroe's randomized algorithm for Lost Immortals is inspired by nature; he calls the above approach "be an ant" because it mimics how ants explore their environment for resources. However, in this module, we will see that this algorithm is also similar to the method of exploration undertaken by a much smaller organism: our old friend *E. coli*.

Like other prokaryotes, *E. coli* is tiny, with a rod-shaped body that is 2µm long and 0.25 to 1µm wide.[^Pierucci1978] In exploring a vast world with sparse resources, *E. coli* finds itself in a situation comparable to the Lost Immortals.

The video below shows a collection of *E. coli* surrounding a sugar crystal. Think of this video the next time you leave a slice of cake out on the kitchen counter!
<iframe width="640" height="360" src="https://www.youtube.com/embed/F6QMU3KD7zw" frameborder="0" allowfullscreen></iframe>

The movement of organisms like the bacteria in the above video in response to a chemical stimulus is called **chemotaxis**. *E. coli* and other bacteria have evolved to move toward **attractants** (e.g., glucose, electron acceptors) and away from **repellents** (e.g., Ni<sup>2+</sup>, Co<sup>2+</sup>). But how?

In this module, we will dive into the chemotaxis process and ask a number of questions. How does a simple organism like *E. coli* sense an attractant or repellent in its environment? How does the bacterium change its internal state in response to this environment? And how does the internal response to a stimulus translate into an interpretable "algorithm" that the wandering *E. coli* implements to explore its environment?

[Next lesson](home_walk){: .btn .btn--primary .btn--large}
{: style="font-size: 100%; text-align: center;"}

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
