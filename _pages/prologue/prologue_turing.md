---
permalink: /prologue/turing
title: "Alan Turing and the Zebra's Stripes"
sidebar:
 nav: "prologue"
toc: true
toc_sticky: true
---

## Turing machines and the foundations of computer science

Our story begins with the unlikeliest of major characters: Alan Turing. If you have heard of Turing, then you might be surprised as to why he would appear in a course on biological modeling.

![image-center](../assets/images/alan_turing_npg_cc.png){: .align-center}
Alan Turing in 1951. © National Portrait Gallery, London.
{: style="font-size: medium; text-align: center;"}

Turing was a genius cryptographer during World War II and helped break several German ciphers. But his most famous scientific contribution was a 1936 paper in which he introduced what has come to be known as a **Turing machine**[^numbers]. This hypothetical computer consists of an infinitely long tape of cells and a reader that can read one cell at a time. Each cell consists of only a single number, and the machine can move one cell at a time, reading and rewriting cells according to a finite collection of internal rules. Turing's major insight was that such a machine, though simple, is enormously powerful. Nearly a century after his work, any task that a computer performs, from the device you are using to read this to the world's most powerful supercomputer, could be implemented by a Turing machine.

You may be shocked that a computer can ultimately be represented by such a simple machine, one that Joseph Weizenbaum called nothing more than "pebbles on toilet paper"[^weizenbaum]. Although they are not our focus here, if Turing machines interest you, then we include an excellent introductory video on Turing machines below, including a demonstration of how a Turing machine can be used to solve an example problem.

<iframe width="640" height="360" src="https://www.youtube-nocookie.com/embed/PLVCscCY4xI" frameborder="0" allowfullscreen></iframe>

Why spend time discussing Turing's foundational work on theoretical computer science?  Because this work enforces a theme of this course that we mentioned in the introduction, in that a computing machine built upon rules that are very simple can nevertheless produce emergent behavior that seems complex. We now will visit this theme in the context of biological modeling.

## Turing the biochemist

Two years before his untimely demise in 1954, Turing published his only paper on biochemistry, which centered on the question that we introduced in the introduction: “Why do zebras have stripes?”[^morphogenesis]

Turing was not approaching this question from the perspective of why zebras have evolved to have stripes --- this was unsolved in Turing's time, and recent research has indicated that the stripes may be helpful in warding off flies.[^zebra] Rather, Turing reasoned that just as computers can be represented by a simple machine, there must be some simple set of molecular "rules" that cause the stripes to appear on a zebra's coat.

In the next two lessons, we will introduce a particle simulation model based on Turing's ideas. We will explore how this model can be tweaked to explain not just the appearance of not just the zebra's stripes but also the leopard's spots.

[Next lesson](random-walk){: .btn .btn--primary .btn--large}
{: style="font-size: 100%; text-align: center;"}

[^numbers]: Turing, Alan M. (1936), "On Computable Numbers, with an Application to the Entscheidungsproblem", Proceedings of the London Mathematical Society, Ser. 2, Vol. 42: 230-265.

[^weizenbaum]: Weizenbaum, Joseph (1976), Computer Power and Human Reason (New York: W.H. Freeman).

[^morphogenesis]: Turing, Alan (1952). "The Chemical Basis of Morphogenesis" (PDF). Philosophical Transactions of the Royal Society of London B. 237 (641): 37–72. Bibcode:1952RSPTB.237...37T. doi:10.1098/rstb.1952.0012. JSTOR 92463.

[^zebra]: Caro, T., Izzo, A., Reiner, R. C., Walker, H., & Stankowich, T. (2014). The function of zebra stripes. Nature Communications, 5(1), 1–10. https://doi.org/10.1038/ncomms4535
