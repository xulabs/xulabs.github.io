---
permalink: /prologue/conclusion
title: "Conclusion: Turing Patterns are Fine-Tuned"
sidebar:
 nav: "prologue"
 toc: true
 toc_sticky: true
---

The Turing patterns that emerged from our particle simulations are a testament to the human eye's ability to find organization within the net behavior of tens of thousands of particles. For example, take another look at the video we produced that showed mottling in our particle simulator. Patterns are present, but they are also noisy --- even in the dark red regions we will have quite a few green particles, and vice-versa. The rapid inference of large-scale patterns from small-scale visual phenomena is one of the tasks that our brains have evolved to perform well.

<center>
<iframe width="750" height="360" src="../assets/gray_scott_11_by_11_f_1_k_1.mp4" frameborder="0" allowfullscreen>
</iframe>
</center>

Our reaction-diffusion system is remarkable because it is so **fine-tuned**, meaning that very slight changes in parameter values can lead to significant changes in the system. These changes could convert spots to stripes, or they could influence how clearly defined the boundaries of the Turing patterns are.

Robert Munafo provides a great figure, reproduced below, showing how the Turing patterns produced by the Gray-Scott model change as the kill and feed rates vary.[^robert] The kill rate increases along the *x*-axis, and the feed rate increases along the *y*-axis. Notice how quickly the patterns change! You may like to try tweaking the parameters of our own Gray-Scott simulator to see if you can reproduce these different patterns.

![image-center](../assets/images/xmorphia-parameter-map.jpg){: .align-center}

Later in this course, we will see an example of a biological system that is the opposite of fine-tuned. In a **robust** system, variation in parameters does not lead to substantive changes in the ultimate behavior of the system. Robust processes are vital for processes in which an organism needs to be resilient to small changes in its environment.

It turns out that although Turing's work offers a compelling argument for how zebras might have gotten their stripes, the exact mechanism by which these stripes form is still an unresolved question. However, the pigmentation of *zebrafish* does follow a Turing pattern because two types of pigment cells follow a reaction-diffusion model much like the one we presented above.[^zebrafish]

Furthermore, note the following two photos of giant pufferfish. These fish are genetically very similar, but their skin patterns are very different. What may seem like a drastic change in the appearance of the fish from spots to stripes is likely attributable to a small change of parameters in a fine-tuned biological system that, like all of life, is powered by randomness.

![image-center](../assets/images/Juvenile_Mbu_pufferfish.jpg){: .align-center}
A juvenile Mbu Pufferfish with a very familiar pattern![^youngfish]
{: style="font-size: medium;"}

![image-center](../assets/images/Giant_Puffer_fish_skin_pattern.jpg){: .align-center}
An adult Mbu Pufferfish exhibiting another familiar pattern![^pufferfish]
{: style="font-size: medium;"}

## A final note

Thank you for making it this far! We hope that you are enjoying the course. You can join the next module of the course by clicking on the "next module" button below. In the meantime, we ask that you complete the <a href="https://forms.gle/egmmBxGtBciDPYNS8" target="_blank">course survey</a> if you have not done so already.


[Next module](/motifs){: .btn .btn--primary .btn--large}
{: style="font-size: 100%; text-align: center;"}

[^robert]: "Reaction-Diffusion by the Gray-Scott Model: Pearson's Parametrization" © 1996-2020 Robert P. Munafo https://mrob.com/pub/comp/xmorphia/index.html

[^zebrafish]: Nakamasu, A., Takahashi, G., Kanbe, A., & Kondo, S. (2009). Interactions between zebrafish pigment cells responsible for the generation of Turing patterns. Proceedings of the National Academy of Sciences of the United States of America, 106(21), 8429–8434. https://doi.org/10.1073/pnas.0808622106

[^youngfish]: NSG Coghlan, 2006 [Creative Commons Attribution-Share Alike 3.0 Unported](https://creativecommons.org/licenses/by-sa/3.0/deed.en)

[^pufferfish]: Chiswick Chap, 20 February 2012, [Creative Commons Attribution-Share Alike 3.0 Unported](https://creativecommons.org/licenses/by-sa/3.0/deed.en)
